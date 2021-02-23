import java.io.File;
import java.io.RandomAccessFile;
import java.io.FileNotFoundException;
import java.io.IOException;

import java.util.Scanner;
import java.util.LinkedList;
import java.util.TreeMap;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Collections;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;

/*
 * Aaron Schwartz-Messing
 * Mordechai Schmutter
 */
public class fat32_reader
{
	private static RandomAccessFile fat;
	private static Info info;

	private static String volume;
	private static String currentDirectory;
	private static LinkedList<String> currentPath;
	private static TreeMap<String, Entry> dirEntries;

	private static LinkedList<Integer> freelist;
	
	/*
	 * This class keeps track of information from the BPB section.
	 * It also provides other basic information gathered from basic arithmetic on this information
	 */
	static class Info {

		int BPB_BytesPerSec;
		int BPB_SecPerClus;
		int BPB_RsvdSecCnt;
		int BPB_NumFATS;
		int BPB_FATSz32;

		int BPB_RootClus;

		/*
		 * This is basically the implementation of the "info" command
		 */
		@Override
		public String toString() {
			return 
			"BPB_BytesPerSec is 0x" + Integer.toHexString(BPB_BytesPerSec) + ", " + BPB_BytesPerSec + "\n" +
			"BPB_SecPerClus is 0x" + Integer.toHexString(BPB_SecPerClus) + ", " + BPB_SecPerClus + "\n" +
			"BPB_RsvdSecCnt is 0x" + Integer.toHexString(BPB_RsvdSecCnt) + ", " + BPB_RsvdSecCnt + "\n" +
			"BPB_NumFATS is 0x" + Integer.toHexString(BPB_NumFATS) + ", " + BPB_NumFATS + "\n" +
			"BPB_FATSz32 is 0x" + Integer.toHexString(BPB_FATSz32) + ", " + BPB_FATSz32;
		}

		/*
		 * Gives the offset (in bytes) of the beginning of the data region, relative to the first byte of the reserved region
		 */
		public long getDataOffset(int clusterNumber) {
			long getFirstSectorOfCluster = ((long)(clusterNumber - 2) * BPB_SecPerClus) + sectorOfStartOfDataRegion();
			return getFirstSectorOfCluster * BPB_BytesPerSec;
		}

		private int sectorOfStartOfDataRegion() {
			return BPB_RsvdSecCnt + (BPB_NumFATS * BPB_FATSz32);
		}

		public long getOffsetOfStartOfFatRegion() {
			return BPB_RsvdSecCnt * BPB_BytesPerSec;
		}


		/*
		 * Gives the offset (in bytes) of the beginning of the fat region, relative to the first byte of the reserved region
		 */
		public long getFatOffset(int clusterNumber) {
			long fatEntrySector = BPB_RsvdSecCnt + ((long)(clusterNumber * 4) / BPB_BytesPerSec);
			long fatEntryOffset = (long)(clusterNumber * 4) % BPB_BytesPerSec;
			return fatEntrySector * BPB_BytesPerSec + fatEntryOffset;
		}


		public int getNumbBytesPerCluster() {
			return BPB_BytesPerSec * BPB_SecPerClus;
		}
	}

	/*
	 * This class represents one 32-byte FAT entry. 
	 * The information that is important for this assignment is parsed out and stored in fields
	 */
	static class Entry {
		String DIR_Name;
		String DIR_ATTR;
		int nextCluster;
		int DIR_FileSize;

		byte[] bytes;

		Entry(byte[] array) {
			bytes = array;

			//compute DIR_Name
			DIR_Name = (new String(Arrays.copyOfRange(bytes, 0, 8))).trim();
			String extensionString = (new String(Arrays.copyOfRange(bytes, 8, 11))).trim();
			if (!extensionString.equals("")) DIR_Name += "." + extensionString;

			//compute DIR_ATTR
			switch((int)bytes[11]) {
				case 0x01: DIR_ATTR = "ATTR_READ_ONLY"; break;
				case 0x02: DIR_ATTR = "ATTR_HIDDEN"; break;
				case 0x04: DIR_ATTR = "ATTR_SYSTEM"; break;
				case 0x08: DIR_ATTR = "ATTR_VOLUME_ID"; break;
				case 0x0F: 
				case 0x1F:
				case 0x2F:
					DIR_ATTR = "ATTR_LONG_NAME"; break;
				case 0x10: DIR_ATTR = "ATTR_DIRECTORY"; break;
				case 0x20: DIR_ATTR = "ATTR_ARCHIVE"; break;
				default: DIR_ATTR = "ERROR!";
			}

			//compute nextCluster
			byte[] nextClusterNumberBytes = new byte[4];
			nextClusterNumberBytes[0] = bytes[26];
			nextClusterNumberBytes[1] = bytes[27];
			nextClusterNumberBytes[2] = bytes[20];
			nextClusterNumberBytes[3] = bytes[21];
			nextCluster = fat32_reader.bytesToInt(nextClusterNumberBytes);

			//compute filesize
			DIR_FileSize = bytesToInt(Arrays.copyOfRange(bytes, 28, 32));
		}
	}

