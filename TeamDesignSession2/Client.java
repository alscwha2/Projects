//Classes: Master, Worker, Client

public class Client {
	int numberOfTasksAssigned;
	Zookeeper zk;

  /**
   * Constructor
   * @param Zookeeper zk
   */
  public Client(Zookeeper zk) {
  	this.zk = zk;
  	this.numberOfTasksAssigned = 0;
  }

  /**
   * Inserts a key-value pair
   * @param String key
   * @param BigDecimal value
   */
  public void insert(String key, BigDecimal value) {
  	return this.process("insert:" + key + ":" + value);
  }

  /**
   * Deletes a key and its value
   * @param String key
   */
  public void delete(String key) {
  	return this.process("delete:" + key);
  }

  public BigDecimal retrieve(String key) {
  	return this.process("retrieve:" + key).toBigDecimal();
  }

  /**
   *
   * @param char op
   * @param ArrayList<String> keys
   **/
  public BigDecimal calculate(char op, ArrayList<String> keys) {
    String requestString = "calculate;" + op;
    for (String key : keys) requestString += ":" key;
  	return this.process(requestString).toBigDecimal();
  }

  private String process(String requestString) {
  	int number = ++numberOfTasksAssigned;
    zk.create("//waitingTasks/task-" + number, "" + number + ";" + requestString.toByteArray(), WHATISANACL?, EPHEMERAL, ASYNCHCALLBACK);
  	while(TASK HAS NOT COMPLETED) {
	  	PUT A WATCHER ON PATH //masterFinishedTasks
	  	check to see if the task number matches
	  	if(matches) {
	  		return the answer that is stored somewhere in the znode;
	  	}
  	}
  }

  /**
   * Main Method
   * @param String[] args: Command line arguments
   */
  public static void main(String[] args) {
  	String host = args[0];
  	String port = args[1];
  	Zookeeper zk = New Zookeeper(host + ":" + port, 1000, NEW WATCHER());

  	Client client = new Client(zk);
  }
}