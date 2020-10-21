/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.*;

import java.io.Closeable;
import java.io.IOException;
import java.util.concurrent.ConcurrentHashMap;

import org.apache.zookeeper.AsyncCallback.ChildrenCallback;
import org.apache.zookeeper.AsyncCallback.DataCallback;
import org.apache.zookeeper.AsyncCallback.StatCallback;
import org.apache.zookeeper.AsyncCallback.StringCallback;
import org.apache.zookeeper.AsyncCallback.VoidCallback;
import org.apache.zookeeper.CreateMode;
import org.apache.zookeeper.KeeperException;
import org.apache.zookeeper.WatchedEvent;
import org.apache.zookeeper.Watcher;
import org.apache.zookeeper.Watcher.Event.EventType;
import org.apache.zookeeper.ZooDefs.Ids;
import org.apache.zookeeper.ZooKeeper;
import org.apache.zookeeper.KeeperException.Code;

import org.apache.zookeeper.data.Stat;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


/**
 * This class implements the master of the master-worker example we use
 * throughout the book. The master is responsible for tracking the list of
 * available workers, determining when there are new tasks and assigning
 * them to available workers. 
 *
 * The flow without crashes is like this. The master reads the list of
 * available workers and watch for changes to the list of workers. It also
 * reads the list of tasks and watches for changes to the list of tasks.
 * For each new task, it assigns the task to a worker chosen at random.
 *
 * Before exercising the role of master, this ZooKeeper client first needs
 * to elect a primary master. It does it by creating a /master znode. If
 * it succeeds, then it exercises the role of master. Otherwise, it watches
 * the /master znode, and if it goes away, it tries to elect a new primary
 * master.
 *
 * The states of this client are three: RUNNING, ELECTED, NOTELECTED. 
 * RUNNING means that according to its view of the ZooKeeper state, there
 * is no primary master (no master has been able to acquire the /master lock).
 * If some master succeeds in creating the /master znode and this master learns
 * it, then it transitions to ELECTED if it is the primary and NOTELECTED
 * otherwise.
 *
 * Because workers may crash, this master also needs to be able to reassign
 * tasks. When it watches for changes in the list of workers, it also 
 * receives a notification when a znode representing a worker is gone, so 
 * it is able to reassign its tasks.
 *
 * A primary may crash too. In the case a primary crashes, the next primary
 * that takes over the role needs to make sure that it assigns and reassigns
 * tasks that the previous primary hasn't had time to process.
 *
 */
public class Master implements Watcher, Closeable {
    private static final Logger LOG = LoggerFactory.getLogger(Master.class);

    /*
     * A master process can be either running for
     * primary master, elected primary master, or
     * not elected, in which case it is a backup
     * master.
     */
    enum MasterStates {RUNNING, ELECTED, NOTELECTED};

    private volatile MasterStates state = MasterStates.RUNNING;

    MasterStates getState() {
        return state;
    }

    private Random random = new Random(this.hashCode());
    private ZooKeeper zk;
    private String hostPort;
    private String serverId = Integer.toHexString( random.nextInt() );
    private volatile boolean connected = false;
    private volatile boolean expired = false;

    protected ChildrenCache tasksCache;
    protected ChildrenCache workersCache;
    private ConcurrentHashMap<String, String> keyMap = new ConcurrentHashMap<String, String>();

    /**
     * Creates a new master instance.
     *
     * @param hostPort
     */
    Master(String hostPort) {
        this.hostPort = hostPort;
    }


    /**
     * Creates a new ZooKeeper session.
     *
     * @throws IOException
     */
    void startZK() throws IOException {
        //this creates a new zookeeper connection
        zk = new ZooKeeper(hostPort, 15000, this);
    }

    public void initialize() {
        bootstrap();
        runForMaster();
    }

    /**
     * Closes the ZooKeeper session.
     *
     * @throws IOException
     */
    void stopZK() throws InterruptedException, IOException {
        //This closes the zookeeper connection
        zk.close();
    }

    /**
     * This method implements the process method of the
     * Watcher interface. We use it to deal with the
     * different states of a session.
     *
     * @param e new session event to be processed
     */
    public void process(WatchedEvent e) {
        if(e.getType() == Event.EventType.None){
            switch (e.getState()) {
                case SyncConnected:
                    connected = true;
                    break;
                case Disconnected:
                    connected = false;
                    break;
                case Expired:
                    expired = true;
                    connected = false;
                    LOG.error("Session expiration");
                default:
                    break;
            }
        }
    }


