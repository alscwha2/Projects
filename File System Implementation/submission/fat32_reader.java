import java.io.File;
import java.io.RandomAccessFile;
import java.io.FileNotFoundException;
import java.io.IOException;

import java.util.Scanner;
import java.util.LinkedList;
import java.util.TreeMap;
import java.util.Arrays;
import java.util.Iterator;

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


		/*
		 * Gives the offset (in bytes) of the beginning of the fat region, relative to the first byte of the reserved region
		 */
		public long getFatOffset(int clusterNumber) {
			long fatEntrySector = BPB_RsvdSecCnt + ((long)(clusterNumber * 4) / BPB_BytesPerSec);
			long fatEntryOffset = (long)(clusterNumber * 4) % BPB_BytesPerSec;
			return fatEntrySector * BPB_BytesPerSec + fatEntryOffset;
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

		//validate number of arguments
		if (args.length != 1) {
			System.err.println("The only parameter expected is the name of the FAT32 image.");
			return;
		}

		//open the .img file as a RandomAccessFile
		try (RandomAccessFile raf = new RandomAccessFile(args[0], "r")) {
			//fat is a static field. Storing the file in a field makes it easier for all of the methods to have access
			// to it. I assigned it to raf first to keep the compiler happy.
			fat = raf;

			//reads the important info from the BPB and stores it in an Info object in the "info" static field
			readBPBinfo();

			//establish root as current working directory, load fat entry information into "dirEntries" field 
			loadRoot();

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

						//print all of the relevant entry names
						for (Entry e : map.values()) {
							if (e.DIR_ATTR.equals("ATTR_LONG_NAME")) 
								continue;
							System.out.print(e.DIR_Name + " ");
						}
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

		//load volume information
		volume = null;
		for (Entry e : dirEntries.values()) {
			if (e.DIR_ATTR.equals("ATTR_VOLUME_ID")) {
				volume = e.DIR_Name;
				break;
			}
		}
		if (volume == null) volume = "Error: volume not found.";
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
				returnMap.put(newEntry.DIR_Name, newEntry);
			}
		}

		return returnMap;

	}
}