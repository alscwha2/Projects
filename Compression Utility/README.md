# Project Description
* Write a compression utility in Java which compresses all the contents of a directory, including all subdirectories
* Program arguments:
	* dir=the absolute path to the dir to compress
	* type=the type of file to produce. Two possibilities: jar and zip
	* report=a file extension to report instances of
* Output: in the directory that was compressed, create the following files:
	1. A file named “out.jar” or “out.zip” (depending on the “type” arg) with the compressed contents that have been compressed as jar or zip
	2. A file called “crc.txt” with the crc checksum of the complete jar/zip file
	3. A file called “report.txt” that gives the relative path inside the zip file to every compressed file that has the file extension that was passed in via the “report” argument. Each relative path should be on its own line
* These 3 files should NOT be in the zip file!