	public static void main(String[] args) {
		//nulling out these fields for testing purposes
		fat = null;
		info = null;
		dirEntries = null;
		currentDirectory = null;
		volume = "Error: volume not found.";
		freelist = null;

		//validate number of arguments
		if (args.length != 1) {
			System.err.println("The only parameter expected is the name of the FAT32 image.");
			return;
		}

		//open the .img file as a RandomAccessFile
		try (RandomAccessFile raf = new RandomAccessFile(args[0], "rw")) {
			//fat is a static field. Storing the file in a field makes it easier for all of the methods to have access
			// to it. I assigned it to raf first to keep the compiler happy.
			fat = raf;

			//reads the important info from the BPB and stores it in an Info object in the "info" static field
			readBPBinfo();

			//establish root as current working directory, load fat entry information into "dirEntries" field 
			loadRoot();

			//read free list
			readFreeList();

			//begin taking user input
			Scanner sc = new Scanner(System.in);
			while (true) {
				//print prompt
				System.out.print(currentDirectory + "]");

				String cmd = sc.nextLine().trim();

				/*
				The reason that I originally added this condition was because I thought that I saw such a 
				limitation in the fat32_reader.c file. But since it wasn't in the instructions I'm taking it out.
				if (cmd.length() > 80) {
					System.out.println("Command too long. All commands must be <= 80 characters."); 
					continue;
				}
				*/

				//parse input command/parameters
				String[] tokens = cmd.split(" ");

				//declairing variables here so that the same name can be used in multiple switch cases
				//not sure whether I had to do this but I had some issues and this works so whatever
				long offset = 0;
				String fileName = "";
				String dirName = "";
				Entry entry = null;

				switch(tokens[0].toLowerCase()) {
					case "quit":
						return;
					case "info":
						System.out.println(info.toString());
						break;
					case "cd":
						//check for valid number of arguments
						if (tokens.length == 1) {
							System.out.println("Invalid syntax: You must specify a directory");
							break;

						}
						if (tokens.length > 2) {
							System.out.println("Invalid syntax. Proper usage: cd <DIR_NAME>");
							break;
						}

						dirName = tokens[1].toUpperCase();
						entry = dirEntries.get(dirName);

						//check for valid directory
						if (entry == null) {
							System.out.println("Error: does not exist");
							break;
						}

						if (!entry.DIR_ATTR.equals("ATTR_DIRECTORY")) {
							System.out.println("Error: not a directory");
							break;
						}
						//this block takes care of an error that for some reason the .. entry for DIR 
						//	doesn't take you back to the root...
						if (dirName.equals("..") && currentPath.size() == 1) {
							loadRoot();
						}

						//establish this directory as the new current working directory
						loadDir(entry);
						break;
					case "ls":
						//check number of arguments
						if (tokens.length == 1) {
							System.out.println("Invalid syntax: You must specify a directory");
							break;
						}
						if (tokens.length > 2) {
							System.out.println("Invalid syntax. Proper usage: ls <DIR_NAME>");
							break;
						}

						fileName = tokens[1].toUpperCase();

						//check for valid directory
						if (!dirEntries.containsKey(fileName) && !fileName.equals(".")) {
							System.out.println("Error: does not exist"); 
							break;
						}
						if (fileName.contains(".") && !fileName.equals(".") && !fileName.equals("..")) {
							System.out.println("Error: not a directory"); 
							break;
						}

						/*
						 *	Here's the actual logic.
						 * The reason for the ternary operator is that the root directory does not have an
						 * entry for ".", so to cover this case we have to treat the "." case separately
						 */
						//get all of the entries in requirested directory
						TreeMap<String, Entry> map = fileName.equals(".") ? dirEntries : buildEntryMap(dirEntries.get(fileName).nextCluster);
						//this handles the case of DIR where for some reason .. does not point back to the root.
						if (fileName.equals("..") && currentPath.size() == 1) map = buildEntryMap(2);

						//print all of the relevant entry names
						for (Entry e : map.values()) if (!e.DIR_ATTR.equals("ATTR_HIDDEN")) System.out.print(e.DIR_Name + " ");
						System.out.println();
						break;
					case "stat":
						//check number of arguments
						if(tokens.length == 1) {
							System.out.println("Invalid syntax: You must specify a file");
							break;
						}
						if (tokens.length > 2) {
							System.out.println("Invalid syntax. Proper usage: stat <FILE_NAME>");
							break;
						}

						fileName = tokens[1].toUpperCase();

						entry = dirEntries.get(fileName);

						//check to make sure that file exists
						if (entry == null) {
							System.out.println("Error: file/directory does not exist");
							break;
						}

						//print the information
						System.out.println("Size is " + entry.DIR_FileSize + "\n"
											+ "Attributes " + entry.DIR_ATTR +"\n"
											+ "Next cluster number is 0x" + Integer.toHexString(entry.nextCluster));
						break;
					case "size":
						//check number of arguments
						if(tokens.length == 1) {
							System.out.println("Invalid syntax: You must specify a file");
							break;
						}
						if (tokens.length > 2) {
							System.out.println("Invalid syntax. Proper usage: size <FILE_NAME>");
							break;
						}

						fileName = tokens[1].toUpperCase();
						entry = dirEntries.get(fileName);

						//check to make sure that file exists
						if (entry == null) {
							System.out.println("Error: file/directory does not exist");
							break;
						}

						System.out.println("size = " + entry.DIR_FileSize);
						break;
					case "volume":
						// the "volume" static field contains either the name of the volume or the error message
						//this information was initialized in the "loadRoot" method.
						System.out.println(volume);
						break;
					case "read":
						//check number of arguments
						if (tokens.length != 4) {
							System.out.println("Invalid syntax: Proper usage: read FILE_NAME POSITION NUM_BYTES");
							break;
						}
						entry = dirEntries.get(tokens[1].toUpperCase());

						//check to make sure that file exists
						if (entry == null) {
							System.out.println("Error: file/directory does not exist");
							break;
						}

						//check that POSITION and NUM_BYTES are valid integers, then execute
						try {
							long position = Long.parseLong(tokens[2]);
							long num_bytes = Long.parseLong(tokens[3]);

							//check valid position
							if(position + num_bytes > entry.DIR_FileSize) {
								System.out.println("Error: attempt to read beyond end of file");
								break;
							}
							
							read(entry, position, num_bytes);
						} catch(NumberFormatException e) {
							System.out.println("Error: POSITION and NUM_BYTES must be valid decimal integers.");
						}
						break;
					case "freelist":
						System.out.print("First three free clusters: ");
						Iterator<Integer> it = freelist.iterator();
						for (int i = 0; i < 3; i++) {
							if (it.hasNext()) System.out.print(it.next() + ", ");
							else System.out.print("N/A");
						}
						System.out.println();

						System.out.println("Total number of free clusters: " + freelist.size());
						break;

					case "newfile":
						//check number of arguments
						if (tokens.length != 3) {
							System.out.println("Invalid syntax: Proper usage: newfile <FILE_NAME> <SIZE>");
							break;
						}
						fileName = tokens[1].toUpperCase();
						String[] nametokens = fileName.split("\\.");
						if (nametokens.length < 2) {
							System.out.println("Invalid file name: must have a file extension");
							break;
						}
						if (nametokens.length > 2) {
							System.out.println("Invalid file name: must only contain one period, in between the file name and extension");
							break;
						}
						if (nametokens[0].length() == 0) {
							System.out.println("Invalid file name: file name must be at least one character");
							break;
						}
						if (nametokens[0].length() > 8) {
							System.out.println("Invalid file name: the length of the file name must be at most 8 characters, excluding extension");
							break;
						}
						if (nametokens[1].length() == 0) {
							System.out.println("Invalid file name: the file extension must be at least one character long");
							break;
						}
						if (nametokens[1].length() > 3) {
							System.out.println("Invalid file name: the length of the extension (not including period) must be at most 3 characters");
							break;
						}
						if (dirEntries.containsKey(fileName)) {
							System.out.println("File already exists.");
							break;
						}
						try {
							int size = Integer.parseInt(tokens[2]);
							if (size < 0) {
								System.out.println("File size may not be negative");
								break;
							}
							createFile(fileName, size);
						} catch(NumberFormatException e) {
							System.out.println("<SIZE> must be a valid, decimal integer");
						}
						break;
					case "delete":
						//check number of arguments
						if (tokens.length != 2) {
							System.out.println("Invalid syntax: Proper usage: delete <FILE_NAME>");
							break;
						}
						fileName = tokens[1].toUpperCase();
						entry = dirEntries.get(fileName);

						//check to make sure that file exists
						if (!dirEntries.containsKey(fileName) || fileName.equals(".") || fileName.equals("..")) {
							System.out.println("Error: file does not exist");
							break;
						}
						if(entry.DIR_ATTR.equals("ATTR_VOLUME_ID") || entry.DIR_ATTR.equals("ATTR_LONG_NAME")) {
							System.out.println("Error: file does not exist");
							break;
						}
						if(entry.DIR_ATTR.equals("ATTR_DIRECTORY")) {
							System.out.println("Error: you may not delete a direcotry.");
							break;
						}
						delete(fileName);
						break;

					/* 
					 * The rest of these commands are helper commands used when figuring out how fat works
					 */

					//print certain number of bytes of specified cluster number in the fat region
					case "fat":
						if (tokens.length == 1) {
							System.out.println("Please specify cluster number.");
							break;
						}
						offset = info.getFatOffset(Integer.parseInt(tokens[1]));
						System.out.println("Offset = " + offset);
						display(fat, offset, tokens.length == 2 ? 100 : Integer.parseInt(tokens[2]));
						break;

					//print certain number of bytes of specified cluster number in the data region
					case "data":
						if (tokens.length == 1) {
							System.out.println("Please specify cluster number.");
							break;
						}
						offset = info.getDataOffset(Integer.parseInt(tokens[1]));
						System.out.println("Offset = " + offset);
						display(fat, offset, tokens.length == 2 ? 100 : Integer.parseInt(tokens[2]));
						break;

					//print certain number of bytes at said byte offset from the beginning of the volume
					case "display":
						switch (tokens.length) {
							case 1: display(fat, 0, 100);
								break;
							case 2: display(fat, Long.parseLong(tokens[1]), 100);
								break;
							default: display(fat, Long.parseLong(tokens[1]), Integer.parseInt(tokens[2]));
						}
						break;
					case "clusters":
						if (tokens.length != 2) {
							System.out.println("Proper usage: clusters <FILE_NAME>");
							break;
						}
						fileName = tokens[1].toUpperCase();
						entry = dirEntries.get(fileName);
						if (entry == null) {
							System.out.println("File does not exist");
							break;
						}
						int firstCluster = entry.nextCluster;
						LinkedList<Integer> clusters = buildClusterChain(firstCluster);
						System.out.print("Clusters (" + clusters.size() + "): ");
						for (int cluster : clusters) {
							System.out.print(cluster + ", ");
						}
						System.out.println();
					break;
					case "text":
						if (tokens.length != 2) {
							System.out.println("Error: proper usage: text <CLUSTER_NUMBER>");
							break;
						}
						try {
							int clusterNumber = Integer.parseInt(tokens[1]);
							if (clusterNumber < 0) {
								System.out.println("Cluster number must be positive");
								break;
							}
							showText(clusterNumber);
						} catch (NumberFormatException e) {
							System.out.println("Cluster number must be a valid positive integer.");
							break;
						}


					//For all other, undefined commands
					default:
						System.out.println("Command not recognized.");
				}
			}
		} catch(FileNotFoundException e) {
			System.err.println("The file does not exist, is a directory rather than a regular file, or for some other reason cannot be opened for reading.");
			e.printStackTrace();
		} catch(Exception e) {
			System.err.println("Error: RandomAccessFile could not be closed.");
			e.printStackTrace();
		}
	}

