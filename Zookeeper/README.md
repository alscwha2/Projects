To run, download Zookeeper and start the zookeeper server on your machine. Then simply run the scrip "easy_run.sh."

The input file is in the curent directory named input.txt. Input syntax and limitations specified there.
I provided two bash files. run.sh takes arguments, arg1=host:port arg2=numWorkers arg3=inputFilePath. 
easy_run.sh takes no arguments and calls run.sh with default arguments.

In the end of the main method for Master and Worker a thread is created that sleeps for ten seconds and then kills them. This is for cleanup. If the ten second limitation will get in your way then you can delete it there. It didn't cause any problems for me.

Zookeeper will stay running until you turn it off.

I put a sleep command for three seconds in the bash file after the master is created.

At the end of the logging you'll see a printout of the current zookeeper znodes. That is caused by the method readZk in the Master being called in the main method. Delete that if you want to turn it off.

# Project Description:
## Master-Worker Calculator
### Basic Description
* Build your distributed calculator design, in Java, using ZooKeeper for coordination
* For this project, we will run a single ZooKeeper server on our local machines
* The master and each worker will each run in separate Java Virtual Machines
* You can use https://github.com/fpj/zookeeper-book-example as a starting point

### Runtime Environment
* Your project must run on a UNIX variant
* If you have a Mac, that means running from the terminal
* If you have Windows, you will need to do the following:
	1. Install https://www.virtualbox.org/
	2. Create a Ubuntu Linux virtual machine (see, for example, https://linus.nci.nih.gov/bdge/installUbuntu.html)

### Maven Build. Run via a Bash script
* Your project must be built using Maven
* You must provide a single Bash shell script to run the master, workers, and client
* The script should take the following command line arguments:
	* port number to start the ZooKeeper server on
	* port number to start the master on
	* the number of workers to start 
	* path an input file
* Once the ZooKeeper server, workers, and master are all started, the script should run the client
* The client should not be interactive. It should
	1. Load a set of ID-value pairs, and calculation commands, from the input file (calculation commands use IDs, not values)
	2. Run the calculations
	3. Output to the console the calculation command (values, not IDs) as well as the answer/solution calculated by the system

## Logging and Comments
* You must log:
	* Every time the master assigns a key-value pair to a worker to store
	* Every time the master receives a task from the client
	* Every action taken by a worker, e.g. storing data, receiving a task assignment, doing a sub-calculation, and returning values to the master
* Log messages from a worker must state explicitly which worker created the message
* In the example github repo, look for “private static final Logger LOG...” in the code to see how to create a logger for a class.
* You must include a comment above every line of code that uses any part of the ZooKeeper API.
	* Explain what the line of code does
	* Explain what it uses ZooKeeper for
	* This includes code you use from the above github repo

### What You Will Learn
* Building a master-worker system
* Building and debugging a system running in multiple processes (i.e. a distributed system!)
* Using an existing piece of software you’ve never used before and build a solution on top of it
* Using someone else’s source code and change or extend it (the github code I pointed to)
* Get comfortable using some UNIX variant
* If you have anything other than a Mac, installing Linux
* Bash shell scripting
