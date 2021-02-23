package distributed_systems_homework_ASM;

import java.net.*;
import java.io.*;
import java.util.Scanner;

public class Client
{
	private boolean verbose;

	public Client()
	{
		this.verbose = false;
	}
	
	private void request(String requestString)
	{
		//create socket
		try(Socket s = new Socket()) {
			s.setSoTimeout(2000);
			InetSocketAddress ina = new InetSocketAddress(InetAddress.getLocalHost(), 8192);
			s.connect(ina, 2000);

			//get input and output streams
			InputStream is = s.getInputStream();
			OutputStream os = s.getOutputStream();

			//create and write to the output stream
			PrintWriter pw = new PrintWriter(os, true);
			pw.println(requestString);

			//read the input stream
			String replyString = "";
			boolean recievedReply = false;
			try(Scanner sc = new Scanner(is).useDelimiter("\\A")){
				if (sc.hasNext()) {
					recievedReply = true;
					replyString = sc.next();
				}
				if (verbose & recievedReply) System.out.println("CLIENT:\n" + replyString);
			}
			s.close();

		//catch statement for creation of socket
		} catch(IOException e) {
			System.err.println("CLIENT: " + e.getClass() + " : " + e.getMessage());
		}
	}
	
	public void get(String code) throws IllegalArgumentException
	{
		switch(code) {
			case "COM":
			case "MAT":
			case "BIO":
			break;
			default:
			throw new IllegalArgumentException("Only \"COM\", \"MAT\", and \"BIO\" are valid inputs.");
		}
		this.request("GET " + code);
	}

	public void add(String code, int crn, String title)
	{
		switch(code) {
			case "COM":
			case "MAT":
			case "BIO":
			break;
			default:
			throw new IllegalArgumentException("Only \"COM\", \"MAT\", and \"BIO\" are valid inputs.");
		}
		this.request("ADD " + code + " " + crn + " " + title);
	}

	public void delete(int crn)
	{
		this.request("DELETE " + crn);
	}
	public void setVerbose(boolean b)
	{
		this.verbose = b;
	}
	public void shutDownServer()
	{
		this.request("SHUTDOWN");
	}
}