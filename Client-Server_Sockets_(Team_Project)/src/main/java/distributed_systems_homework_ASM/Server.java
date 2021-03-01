package distributed_systems_homework_ASM;

import java.net.*;
import java.io.*;
import java.util.Scanner;
import java.util.HashSet;
import com.google.gson.Gson;

public class Server
{
	private distributed_systems_homework_ASM.ClassList classList;
	private boolean verbose;
	private File file;
	private Gson gson;
	private HashSet<Thread> threads;

	public Server(File file) throws IOException
	{
		this.file = file;
		this.gson = new Gson();
		this.verbose = false;
		this.threads = new HashSet<Thread>();
		this.initialize();
		this.startUp();
	}
	
	private void startUp() throws SocketException
	{
		Thread t = new Thread(() -> {
			//crate serversocket
			try(ServerSocket s = new ServerSocket(8192)) {
				s.setSoTimeout(2000);
				while(!Thread.currentThread().isInterrupted()) {
					//receive socket
					try(Socket incoming = s.accept()) {

						//get input and output streams
						InputStream is = incoming.getInputStream();
						OutputStream os = incoming.getOutputStream();

						//make scanner and printwriter
						PrintWriter pw = new PrintWriter(new OutputStreamWriter(os), true);
						try(Scanner sc = new Scanner(is)) {

							//parse through, print, and echo
							while (sc.hasNextLine()) {
								String line = sc.nextLine();
								if (line.equals("SHUTDOWN")) {
									this.shutDown();
									break;
								}
								if (verbose) System.out.println("SERVER:\n" + line);
								pw.println(this.parse(line));
							}
						}

					//catch incoming socket
					} catch (IOException e) {
						System.err.println("SERVER 1 Caught IOException: " + e.getClass() + " : " + e.getMessage());
					}
				}
			//catch creation of serversocket
			} catch (IOException e) {
				System.err.println("SERVER 2 Caught IOException: " + e.getClass() + " : " + e.getMessage());
			}
		});
		t.start();
		threads.add(t);
	}
	

	/*
	 *
	*/
	private void initialize() throws IOException
	{
		try (Scanner sc = new Scanner(file)) {
			String jsonString = sc.useDelimiter("\\Z").next();
			this.classList = gson.fromJson(jsonString, distributed_systems_homework_ASM.ClassList.class);
		}
	}

	private String parse(String requestString)
	{
		String[] tokens = requestString.split(" ");
		switch(tokens[0]) {
			case "GET": return this.classList.get(tokens[1]);
			case "ADD": return this.add(tokens);
			case "DELETE": return this.delete(tokens[1]);
			default: throw new IllegalArgumentException("Error: Client request did not begin with GET ADD DELETE or SHUTDOWN.");
		}
	}

	private String add(String[] tokens)
	{
		try {
			int crnNumber = Integer.parseInt(tokens[2]);
			String returnString = this.classList.add(tokens[1], crnNumber, tokens[3]);
			this.updateFile();
			return returnString;
		} catch (NumberFormatException e ) {
			throw new IllegalArgumentException("ERROR: CRN received by the server is not an integer.");
		}
	}

	private String delete(String crn) throws IllegalArgumentException
	{
		try {
			int crnNumber = Integer.parseInt(crn);
			String returnString = this.classList.delete(crnNumber);
			this.updateFile();
			return returnString;
		} catch (NumberFormatException e ) {
			throw new IllegalArgumentException("ERROR: CRN received by the server is not an integer.");
		}
	}

	private void updateFile()
	{
		String parent = file.getParent();
		File oldFile = new File(parent, "json" + System.currentTimeMillis());
		try {
			oldFile.createNewFile();
		} catch(IOException e) {
			System.err.println("Server Caught exception when trying to create new file to store old json information: " + e.getClass() + " : " + e.getMessage());
		}
		try {
			//transfer old information into the new timestamped file
			FileReader fr = new FileReader(file);
			FileWriter fw = new FileWriter(oldFile, true);
			char[] cbuf = new char[1000];
			int numCharsRead = fr.read(cbuf);
			while (numCharsRead != -1) {
				fw.write(cbuf);
				fw.flush();
				numCharsRead = fr.read(cbuf);
			}
			fr.close();
			fw.close();
			//write the new data to the file
			fw = new FileWriter(file);
			fw.write(gson.toJson(classList));
			fw.close();
		} catch(IOException e) {
			System.err.println("Server Caught: " + e.getClass() + " : " + e.getMessage());
		}
	}

	public void setVerbose(boolean b)
	{
		this.verbose = b;
	}

	public void shutDown() throws UnsupportedOperationException
	{
		if (this.threads.isEmpty()) throw new UnsupportedOperationException("You cannot shut down a server that has already been shut down.");
		for (Thread t : this.threads) t.interrupt();
	}
}
