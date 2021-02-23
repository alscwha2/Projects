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
 * Waits for connections from the client. Supports mutltiple connections. Runs threads (max 25) handing requests
 * 	with RequestHandlers running in the threads.
 */

public class Server
{
	// Only 25 unshipped orders at a time. Use a threadpool to enforce this, and to allow concurrency.
	private final ThreadPoolExecutor threadPool = new ThreadPoolExecutor(25, 25, 1, TimeUnit.MILLISECONDS, new SynchronousQueue<Runnable>(), new ThreadPoolExecutor.AbortPolicy());
	private final ThreadPoolExecutor manufacturePartsThreadPool = new ThreadPoolExecutor(100, 100, 1, TimeUnit.MILLISECONDS, new LinkedBlockingQueue<Runnable>(), new ThreadPoolExecutor.DiscardPolicy());
	private final DBManager db = new DBMDummyImpl();//This is a dummy Database. When using AWS database, switch to DBManagerImpl instance
	private final DBLockHandler lockHandler = new DBLockHandler();

	public static void main(String[] args) {
		Server s = new Server();
		s.listenForRequests();
	}

	public Server() {
		this.threadPool.prestartAllCoreThreads();
		this.manufacturePartsThreadPool.prestartAllCoreThreads();
	}

	/*
	 * Create a thread that listens for client requests.
	 * When a request is received, put it on the queue.
	 * If there is no room on the queue, reject the request.
	 */
	private void listenForRequests() {
		//create ServerSocket
		try (ServerSocket ssc = new ServerSocket(8189)) {
			//create Socket

			try {
				Socket incoming = ssc.accept();
				for (int sessionNum = 0; incoming != null; sessionNum++) {
						System.out.println("New Connection: Session#" + sessionNum);
						Thread connectionManager = new Thread(new ConnectionManager(incoming, sessionNum));
						connectionManager.setDaemon(true);
						connectionManager.start();
						incoming = ssc.accept();

				}
		} catch (IOException e) {
			System.err.println("Caught exception while creating socket connection to client.");
			System.err.println(e.getMessage());
			e.printStackTrace();
		}
		} catch (IOException e) {
			System.out.println("Server already running");
		}
	}
}