	/*
	 * Reads specific information from the BPB data structure and stores it in an Info object in the "info" static field
	 */
	private static void readBPBinfo() throws IOException {
		info = new Info();
		byte[] oneByteBuffer = new byte[1];
		byte[] twoByteBuffer = new byte[2];
		byte[] fourByteBuffer = new byte[4];

		fat.seek(11);
		fat.read(twoByteBuffer); info.BPB_BytesPerSec = bytesToInt(twoByteBuffer);
		fat.read(oneByteBuffer); info.BPB_SecPerClus = bytesToInt(oneByteBuffer);
		fat.read(twoByteBuffer); info.BPB_RsvdSecCnt = bytesToInt(twoByteBuffer);
		fat.read(oneByteBuffer); info.BPB_NumFATS = bytesToInt(oneByteBuffer);
		fat.seek(36);
		fat.read(fourByteBuffer); info.BPB_FATSz32 = bytesToInt(fourByteBuffer);
		fat.seek(44);
		fat.read(fourByteBuffer); info.BPB_RootClus = bytesToInt(fourByteBuffer);
	}
	/*
	 * convert little-endian byte array into an int
	 */
	public static int bytesToInt(byte[] bytes) {
		int sum = 0;
		for (int i = 0; i < bytes.length; i++) {
			sum += Byte.toUnsignedInt(bytes[i]) * Math.pow(256, i);
		}
		return sum;
	}