    /**
     * This method creates some parent znodes we need for this example.
     * In the case the master is restarted, then this method does not
     * need to be executed a second time.
     */
    public void bootstrap(){
        createParent("/workers", new byte[0]);
        createParent("/assign", new byte[0]);
        createParent("/tasks", new byte[0]);
        createParent("/status", new byte[0]);
        createParent("/results", new byte[0]);
    }

    void createParent(String path, byte[] data){
        /*
        This creates a znode with the given path.
        This is used by the master to create a number of znodes that will function as logical parents to other znodes.
        This is useful because if one calls zk.getChildren(parent) he can get all of the znodes that are children of that znode
        */
        zk.create(path,
                data,
                Ids.OPEN_ACL_UNSAFE,
                CreateMode.PERSISTENT,
                createParentCallback,
                data);
    }

    StringCallback createParentCallback = new StringCallback() {
        public void processResult(int rc, String path, Object ctx, String name) {
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    /*
                     * Try again. Note that registering again is not a problem.
                     * If the znode has already been created, then we get a
                     * NODEEXISTS event back.
                     */
                    createParent(path, (byte[]) ctx);

                    break;
                case OK:

                    break;
                case NODEEXISTS:
                    LOG.warn("Parent already registered: " + path);

                    break;
                default:
                    LOG.error("Something went wrong: ",
                            KeeperException.create(Code.get(rc), path));
            }
        }
    };

    /**
     * Check if this client is connected.
     *
     * @return boolean ZooKeeper client is connected
     */
    boolean isConnected() {
        return connected;
    }

    /**
     * Check if the ZooKeeper session has expired.
     *
     * @return boolean ZooKeeper session has expired
     */
    boolean isExpired() {
        return expired;
    }

    /*
     **************************************
     **************************************
     * Methods related to master election.*
     **************************************
     **************************************
     */


    /*
     * The story in this callback implementation is the following.
     * We tried to create the master lock znode. If it suceeds, then
     * great, it takes leadership. However, there are a couple of
     * exceptional situations we need to take care of.
     *
     * First, we could get a connection loss event before getting
     * an answer so we are left wondering if the operation went through.
     * To check, we try to read the /master znode. If it is there, then
     * we check if this master is the primary. If not, we run for master
     * again.
     *
     *  The second case is if we find that the node is already there.
     *  In this case, we call exists to set a watch on the znode.
     */
    StringCallback masterCreateCallback = new StringCallback() {
        public void processResult(int rc, String path, Object ctx, String name) {
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    checkMaster();

                    break;
                case OK:
                    state = MasterStates.ELECTED;
                    takeLeadership();

                    break;
                case NODEEXISTS:
                    state = MasterStates.NOTELECTED;
                    masterExists();

                    break;
                default:
                    state = MasterStates.NOTELECTED;
                    LOG.error("Something went wrong when running for master.", KeeperException.create(Code.get(rc), path));
            }
            LOG.info("I'm " + (state == MasterStates.ELECTED ? "" : "not ") + "the leader" + serverId);
        }
    };

    void masterExists() {
        //this test to see if a znode exists with the name master. asynchronously
        //the purpose of this is to see if there is already an acting master (i.e. leader).
        /*
        This test to see if there is a znode named master.
        If there is, that means that there is another server that is functioning as the master. That server
            must be running becaues if it weren't then there would be no znode because the znode is ephemeral.
        If there is no znode then the master will create the znode to declare itself the current master
        */
        zk.exists("/master",
                masterExistsWatcher,
                masterExistsCallback,
                null);
    }

    StatCallback masterExistsCallback = new StatCallback() {
        public void processResult(int rc, String path, Object ctx, Stat stat){
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    masterExists();

                    break;
                case OK:
                    break;
                case NONODE:
                    state = MasterStates.RUNNING;
                    runForMaster();
                    LOG.info("It sounds like the previous master is gone, " +
                            "so let's run for master again.");

                    break;
                default:
                    checkMaster();
                    break;
            }
        }
    };

    Watcher masterExistsWatcher = new Watcher(){
        public void process(WatchedEvent e) {
            if(e.getType() == EventType.NodeDeleted) {
                assert "/master".equals( e.getPath() );

                runForMaster();
            }
        }
    };

    void takeLeadership()  {
        deleteOldAssignNodes();
        getWorkers();
        getTasks();
    }

    /*
     * Run for master. To run for master, we try to create the /master znode,
     * with masteCreateCallback being the callback implementation.
     * In the case the create call succeeds, the client becomes the master.
     * If it receives a CONNECTIONLOSS event, then it needs to check if the
     * znode has been created. In the case the znode exists, it needs to check
     * which server is the master.
     */

    /**
     * Tries to create a /master lock znode to acquire leadership.
     */
    public void runForMaster() {
        /*
        Tries to create a znode called /master.
        See comment in the masterExists() method for an explanation as to why this is important.
        */
        zk.create("/master",
                serverId.getBytes(),
                Ids.OPEN_ACL_UNSAFE,
                CreateMode.EPHEMERAL,
                masterCreateCallback,
                null);
    }

    DataCallback masterCheckCallback = new DataCallback() {
        public void processResult(int rc, String path, Object ctx, byte[] data, Stat stat) {
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    checkMaster();

                    break;
                case NONODE:
                    runForMaster();

                    break;
                case OK:
                    if( serverId.equals( new String(data) ) ) {
                        state = MasterStates.ELECTED;
                        takeLeadership();
                    } else {
                        state = MasterStates.NOTELECTED;
                        masterExists();
                    }

                    break;
                default:
                    LOG.error("Error when reading data.", KeeperException.create(Code.get(rc), path));
            }
        }
    };

    void checkMaster() {
        /*
        The master has attempted to create a /master znode. It now checks the data to make sure that the znode that was just created has its information
        If it does then it is indeed the master. Else a different master must have gotten there first.

        Aye, you'll ask that this should have been taken care of by the createMasterCallback, if it successfully created the node then its the master,
        and if not then it's not the master? This is needed too because if there was a connectionLoss or something else that prevented the master from
        recieving the confirmation that it ideed created the znode, it has to check to make sure that the znode that was created came from himself.
        */
        zk.getData("/master", false, masterCheckCallback, null);
    }

    /*
     ****************************************************
     ****************************************************
     * Methods to handle changes to the list of workers.*
     ****************************************************
     ****************************************************
     */


    /**
     * This method is here for testing purposes.
     *
     * @return size Size of the worker list
     */
    public int getWorkersSize(){
        if(workersCache == null) {
            return 0;
        } else {
            return workersCache.getList().size();
        }
    }

    Watcher workersChangeWatcher = new Watcher() {
        public void process(WatchedEvent e) {
            if(e.getType() == EventType.NodeChildrenChanged) {
                assert "/workers".equals( e.getPath() );

                getWorkers();
            }
        }
    };

    void getWorkers(){
        /*
        This gets a list of the znodes that have the prefix /workers/.
        This is important because these znodes represent the workers that are connected to zookeeper. The master can assign them tasks, so 
        the master needs to know who they are and where to assign the tasks too. The master can also detect a change in the list of workers. Lets
        say that a worker died. Then the master knows to delete its assign node and not assign it anything else. And to take its previously assigned
        tasks and reassign them.
        */
        zk.getChildren("/workers",
                workersChangeWatcher,
                workersGetChildrenCallback,
                null);
    }

    ChildrenCallback workersGetChildrenCallback = new ChildrenCallback() {
        public void processResult(int rc, String path, Object ctx, List<String> children){
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    getWorkers();
                    break;
                case OK:
                    reassignAndSet(children);
                    break;
                default:
                    LOG.error("getChildren failed", KeeperException.create(Code.get(rc), path));
            }
        }
    };

    /*
     *******************
     *******************
     * Assigning tasks.*
     *******************
     *******************
     */

    void reassignAndSet(List<String> children){
        List<String> toProcess;

        if(workersCache == null) {
            workersCache = new ChildrenCache(children);
            toProcess = null;
        } else {
            toProcess = workersCache.removedAndSet( children );
        }
    }

    void deleteOldAssignNodes()  {
        List<String> workers = null;
        try {
            /*
            Just in case there were assign nodes that were not deleted from the last session, this method compares the list
            of workers currently connected to zookeeper and compares it against the list of workers that have assign nodes and 
            deletes all of the assign nodes that do not have corresponding worker nodes. This is for cleanup purposes, those nodes wouldn't
            have gotten in the way, they're just clutter.

            The first line gets the list of znodes that have the prefix /workers, and the second line gets the list of 
            znodes with the prefic /assign
            */
            workers = zk.getChildren("/workers", false);
            List<String> assignNodes = zk.getChildren("/assign", false);
            assignNodes.removeAll(workers);
            for (String node : assignNodes) {
                deleteAssignNode(node);
            }
        } catch (KeeperException e) {
            e.printStackTrace();
        } catch (InterruptedException e){
            e.printStackTrace();
        }
    }

    void deleteAssignNode(String worker) {
        /*
        The deletes the znode /assign/<worker>. See previous method.
        */
        zk.delete("/assign/" + worker, -1, deleteOldAssignNodeCallback, null);
    }

    VoidCallback deleteOldAssignNodeCallback = new VoidCallback() {
        @Override
        public void processResult(int rc, String path, Object ctx) {
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    deleteAssignNode(path);

                    break;
                case OK:

                    break;
                case NONODE:
                    LOG.info("Assign Node has been deleted already");

                    break;
                default:
                    LOG.error("Something went wrong here, " +
                            KeeperException.create(Code.get(rc), path));
            }
        }
    };



    /*
     ******************************************************
     ******************************************************
     * Methods for receiving new tasks and assigning them.*
     ******************************************************
     ******************************************************
     */

    Watcher tasksChangeWatcher = new Watcher() {
        public void process(WatchedEvent e) {
            if(e.getType() == EventType.NodeChildrenChanged) {
                assert "/tasks".equals( e.getPath() );

                getTasks();
            }
        }
    };

    void getTasks(){
        /*
        This gets the list of znodes with the prefic /tasks/. These znodes represent the tasks that the client is requesting
        be processed. Each node is one task. This is how the client communicates this to the master.
        */
        zk.getChildren("/tasks",
                tasksChangeWatcher,
                tasksGetChildrenCallback,
                null);
    }

    ChildrenCallback tasksGetChildrenCallback = new ChildrenCallback() {
        public void processResult(int rc, String path, Object ctx, List<String> children){
            switch(Code.get(rc)) {
                case CONNECTIONLOSS:
                    getTasks();

                    break;
                case OK:
                    List<String> toProcess;
                    if(tasksCache == null) {
                        tasksCache = new ChildrenCache(children);

                        toProcess = children;
                    } else {
                        toProcess = tasksCache.addedAndSet( children );
                    }

                    if(toProcess != null){
                        assignTasks(toProcess);
                    }

                    break;
                default:
                    LOG.error("getChildren failed.", KeeperException.create(Code.get(rc), path));
            }
        }
    };

    void assignTasks(List<String> tasks) {
        for(String task : tasks){
            getTaskData(task);
        }
    }

    void getTaskData(String task) {
        /*
        This gets the data for the znode /tasks/<task>. This tells the master the particulars of the request being requested with this znode.
        */
        zk.getData("/tasks/" + task,
                false,
                taskDataCallback,
                task);
    }

    ConcurrentHashMap<String, TaskOrganizer> partialTaskMap = new ConcurrentHashMap<String, TaskOrganizer>();

    class TaskOrganizer {
        String[] operands;
        String taskName;
        String request;
        String operator;
        int numParts;
        int remainingparts = 0;
        HashMap<String, ArrayList<String>> workerToComponentsMap = new HashMap<>();
        LinkedList<String> workerResults = new LinkedList<>();
    }

    DataCallback taskDataCallback = new DataCallback() {
        public void processResult(int rc, String path, Object ctx, byte[] data, Stat stat)  {
            switch(Code.get(rc)) {
                case CONNECTIONLOSS:
                    getTaskData((String) ctx);

                    break;
                case OK:
                    LOG.info("Master just got data for client task: " + path + ", DATA:" + new String(data));
                    /*
                     * Choose worker at random.
                     */
                    List<String> list = workersCache.getList();
                    if (list.size() == 0) {
                        getTaskData((String ) ctx);
                        return;
                    }
                    String designatedWorker = "";

                    String request = new String(data);
                    String[] tokens = request.split(";");
                    switch(tokens[0]) {
                        case "RETRIEVE":
                        case "DELETE":
                            designatedWorker = keyMap.get(tokens[1]);
                            break;
                        case "INSERT":
                            designatedWorker = list.get(random.nextInt(list.size()));
                            break;
                        case "COMPUTE":
                            //will return at the end of switch statement
                            TaskOrganizer organizer = new TaskOrganizer();
                            organizer.request = request;
                            organizer.taskName = (String) ctx;
                            organizer.operator = tokens[1];
                            organizer.operands = tokens[2].split(", ");

                            HashMap<String, String> workersMap = new HashMap<String, String>();

                            for (String operand : organizer.operands) {
                                String worker = keyMap.get(operand);

                                if (!workersMap.containsKey(worker)) {
                                    workersMap.put(worker, "COMPUTE;" + tokens[1] + ";" + operand);
                                    continue;
                                }

                                workersMap.put(worker, (workersMap.get(worker) + ", " + operand));
                            }

                            organizer.numParts = workersMap.size();

                            for (String worker : workersMap.keySet()) {
                                data = workersMap.get(worker).getBytes();
                                String assignmentPath = "/assign/" + worker + "/" + organizer.taskName + "." + organizer.remainingparts++;
                                createAssignment(assignmentPath, data);
                            }

                            partialTaskMap.put(organizer.taskName, organizer);
                            return;
                        default:
                            //something went terribly wrong
                            break;
                    }
                    //all but compute continue here
                    String assignmentPath = "/assign/" + designatedWorker + "/" + (String) ctx;
                    createAssignment(assignmentPath, data);

                    break;
                default:
                    LOG.error("Error when trying to get task data.", KeeperException.create(Code.get(rc), path));
            }
        }
    };

    void createAssignment(String path, byte[] data){
        /*
        This creates the znode with path <path> and data <data>. The purpose of this method is the create a znode  /assign/<worker>/<taskNamer>
        where <taskName> is the name of the task being assigned to the <worker>. This is how the master tells the worker what task it wants it to do.
        The data is the particulars of the request.
        */
        zk.create(path,
                data,
                Ids.OPEN_ACL_UNSAFE,
                CreateMode.EPHEMERAL,
                assignTaskCallback,
                data);
    }

    StringCallback assignTaskCallback = new StringCallback() {
        public void processResult(int rc, String path, Object ctx, String name) {
            switch(Code.get(rc)) {
                case CONNECTIONLOSS:
                    createAssignment(path, (byte[]) ctx);

                    break;
                case OK:
                    String wokerAssignedTaskName = name.substring( name.lastIndexOf("/") + 1);
                    String completeTaskName =
                            (wokerAssignedTaskName.contains(".")) ?
                                    (wokerAssignedTaskName.substring(0, wokerAssignedTaskName.indexOf("."))) : (wokerAssignedTaskName);
                    deleteTask(completeTaskName);
                    watchStatus("/results/" + wokerAssignedTaskName, ctx);

                    break;
                case NODEEXISTS:
                    //LOG.warn("Task already assigned");

                    break;
                default:
                    LOG.error("Error when trying to assign task.", KeeperException.create(Code.get(rc), path));
            }
        }
    };

    /*
     * Once assigned, we delete the task from /tasks
     */
    void deleteTask(String name){
        /*
        This deletes the znode with path /tasks/<name>. This was the znode that the client used to communicate the task over to the master. Once
        the master has read the data of that znode to get the particulars of that request and then delegated the request over to workers to complete, 
        there is no longer any need for this znode to be here. It is just clutter.
        */
        zk.delete("/tasks/" + name, -1, taskDeleteCallback, null);
    }

    VoidCallback taskDeleteCallback = new VoidCallback(){
        public void processResult(int rc, String path, Object ctx){
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    deleteTask(path);

                    break;
                case OK:

                    break;
                case NONODE:
                    //LOG.info("Task has been deleted already");

                    break;
                default:
                    LOG.error("Something went wrong here, " +
                            KeeperException.create(Code.get(rc), path));
            }
        }
    };
    /*
     ******************************************************
     ******************************************************
     **** METHODS FOR GETTING RESULTS FROM THE WORKERS ****
     ******************************************************
     ******************************************************
     */

    ConcurrentHashMap<String, Object> ctxMap = new ConcurrentHashMap<String, Object>();
    void watchStatus(String path, Object ctx){
        ctxMap.put(path, ctx);
        /*
        This check to see if the znode with a particular path exists. Once the master assigns a task to a worker to complete, it expects that 
        when the worker completes that task it will create a znode with path <path> to communicate the results of the task.
        */
        zk.exists(path,
                statusWatcher,
                existsCallback,
                ctx);
    }

    Watcher statusWatcher = new Watcher(){
        public void process(WatchedEvent e){
            if(e.getType() == EventType.NodeCreated) {
                assert e.getPath().contains("/results/task-");
                //assert ctxMap.containsKey( e.getPath() );
                /*
                This gets the data in the znode that the master was just informed that the worker created. This data is the results the task that the
                worker was executing.
                */
                zk.getData(e.getPath(),
                        false,
                        getDataCallback,
                        ctxMap.get(e.getPath()));
            }
        }
    };

    StatCallback existsCallback = new StatCallback(){
        public void processResult(int rc, String path, Object ctx, Stat stat){
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    watchStatus(path, ctx);

                    break;
                case OK:
                    if(stat != null){
                        /*
                        See previous method for explanation of zookeeper usage here.
                        */
                        zk.getData(path, false, getDataCallback, ctx);
                    }

                    break;
                case NONODE:
                    break;
                default:
                    LOG.error("Something went wrong when " + "checking if the status node exists: " + KeeperException.create(Code.get(rc), path));

                    break;
            }
        }
    };

    DataCallback getDataCallback = new DataCallback(){
        public void processResult(int rc, String path, Object ctx, byte[] data, Stat stat) {
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:

                    //Try again.
                    /*
                    See previous method for explanation of zookeeper usage here
                    */
                    zk.getData(path, false, getDataCallback, null);
                    return;
                case OK:
                    String responseString = new String(data);
                    String[] tokens = responseString.split(";");
                    String requestType = tokens[0];
                    String originalClientRequest = responseString.substring(responseString.lastIndexOf(";") + 1);

                    if (requestType.equals("INSERT")) {
                        keyMap.put(tokens[1], tokens[2]);
                        LOG.info("MASTER: Assigned "
                                + originalClientRequest.substring(originalClientRequest.indexOf(" ") + 1, originalClientRequest.lastIndexOf(" "))
                                + " to worker: " + tokens[2]);
                    }
                    if (requestType.equals("DELETE")) keyMap.remove(tokens[1]);
                    if (!requestType.equals("COMPUTE"))
                        /*
                        This creates a znode with the path /status/<task> where <task> was the name of a task that the client assigned the master. The 
                        data is the results of that task. This is used in order to communicate those results back to the client. The client waits for this 
                        znode to exist, and when it is created the client reads the data and gets its answer.
                        */
                        zk.create(path.replace("/results/", "/status/"), originalClientRequest.getBytes(), Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL, taskStatusCreateCallback, null);
                    if(requestType.equals("COMPUTE")) {
                        //get task organizer
                        TaskOrganizer organizer = partialTaskMap.get(path.substring(path.lastIndexOf("/") + 1, path.indexOf(".")));

                        //store and keep track of the information
                        String worker = tokens[4];
                        ArrayList<String> componentList = new ArrayList<>();
                        componentList.addAll(Arrays.asList(tokens[3].split(", ")));
                        organizer.workerToComponentsMap.put(worker, componentList);
                        organizer.workerResults.add(tokens[2]);

                        organizer.remainingparts--;

                        //we have everything that we need, now let's put it all together
                        if (organizer.remainingparts == 0) {
                            //build the string of values in the same order that the keys were requested
                            String componentString = "";
                            for (String key : organizer.operands) {
                                worker = keyMap.get(key);
                                String component = organizer.workerToComponentsMap.get(worker).remove(0);
                                componentString += component + ", ";
                            }
                            componentString = componentString.substring(0, componentString.length() - 2);
                            ArrayList<String> operands = new ArrayList<String>();
                            if(organizer.operator.equals("/") || organizer.operator.equals("-")) operands.addAll(Arrays.asList(componentString.split(", ")));
                            if(organizer.operator.equals("+") || organizer.operator.equals("*")) operands.addAll(organizer.workerResults);
                            int numOperands = operands.size();
                            String result = "";

                            if (numOperands == 1) {
                                result = operands.get(0);
                            } else {
                                BigDecimal total = null;

                                switch(organizer.operator) {
                                    case "*":
                                        total = new BigDecimal(1);
                                        for (int i = 0; i < numOperands; i++)
                                            total = total.multiply(new BigDecimal(operands.get(i)));
                                        break;
                                    case "+":
                                        total = new BigDecimal(0);
                                        for (int i = 0; i < numOperands; i++)
                                            total = total.add(new BigDecimal(operands.get(i)));
                                        break;
                                    case "-":
                                        total = new BigDecimal(operands.remove(0));
                                        for (int i = 0; i < numOperands - 1; i++)
                                            total = total.subtract(new BigDecimal(operands.get(i)));
                                        break;
                                    case "/":
                                        total = new BigDecimal(operands.remove(0));
                                        for (int i = 0; i < numOperands - 1; i++)
                                            total = total.divide(new BigDecimal(operands.get(i)));
                                        break;
                                    default:
                                        break;
                                }

                                result = total.toString();
                            }

                            result = "REQUEST: " + organizer.request + ". RESULT: " + organizer.operator + ": " + componentString + " = " + result;
                            /*
                            See create call earlier in this method for an explanation of the zookeeper usage here.
                            */
                            zk.create("/status/" + organizer.taskName, result.getBytes(), Ids.OPEN_ACL_UNSAFE,
                                    CreateMode.EPHEMERAL, taskStatusCreateCallback, result.getBytes());
                            partialTaskMap.remove(organizer.taskName);
                        }
                    }
                    // Delete status znode
                    /*
                    This tries to delete a znode with path /results/<task>. This znode contained the results of the task executed by the worker. Once
                    the master reads the results and returns them to the client, there is no longer any need for this znode. Cleanup.
                    */
                    zk.delete(path, -1, assignDeleteCallback, null);

                    break;
                case NONODE:
                    LOG.warn("Status node is gone!");
                    return;
                default:
                    LOG.error("Something went wrong here, " +
                            KeeperException.create(Code.get(rc), path));
            }
        }
    };

    StringCallback taskStatusCreateCallback = new StringCallback(){
        public void processResult(int rc, String path, Object ctx, String name) {
            switch(Code.get(rc)) {
                case CONNECTIONLOSS:
                    /*
                    See previous method for explanation of zookeeper usage
                    */
                    zk.create(path + "/status", (byte[]) ctx, Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL,
                            taskStatusCreateCallback, ctx);
                    break;
                case OK:
                    break;
                case NODEEXISTS:
                    LOG.warn("Node exists: " + path);
                    break;
                default:
                    LOG.error("Failed to create task data: ", KeeperException.create(Code.get(rc), path));
            }

        }
    };

    VoidCallback assignDeleteCallback = new VoidCallback(){
        public void processResult(int rc, String path, Object ctx){
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    /*
                    See end of two methods ago for zookeeper usage here
                    */
                    zk.delete(path, -1, assignDeleteCallback, null);
                    break;
                case OK:
                    break;
                default:
                    LOG.error("Something went wrong here, " +
                            KeeperException.create(Code.get(rc), path));
            }
        }
    };

    /**
     * Closes the ZooKeeper session. 
     *
     * @throws IOException
     */
    @Override
    public void close() throws IOException {
        if(zk != null) {
            try{
                //This closes the connection to zookeeper
                zk.close();
            } catch (InterruptedException e) {
                LOG.warn( "Interrupted while closing ZooKeeper session.", e );
            }
        }
    }

    /**
     * Main method providing an example of how to run the master.
     *
     * @param args
     * @throws Exception
     */
    public static void main(String args[]) throws Exception {
        final Master m = new Master(args[0]);
        m.startZK();
        while(!m.isConnected()) Thread.sleep(100);
        m.initialize();

        new Thread(new Runnable(){
            @Override
            public void run() {
                try {
                    Thread.sleep(10000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                try {
                    m.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }
}