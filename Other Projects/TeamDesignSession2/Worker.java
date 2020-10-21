public class Worker{

	Zookeeper zk;
	private int workerId;
	private TreeMap<String, BigDecimal> tmap;
  private LinkedBlockingQueue<Task> tasks;

	public Worker(Zookeeper zk, int workerId) {
		  this.zk = zk;
      this.workerId = workerId;
      this.tmap = new TreeMap<String, BigDecimal>();
      this.watchForChildren("//assignedTasks/worker-" + workerId);
   }

   /*
    *
    * Sets up an Asynccallback so that when a new ZNODE is created to assign a task
    * to this worker it parses the znode into a Task object and stores it in the 
    * tasks queue and deletes the Znode
    */
   private void watchForChildren(String path) {
     getChildren(path, new processor(this, this.getClass(), path, this.tasks));
   }

   /*
    *
    *creates a thread to monitor the queue. Goes through each task and executes it
    * creating a new ZNODE under //wokerFinishedTasks with its ansewer when it's done.
    * the master will monitor the //wokerFinishedTasks parent node
    */
   private void processTasks() {
      new Thread(()->{
         while(true) {
            if(this.tasks.peek() != null) {
               Task task = this.tasks.poll();
               String responseString = "";
               switch (task.requestType) {
                  case "insert":
                     String[] tokens = task.parameters.split(":");
                     tmap.put(tokens[0], tokens[1].toBigDecimal());
                     responseString = "okay";
                  break;
                  case "delete":
                     tmap.delete(task.parameters);
                     responseString = "okay";
                  break;
                  case "retrieve":
                     responseString = tmap.get(task.parameters);
                  break;
                  case "calculate":
                    String[] keys = task.parameters.split(":");
                    switch(task.operation) {
                      case("*"):
                        BigDecimal sum = 1;
                        for (String key : keys) {
                          if (tmap.contains(key)) {
                            sum *= map.get(key);
                          }
                        }
                        responseString = "" + sum; 
                        break;
                      case("+"):
                        BigDecimal sum = 0;
                        for (String key : keys) {
                          if (tmap.contains(key)) {
                            sum += map.get(key);
                          }
                        }
                        responseString = "" + sum;
                        break;
                        case ("-"):
                        case ("/"):
                          for (String key : keys) {
                            if (tmap.contains(key)) {
                              responseString += ":" + key;
                            }
                          }
                          break;
                    }
                  break;
               }
               task.response = responseString;
            }
         }
      }).start();
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