	/*
	 * Print certain number of bytes at given offset from beginning of volume.
	 * Takes the fat as a parameter from a previous design where fat was not a field. 
	 * Since we no longer need or use this we are not bothering to change this.
	 */
	private static void display(RandomAccessFile fat, long offset, int amount) throws IOException {
		long pos = fat.getFilePointer();
		fat.seek(offset);

		byte[] buffer = new byte[amount];
		fat.read(buffer);
		System.out.println(byteArrayToString(buffer));

		fat.seek(pos);
	}

	/*
	 * Converts byte into a string of hex representations of each byte. To be printed, for the display method.
	 */
	private static String byteArrayToString(byte[] array) {
		String returnString = "";
		int counter = 0;
		for (byte b : array) {
			returnString += String.format("%02X", b) + " ";
			counter = (counter + 1) % 16;
			if (counter == 0) returnString += "\n";
		}
		return returnString;
	}

	/*
	 * Given the cluster number of the first cluster of a file, return a list containing the cluster numbers of 
	 * all clusters (in order) making up the file
	 */
	private static LinkedList<Integer> buildClusterChain(int firstCluster) throws IOException {
		byte[] fourByteBuffer = new byte[4];
		long fatOffset = info.getFatOffset(firstCluster);

		LinkedList<Integer> chain = new LinkedList<Integer>();
		chain.add(firstCluster);

		boolean finished = false;
		while(!finished) {
			fat.seek(fatOffset);
			fat.read(fourByteBuffer);
			int value = bytesToInt(fourByteBuffer) & 0x0FFFFFFF;
			if (value >= 0x00000002 && value <= 0x0FFFFFEF) {
				chain.add(value);
				fatOffset = info.getFatOffset(value);
			} else {
				finished = true;
			}
		}

		return chain;
	}

