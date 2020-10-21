public class Master {

  private Zookeeper zk;

  private HashMap<String, Integer> KeyToWorkerId;

  private int numWorkers;
  private int upToWorker;

  private int numberOfTasksAssigned;
  private queueOfNewTasks LinkedBlockingQueue<Task>;
  private mapOfCurrentTasks LinkedBlockingQueue<Integer, String>
  private queueOfFinishedTasks LinkedBlockingQueue<Task>;

  public Master(Zookeeper zk) {
    this.zk = zk;
    this.numWorkers = zk.getChildren("//workers", false);
    this.upToWorker = 1;
    this.watchForChildren("//waitingTasks");
    this.processNewRequests();
    this.watchForChildren("//workerFinishedTasks");
    this.processFinishedTasks();
  }

  /**
   *
   * This puts a Asynchronous watcher on either //waitingTasks or //workerFinishedTasks
   *   to watch for new children. When the handler finds a new child ZNODE it parses
   *  it into a Task object, deletes the ZNODE, and puts the task object into the correct queue
   */
  private void watchForChildren(String path) {
    LinkedBlockingQueue queue = null;
    if (path.equals("//waitingTasks")) queue = this.queueOfNewTasks;
    if (path.equals("//workerFinishedTasks")) queue = this.queueOfFinishedTasks;
    //processor implements AsyncCallback.ChildrenCallback
    getChildren(path, new processor(path, queue));
  }
  /*
   *
   * This creates a thread that constatly monitors the queue of new requests
   * A new request is added to that queue when the asynccallback handler finds
   *  a new ZNODE for a new request from the client, and takes the information from
   *  that znode and parses it into a Task object and stores that into the queue
   *  of new requests
   * When it finds a new request in that queue it takes it and parses it into a ZNODE 
   *  or multiple ZNODEs if it's a computation and creates those ZNODES under //assignedTasks
   */
  private void processNewRequests() {
   new Thread(()->{
    while (true) {
      if (queueOfNewTasks.peek() != null) {

        //get the new client-task to process
        Task task = queueOfNewTasks.poll();
        //add this task to the client-task-number to task-object map
        this.mapOfCurrentTasks.put(new Integer(task.clientRequestNumber), task);

        //process it by type
        swich(task.requestType) {
          case "insert":
            //decide which worker should store the information
            int nextWorkerNumber = this.getNextWorker();
            //assign this task a task number
            Integer taskNumber = new Integer(numberOfTasksAssigned++);
            //make the znode that assigns the task to the worker
            zk.create("//assignedTasks/worker-" + nextWorkerNumber +"/task-" + taskNumber, task.toString(), WHATISANACL?, EPHEMERAL, ASYNCHCALLBACK);   
            break;  
          case "delete":
          case "retrieve":
            //assign this task a worker-task-number
            Integer taskNumber = new Integer(numberOfTasksAssigned++);
            //figure out which worker has the information that we need
            Integer workerID = this.KeyToWorkerId(task.parameters);
            //make the znode
            zk.create("//assignedTasks/worker-" + workerID +"/task-" + taskNumber, t.toString(), WHATISANACL?, EPHEMERAL, ASYNCHCALLBACK);   
          break;
          case "calculate":
            //get the list of all of the keys that we need
            String[] keyStrings = task.parameters.split(":");
            //get a set of all of the workers that we need for the given information
            HashSet<Integer> workers = new HashSet<Integer>();
            for (String key : keyStrings) {
              workers.add(KeyToWorkerId.get(key));
            }
            //create an assignment znode for each worker. pass on the entire task
            // to each worker, and they'll respond only with the information that 
            // they know, and will ignore the rest
            for (String workerID : workers) {
              //assign a task number
              Integer taskNumber = new Integer(numberOfTasksAssigned++);
              //create the assignment znode
              zk.create("//assignedTasks/worker-" + workerID +"/task-" + taskNumber, t.toString(), WHATISANACL?, EPHEMERAL, ASYNCHCALLBACK);   
              //the task object keeps track of all of the worker tasks that are
              //needed to complete the calculation
              task.workerTaskNumbers.add(taskNumber);
            }
            break;
        }
      }
    }
  }).start();

   /*
    *
    * This creates a thread that constantly monitors the queue of tasks that the workers have finished
    * if that tasks is totally finished then it creates a new ZNODE under //masterFinishedTasks
    *   to communicate back to the client that its task has been completed.
    */
   private void processFinishedTasks() {
    new Thread(()->{
      while(true) {
        if(queueOfFinishedTasks.peek() != null) {
          Task task = queueOfNewTasks.poll();
          swich(task.requestType) {
            case "insert":
            case "delete":
            case "retrieve":
            //task is done. remove from map, make new znode under //masterFinishedTasks to tell client
            zk.create("//masterFinishedTasks/task-" + task.clientRequestNumber, task.toString(), List<ACL> acl, EPHEMERAL) 
            mapOfCurrentTasks.remove(new Integer(t.clientRequestNumber()));
            break;
            case "calculate":
            //all of this is making sure that the master only passes on the result
            // to the client after all of the parts have been finished.
            Task clientTask = mapOfCurrentTasks.get(new Integer(t.clientRequestNumber));
            clientTask.workerTaskNumbers.remove(new Integer(task.WORKERTASKNUMBER));
            clientTask.response += ":" + t.response
            //once you have all of the pieces, compute them together and return
            if (clientTask.workerTaskNumbers().size() == 0) {
              String[] tokens = clientTask.response.split(":");
              for (String token : tokens) {
                Do the computation. 
                +: start with 0 and add
                *: start with 1 and multply
                -: start with the first one and subtract all subsequent ones
                /: start with first one and devide by second one, devide result by third etc.
              }
              zk.create("//masterFinishedTasks/task-" + t.clientRequestNumber, clientTask.toString(), List<ACL> acl, EPHEMERAL);
            }
            break;
          }
        }
      }
    }).start();
  }
  /*
   *
   *
   *Iterates through the workers one at a time 
   *in order to evenly spread out the amount of information that each worker stores
   */
  private void getNextWorker() {
   if (this.upToWorker == numWorkers) {
    upToWorker = 1;
    return numWorkers;
  }
    return upToWorker++;
  }

   /**
   * Main Method
   * @param String[] args: Command line arguments
   */
   public static void main(String[] args) {
   	String host = args[0];
   	String port = args[1];
   	Zookeeper zk = New Zookeeper(host + ":" + port, 1000, NEW WATCHER());

   	Master master = new Master(zk);
   }
 }