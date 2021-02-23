import java.util.zip.*;
import java.lang.StringBuilder;
import java.io.*;
import java.nio.*;
import java.util.ArrayList;
import java.util.jar.*;

//save to temp file
//crc in one shot / maybe check
public class CompressionUtility
{
	private static ZipOutputStream zout;
	private static JarOutputStream jout;
	private static String report;
	private static String type;
	private static File reportFile;
	private static ArrayList<String> pathList;
	private static CRC32 crc;
	private static File tempFile;
	private static File finalFile;
	private static String filePath;

	public static void main(String[] args)
	{
		CompressionUtility.zout = null;
		CompressionUtility.jout = null;
		CompressionUtility.report = null;
		CompressionUtility.type = null;
		CompressionUtility.reportFile = null;
		CompressionUtility.pathList = null;
		CompressionUtility.crc = null;
		CompressionUtility.tempFile = null;

		report = args[2];
		crc = new CRC32();
		pathList = new ArrayList<String>();

		CompressionUtility.filePath = args[0];
		File file = new File(filePath);

		type = args[1];
		if (!type.equals("jar") && !type.equals("zip")) {
			System.out.println("Error: invalid type. Please select from the following file types: zip, jar");
			return;
		}

		//naming and creating the temp zip/jar file
		String newFilePath = filePath + "\\" + "out";

		try {
			if (type.equals("zip")) {
				tempFile = File.createTempFile(newFilePath, ".zip");
				finalFile = new File(newFilePath + ".zip");
			}
			else if (type.equals("jar")) {
				tempFile = File.createTempFile(newFilePath, ".jar");
				finalFile = new File(newFilePath + ".jar");
			}
		} catch (IOException e) {
			System.err.println("Caught IOException while creating zip/jar file: " + e.getMessage());
		}

		//write the zip file
		try {
			if (type.equals("zip")) {
				zout = new ZipOutputStream(new FileOutputStream(tempFile));
			}
			else if (type.equals("jar")) {
				jout = new JarOutputStream(new FileOutputStream(tempFile));
			}
			compress(file, "", type);
			closeOutputStream();
		} catch (IOException e) {
			System.err.println ("Caught IOException while creating FileOutputStream: " + e.getMessage());
		}

		copyFile();

		CreateCRCFile();

		//create report file
		reportFile = new File(filePath + "\\report.txt");
		try {
			reportFile.createNewFile();
		} catch(IOException e) {
			System.err.println("Caught IOException while creating report file: " + e.getMessage());
		}
		report();
	}

	private static void compress(File file, String directoryName, String type)
	{
		try{
			if (file.isDirectory()) {
				directoryName += (file.getName() + "\\");

				File[] contentList = file.listFiles();
				for (File f : contentList) {
					compress(f.getAbsoluteFile(), directoryName, type);
				}
			}
			else if (type.equals("zip")) {
				String relativePath = directoryName + file.getName();
				FileInputStream in = new FileInputStream(file);
				zout.putNextEntry(new ZipEntry(relativePath));
				while (in.available() > 0) {
					byte[] bytes = new byte[in.available()];
					in.read(bytes, 0, bytes.length);
					zout.write(bytes, 0, bytes.length);
				}
				in.close();
				zout.closeEntry();

				//checking file type to see if we should add the path to the report
				if (file.getName().endsWith(report)) {
					pathList.add(relativePath);
				}
			}
			else if (type.equals("jar")) {
				String relativePath = directoryName + file.getName();
				FileInputStream in = new FileInputStream(file);
				jout.putNextEntry(new JarEntry(relativePath));
				while (in.available() > 0) {
					byte[] bytes = new byte[in.available()];
					in.read(bytes, 0, bytes.length);
					jout.write(bytes, 0, bytes.length);
					crc.update(bytes);
				}
				in.close();
				jout.closeEntry();

				//checking file type to see if we should add the path to the report
				if (file.getName().endsWith(report)) {
					pathList.add(relativePath);
				}
			}
		} catch (IOException e) {
			System.err.println("Caught IOException in method:compress: " + e.getMessage());
		} 
	}

	private static void closeOutputStream()
	{
		try {
			if (type.equals("zip")) {
				zout.close();
			}
			else if (type.equals("jar")) {
				jout.close();
			}
		} catch (IOException e) {
			System.err.println("Caught IOException in method:closeOutputStream: " + e.getMessage());
		}
	}

	private static void report()
	{
		try {
			FileWriter fw = new FileWriter(CompressionUtility.reportFile);
			for (int i = 0; i < pathList.size(); i++) {
				String relativePath = pathList.get(i);
				relativePath += "\n";
				fw.write(relativePath);
			}
			fw.close();
		} catch(IOException e) {
			System.err.println("Caught IOException in method:report: " + e.getMessage());
		}
	}

	private static void CreateCRCFile()
	{
		//Create the file where you will store the CRC32 value
		File crcFile = new File(CompressionUtility.filePath + "\\crc.txt");
		try {
			crcFile.createNewFile();
		} catch (IOException e) {
			System.err.println("Caught IOException while making CRC32 text file: " + e.getMessage());
		}

		//update the CRC32 object with the bytes from the completed zip file
		try {
			FileInputStream fins = new FileInputStream(CompressionUtility.finalFile);
			byte[] bytes = new byte[fins.available()];
			while (fins.available() > 0) {
				fins.read(bytes);
				crc.update(bytes);
			}
			fins.close();
		} catch (IOException e) {
			System.err.println("Caught IOException while updating CRC32 value: " + e.getMessage());
		}

		//print the CRC32 value into the CRC32 text file
		try {
			FileWriter fw = new FileWriter(crcFile);
			long value = crc.getValue();
			fw.write("" + value);
			fw.close();
		} catch (IOException e) {
			System.err.println("Caught IOException while writing CRC32 text file: " + e.getMessage());
		}
	}

	private static void copyFile()
	{
		try {
			finalFile.createNewFile();
			FileInputStream fins = new FileInputStream(tempFile);
			FileOutputStream fouts = new FileOutputStream(finalFile);

		//got the following code from: http://stackoverflow.com/questions/1946298/best-way-to-copy-a-zip-file-via-java

			byte[] buf = new byte[1024];
			int i = 0;
			while ((i = fins.read(buf)) != -1) {
		  		fouts.write(buf, 0, i);
			}
			fins.close();
			fouts.close();
		} catch (IOException e) {
			System.err.println("Caught IOException while copying compressed file: " + e.getMessage());
		}
	}
}