	/*
	 * Change current working directory to an immediate subdirectory (or immediate parent) of current working directory
	 */
	private static void loadDir(Entry entry) throws IOException {
		//change current directory information
		switch (entry.DIR_Name) {
			case "..":
				if(currentDirectory.equals("/"))
					return;
				currentPath.removeLast();
				break;
			case ".":
				break;
			default:
				currentPath.add(entry.DIR_Name);
		}
		currentDirectory = currentpathToString();	

		//load dir entries
		dirEntries = buildEntryMap(entry.nextCluster);
	}

	/*
	 * Helper method to construt prompt-string
	 */
	private static String currentpathToString() {
		String returnString = "/";
		for (String dir : currentPath) returnString += dir + "/";
		return returnString;
	}

	/*
	 * Initialize current working directory as root. 
	 */
	private static void loadRoot() throws IOException {
		//load root dir entries
		dirEntries = buildEntryMap(info.BPB_RootClus);

		//initialize path/directory name
		currentPath = new LinkedList<String>();
		currentDirectory = "/";
	}

	/*
	 * Returns a map of (String)name to (Entry)fatDirectoryEntry for directory whose first cluster is provided in the parameter
	 */
	private static TreeMap<String, Entry> buildEntryMap(int clusterNumber) throws IOException {
		//get list of all clusters belonging to this directory
		LinkedList<Integer> clusterChain = buildClusterChain(clusterNumber);
		//create map object to hold entries
		TreeMap<String, Entry> returnMap = new TreeMap<String, Entry>();

		/*
		 * Parse through the entries in each cluster.
		 * numEntries is the number of entries per cluster.
		 */
		int numEntries = (info.BPB_BytesPerSec * info.BPB_SecPerClus) / 32;
		for (int cluster : clusterChain) {
			fat.seek(info.getDataOffset(cluster));

			for(int i = 0; i < numEntries; i++) {
				byte[] directoryEntry = new byte[32];
				fat.read(directoryEntry);

				if (directoryEntry[0] == (byte)0x00) break; //entry is empty and no more entries after this one
				if (directoryEntry[0] == (byte)0xE5) continue; //entry is empty but there may be more entries after this one

				Entry newEntry = new Entry(directoryEntry);
				if (newEntry.DIR_ATTR.equals("ATTR_VOLUME_ID")) volume = newEntry.DIR_Name;
				if (newEntry.DIR_ATTR.equals("ATTR_LONG_NAME") || newEntry.DIR_ATTR.equals("ATTR_VOLUME_ID")) continue;

				returnMap.put(newEntry.DIR_Name, newEntry);
			}
		}

		return returnMap;
	}

