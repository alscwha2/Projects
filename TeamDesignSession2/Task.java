  public class Task {
    private String creationString;
    public int clientRequestNumber;
    public String requestType;
    public String operation;
    public String parameters;

    public HashSet<Integer> workerTaskNumbers;
    public String response;

    public Task(String nodeString) {
      creationString = nodeString;

      String[] tokens = nodeString.split(";")
      clientRequestNumber = Integer.parseInt(tokens[0]);
      requestType = tokens[1];
      operation = tokens[2]
      paramters = tokens[3];
      workerTaskNumbers = new HashSet<Integer>();
    }

    @Override
    public String toString() {
      return creationString;
    }
  }