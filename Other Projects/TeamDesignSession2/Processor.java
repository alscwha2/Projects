public class processor implements AsyncCallback.ChildrenCallback {
  private Object caller;
  private Class<> callerClass;
  private String watchPath;

  private processor(Object caller, Class<> class, String path, LinkedBlockingQueue queue) {
    this.caller = caller;
    this.callerClass = class;
    this.watchPath = path;
    this.queue = queue;
  }

  public void processResult(int rc, String path, Object ctx, List<String> children) {
    for (String znode : children) {
      Task task = new Task(znode);
      queue.put(task);
      zk.delete(path + "/task-" + task.clientRequestNumber, VERSION);
    }
    ((callerClass)caller).watchForChildren(watchPath);
  }
}