	/*
	 * Prints to console 'num_bytes' bytes from file 'entry' starting at offset 'position'
	 */
	private static void read(Entry entry, long position, long num_bytes) throws IOException {
		//get list of all clusters belonging to this file
		LinkedList<Integer> clusterChain = buildClusterChain(entry.nextCluster);

		//we need to know the amount of bytes in a cluster to make calculations
		int bytesPerCluster = info.getNumbBytesPerCluster();

		//i.e. 1st cluster, 2nd cluster, etc. These will be converted to actual cluster numbers later
		int serialClusterNumber = (int)(position / bytesPerCluster);

		//offset to start reading first cluster that will be read. This will only be non-zero for first cluster.
		// once we're done reading the first cluster we will set this to zero.
		int offset = (int)(position % bytesPerCluster);

		/*
		 * make a list of the amount of bytes to read from each (serial) cluster
		 */
		LinkedList<Integer> btyesToReadFromCluster = new LinkedList<Integer>();

		//calculate amount to read from first cluster
		if (offset + num_bytes > bytesPerCluster) {
			btyesToReadFromCluster.add(bytesPerCluster - offset);
			//update num_bytes variable accordingly. We will use this to keep track of how many bytes are left to be read.
			num_bytes -= (bytesPerCluster - offset);
		} else {
			btyesToReadFromCluster.add((int)num_bytes);
			num_bytes = 0;
		}

		//calculate the amount to be read from the rest of the clusters
		while(num_bytes > 0) {
			if (num_bytes > bytesPerCluster) {
				btyesToReadFromCluster.add(bytesPerCluster);
			} else {
				btyesToReadFromCluster.add((int)num_bytes);
			}
			//note that this subtraction could make num_bytes negative. This doesn't matter for our purposes
			num_bytes -= bytesPerCluster;
		}

		/*
		 * Read the required amount from each cluster, and print the text to the console.
		 */
		for (int i : btyesToReadFromCluster) {
			byte[] buffer = new byte[i];
			int actualClusterNumber = clusterChain.get(serialClusterNumber++);
			fat.seek(info.getDataOffset(actualClusterNumber) + offset);

			//therefore offset will be zero for all except (possibly) the first cluster
			offset = 0;

			fat.read(buffer);
			System.out.print(new String(buffer));
		}
		System.out.println();
	}

	/*
	 * Read the free list in the FAT data structure into a static LinkedList field.
	 */
	private static void readFreeList() throws IOException {
		freelist = new LinkedList<Integer>();
		byte[] fourByteBuffer = new byte[4];

		fat.seek(info.getOffsetOfStartOfFatRegion());
		int clusterNumber = 0;
		long totalFatEntries = (info.BPB_FATSz32 * info.BPB_BytesPerSec) / 32;
		for (long i = 0; i < totalFatEntries; i++) {
			fat.read(fourByteBuffer);
			int value = bytesToInt(fourByteBuffer) & 0x0FFFFFFF;
			if (value == 0) freelist.add(clusterNumber);
			clusterNumber++;
		}
	}

	/*
	 * Deletes the file
	 */
	private static void delete(String fileName) throws IOException {
		//get cluster number of current working directory
		int clusterNumber = getCurrentDirectoryClusterNumber();
		//get list of all clusters belonging to this directory
		LinkedList<Integer> clusterChain = buildClusterChain(clusterNumber);

		/*
		 * Parse through the entries in each cluster.
		 * numEntries is the number of entries per cluster.
		 * The goal here is to find the entry that corresponds to the file that we want to delete
		 */
		int numEntries = (info.BPB_BytesPerSec * info.BPB_SecPerClus) / 32;
		outer:
		for (int cluster : clusterChain) {
			fat.seek(info.getDataOffset(cluster));

			for(int i = 0; i < numEntries; i++) {
				byte[] directoryEntry = new byte[32];
				fat.read(directoryEntry);

				Entry entry = new Entry(directoryEntry);

				//when we find the file
				if (entry.DIR_Name.equals(fileName)) {
					//free it on the directory entry
					fat.seek(fat.getFilePointer() - 32);
					byte[] b = new byte[] {(byte)0xE5};
					fat.write(b);

					fat.seek(fat.getFilePointer() - 1);
					fat.read(directoryEntry);
					entry = new Entry(directoryEntry);

					//free it on the freelist
					freeClusters(entry);

					break outer;
				}
			}
		}
		reloadCurrentDirectory();
	}

	private static void reloadCurrentDirectory() throws IOException {
		if (dirEntries.containsKey(".")) loadDir(dirEntries.get("."));
		else loadRoot();	
	}

	/*
	 * Get the cluster number of the current working directory
	 */
	private static int getCurrentDirectoryClusterNumber() {
		//every directory should contain a "." entry for the current directory
		if (dirEntries.containsKey(".")) {
			return dirEntries.get(".").nextCluster;
		}
		//except for the root, whose cluster number is 2
		return 2;
	}

