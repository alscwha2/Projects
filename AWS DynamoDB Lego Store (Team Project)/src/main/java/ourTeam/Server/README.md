# Server
* listens for connections from client
* creates thread running ConnectionManager to handle request
* supports maximum of 25 connections at one time
# Server.ConnectionManager
* Manages communication with client
* creates RequestHandler thread to handle client request
# RequestHandler.java
* handles request by transforming it into database accesses
# DBLockHandler
* makes database thread-safe by ensuring atomicity
# DBManager
* Interface to the Database
