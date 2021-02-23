package ourTeam;

import java.net.SocketException;
import java.util.concurrent.*;

import java.io.IOException;
import java.io.EOFException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.ObjectInputStream;

import java.net.ServerSocket;
import java.net.Socket;
/*
 * This class takes a socket and manages the connection/requests of this client instance.
 * Refactoring this out into its own class allows for multiple client instances to connect to the server concurrently
 */
public class ConnectionManager implements Runnable {
	Socket socket;
	int sessionNum;
	Server parent;

	ConnectionManager(Socket socket, int sessionNum) {
		this.socket = socket;
		this.sessionNum = sessionNum;

	}

	@Override
	public void run() {
		try {
			ObjectInputStream fromClient = new ObjectInputStream(this.socket.getInputStream());
			PrintWriter toClient = new PrintWriter(new OutputStreamWriter(this.socket.getOutputStream(), "UTF-8"), true);

			toClient.println("Server: Connected, Session #" + this.sessionNum);
			boolean endCondition = true;

			try {
				Request request = (Request) fromClient.readObject();
				while (request != null) {

						System.out.println("Received request: " + request);
						if(request.getName().equals("quit"))
							break;
						try {
							threadPool.execute(new RequestHandler(request, db, manufacturePartsThreadPool, lockHandler, toClient));
						}catch (RejectedExecutionException e) {
							toClient.println("Request Rejected: 25 requests outstanding" + request.toString());
						}
						request = (Request) fromClient.readObject();

				}
			}  catch (EOFException e) {

			} catch (ClassNotFoundException e) {
				System.out.println("Caught ClassNotFoundException: " + e.getMessage());
				toClient.println("Error: Could not find class.");

			}
		} catch (SocketException e) {
			System.out.println("Session#" + sessionNum + " disconnected");
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				this.socket.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}