	/*
	 * Adds the clusters currently being occupied by this file to the freelist
	 */
	private static void freeClusters(Entry entry) throws IOException {
		if (entry.nextCluster == 0) {
			return;
		}
		LinkedList<Integer> clusterChain = buildClusterChain(entry.nextCluster);
		//System.out.println("Freeing " + clusterChain.size() + " clusters:");
		byte[] fourByteBuffer = new byte[4];
		for(int cluster : clusterChain) {
			for (int fatNumber = 0; fatNumber < 2; fatNumber++) {
				//The second term in the sum here is taking into account the offsets of which fat it is
				fat.seek(info.getFatOffset(cluster) + (fatNumber * info.BPB_FATSz32 * info.BPB_BytesPerSec));
				fat.read(fourByteBuffer);
				fat.seek(fat.getFilePointer() - 4);
				//replace the current entry with 0, maingaining the reserved bits
				fourByteBuffer = new byte[] {0x00, 0x00, 0x00, (byte)((int)fourByteBuffer[3] & (int)0xF0)};
				fat.write(fourByteBuffer);
			}
			freelist.add(cluster);
		}
		Collections.sort(freelist);
	}

	/*
	 * Create file named "fileName" of size 'size'.
	 * 
	 * Allocate its clusters and update the fat
	 * 
	 * Fill the file with the string "New File.\r\n" repeated 
	 * 
	 * Create the directory entry for it
	 */
	private static void createFile(String fileName, int size) throws IOException {
		if(size == 0) {
			createDirectoryEntry(fileName, size, 0);
			return;
		}

		//allocate the clusters for this file.
		int firstCluster = allocateClusters(size);

		//get the cluster list for this file
		LinkedList<Integer> clusters = buildClusterChain(firstCluster);

		//compute the number of bytes to write to the last cluster (every previous cluster will be filled entirely)
		int numberOfBytesToWriteToLastCluster = size % (info.getNumbBytesPerCluster());

		/*
		 * This class is responsible for filling up the buffers with the bytes to be written to the new file.
		 */
		class Letters {
			byte[] characters;
			int index;

			Letters() {
				characters = "New File.\r\n".getBytes();
				index = 0;
			}

			void fill(byte[] buffer) {
				for (int i = 0; i < buffer.length; i++) {
					buffer[i] = characters[index];
					index++;
					index = index % characters.length;
				}
			}
		}

		byte[] buffer = new byte[info.getNumbBytesPerCluster()];
		Letters letters = new Letters();

		while(clusters.size() > 0) {
			//get the cluster number and seek to it
			int cluster = clusters.removeFirst();
			fat.seek(info.getDataOffset(cluster));

			//fille the buffer with the bytes to be written to the cluster
			if (clusters.size() == 0) buffer = new byte[numberOfBytesToWriteToLastCluster];
			letters.fill(buffer);

			//write
			fat.write(buffer);
		}

		//create a directory entry for this new file
		createDirectoryEntry(fileName, size, firstCluster);
	}

	/*
	 * Allocate the clusters needed for this new file.
	 * Update the free list by removing those clusters
	 * Update the fat data structure with the information for the new file.
	 */
	private static int allocateClusters(int size) throws IOException {
		//compute the number of clusters needed for this file
		int numClusters = size / (info.getNumbBytesPerCluster());
		if ((size % info.getNumbBytesPerCluster()) != 0) numClusters++;

		//this variable is just to save the first cluster number in order to return it.
		//  Hence it is immediately stored in "clusterNumber", which is used for iteration.
		int firstCluster = freelist.removeFirst();

		int clusterNumber = firstCluster;

		numClusters--;
		while (numClusters >= 0) {
			int nextCluster = (numClusters == 0) ? 0x0FFFFFFF : freelist.removeFirst();
			writeNextClusterNumberToFat(clusterNumber, nextCluster);
			clusterNumber = nextCluster;
			numClusters--;
		}

		return firstCluster;
	}

	private static void showText(int clusterNumber) throws IOException {
		fat.seek(info.getDataOffset(clusterNumber));
		byte[] buffer = new byte[512];
		fat.read(buffer);
		System.out.println(new String(buffer));
	}


