The input file is in the curent directory named input.txt. Input syntax and limitations specified there.
I provided two bash files. run.sh takes arguments, arg1=host:port arg2=numWorkers arg3=inputFilePath. 
noop.sh takes no arguments and calls run.sh with default arguments.

In the end of the main method for Master and Worker a thread is created that sleeps for ten seconds and then kills them. This is for cleanup. If the ten second limitation will get in your way then you can delete it there. It didn't cause any problems for me.

Zookeeper will stay running until you turn it off.

I put a sleep command for three seconds in the bash file after the master is created.

At the end of the logging you'll see a printout of the current zookeeper znodes. That is caused by the method readZk in the Master being called in the main method. Delete that if you want to turn it off.