	private static void createDirectoryEntry(String fileName, int size, int firstCluster) throws IOException {
		int clusterNumber = 0;
		if (dirEntries.containsKey(".")) {
			clusterNumber = dirEntries.get(".").nextCluster;
		} else {
			clusterNumber = 2;
		}

		LinkedList<Integer> clusters = buildClusterChain(clusterNumber);
		byte[] firstByte = new byte[1];
		for (int cluster : clusters) {
			fat.seek(info.getDataOffset(cluster));
			for (int i = 32; i < info.getNumbBytesPerCluster(); i += 32) {
				fat.read(firstByte);
				if (firstByte[0] == (byte)0x00 || firstByte[0] == (byte)0xE5) {
					fat.seek(fat.getFilePointer() - 1);
					fat.write(constructNewDirectoryEntry(fileName, size, firstCluster));
					reloadCurrentDirectory();
					return;
				} else {
					fat.skipBytes(31);
				}
			}
		}

		//if we reach this point then all of the clusters for this directory are currently filled to the brim with entries
		//we now have to add another cluster
		int lastCluster = clusters.getLast();
		int newCluster = addNewCluster(lastCluster);
		fat.seek(info.getDataOffset(newCluster));
		fat.write(constructNewDirectoryEntry(fileName, size, firstCluster));

		reloadCurrentDirectory();
	}

	private static int addNewCluster(int previousCluster) throws IOException {
		int newCluster = freelist.removeFirst();
		writeNextClusterNumberToFat(previousCluster, newCluster);
		writeNextClusterNumberToFat(newCluster, 0x0FFFFFFF);
		return newCluster;
	}

	/*
	 * This is used to write the next cluster in the entries in the fat data strcute
	 * To create a new file (cluster chain) one would take a free cluster and write EOC (0x?FFFFFFF) if it is the only
	 * 	cluster, or would write the number of another free cluster, and then set that second one to EOC
	 * To append to a previous cluster chain, simply overwrite the EOC value of the last cluster with the number of the
	 * 	new cluster, and write EOC to the new cluster
	 *
	 * This writes to both fats
	 */
	private static void writeNextClusterNumberToFat(int previousCluster, int nextCluster) throws IOException {
		//do this for both fats
		for (int fatNumber = 0; fatNumber < 2; fatNumber++) {
			//turn the next cluster number into its byte representation
			byte[] bytes = intToBytes(nextCluster);

			//a lot of this complicated stuff is dealing with preserving the reserved four bits
			byte[] maskedByte = new byte[1];
			fat.seek(info.getFatOffset(previousCluster) + 3 + (fatNumber * info.BPB_FATSz32 * info.BPB_BytesPerSec));
			fat.read(maskedByte);
			maskedByte[0] = (byte)((int)maskedByte[0] & 0xF0);
			bytes[3] = (byte)((int)bytes[3] & 0x0F);
			bytes[3] = (byte)((int)bytes[3] | maskedByte[0]);

			//now write the next cluster number
			fat.seek(fat.getFilePointer() - 4);
			fat.write(bytes);
		}
	}

	/*
	 *
	 */
	private static byte[] constructNewDirectoryEntry(String fileName, int size, int firstCluster) {
		byte[] entry = new byte[32];

		//parse the filename into the first 11 bytes (0-10) in the proper format
		String[] tokens = fileName.split("\\.");
		byte[] nameBytes = tokens[0].getBytes();
		byte[] extBytes = tokens[1].getBytes();
		for (int i = 0; i < nameBytes.length; i++) {
			entry[i] = nameBytes[i];
		}
		for (int i = nameBytes.length; i < 8; i++) {
			entry[i] = (byte)0x20;
		}
		for (int i = 11 - extBytes.length; i < 11; i++) {
			entry[i] = extBytes[i - 8];
		}

		//set attr to ATTR_ARCHIVE
		entry[11] = (byte)0x20;
		//WINDOWSNT
		entry[12] = (byte)0x00;
		//NEED TO FIX THIS
		for (int i = 13; i < 20; i++) entry[i] = (byte)0x00;
		//the high bytes of the cluster number
		byte[] clusterBytes = intToBytes(firstCluster);
		entry[20] = clusterBytes[2]; 
		entry[21] = clusterBytes[3];
		//need to fix this
		for (int i = 22; i < 26; i++) entry[i] = (byte)0x00;
		entry[26] = clusterBytes[0];
		entry[27] = clusterBytes[1];
		//store the size
		byte[] sizeBytes = intToBytes(size);
		for (int i = 0; i < 4; i++) entry[28 + i] = sizeBytes[i];

		return entry;
	} 

	private static byte[] intToBytes(int number) {
		//got this method from here: https://stackoverflow.com/questions/1936857/convert-integer-into-byte-array-java
		ByteBuffer bbuf = ByteBuffer.allocate(4);
		bbuf.order(ByteOrder.LITTLE_ENDIAN);
		bbuf.putInt(number);
		return bbuf.array();
	}
}
