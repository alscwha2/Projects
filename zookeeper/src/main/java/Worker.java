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

import java.io.Closeable;
import java.io.IOException;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

//import com.sun.activation.registries.LogSupport;
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
import org.apache.zookeeper.AsyncCallback.ChildrenCallback;
import org.apache.zookeeper.KeeperException.Code;
import org.apache.zookeeper.data.Stat;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Worker implements Watcher, Closeable {
    private static final Logger LOG = LoggerFactory.getLogger(Worker.class);

    private ZooKeeper zk;
    private String hostPort;
    private String serverId = Integer.toHexString((new Random()).nextInt());
    private volatile boolean connected = false;
    private volatile boolean expired = false;

    private ConcurrentHashMap<String, BigDecimal> map = new ConcurrentHashMap<String, BigDecimal>();

    /*
     * In general, it is not a good idea to block the callback thread
     * of the ZooKeeper client. We use a thread pool executor to detach
     * the computation from the callback.
     */
    private ThreadPoolExecutor executor;

    /**
     * Creates a new Worker instance.
     *
     * @param hostPort
     */
    public Worker(String hostPort) {
        this.hostPort = hostPort;
        this.executor = new ThreadPoolExecutor(1, 1,
                1000L,
                TimeUnit.MILLISECONDS,
                new ArrayBlockingQueue<Runnable>(200));
    }

    /**
     * Creates a ZooKeeper session.
     *
     * @throws IOException
     */
    public void startZK() throws IOException {
        /*
        This creates a connection to the zookeeper server.
        */
        zk = new ZooKeeper(hostPort, 15000, this);
    }

    /**
     * Deals with session events like connecting
     * and disconnecting.
     *
     * @param e new event generated
     */
    public void process(WatchedEvent e) {
        LOG.info(e.toString() + ", " + hostPort);
        if(e.getType() == Event.EventType.None){
            switch (e.getState()) {
                case SyncConnected:
                    /*
                     * Registered with ZooKeeper
                     */
                    connected = true;
                    break;
                case Disconnected:
                    connected = false;
                    break;
                case Expired:
                    expired = true;
                    connected = false;
                    LOG.error("Session expired");
                default:
                    break;
            }
        }
    }

    /**
     * Checks if this client is connected.
     *
     * @return boolean
     */
    public boolean isConnected() {
        return connected;
    }

    /**
     * Checks if ZooKeeper session is expired.
     *
     * @return
     */
    public boolean isExpired() {
        return expired;
    }

    /**
     * Bootstrapping here is just creating a /assign parent
     * znode to hold the tasks assigned to this worker.
     */
    public void bootstrap(){
        createAssignNode();
    }

    void createAssignNode(){
        /*
        This creates a znode with the path /assign/worker-<serverid>. This is a parent znode under which the master will post 
        tasks for this worker to execute. 
        */
        zk.create("/assign/worker-" + serverId, new byte[0], Ids.OPEN_ACL_UNSAFE, CreateMode.PERSISTENT,
                createAssignCallback, null);
    }

    StringCallback createAssignCallback = new StringCallback() {
        public void processResult(int rc, String path, Object ctx, String name) {
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    /*
                     * Try again. Note that registering again is not a problem.
                     * If the znode has already been created, then we get a
                     * NODEEXISTS event back.
                     */
                    createAssignNode();
                    break;
                case OK:
                    break;
                case NODEEXISTS:
                    LOG.warn("Assign node already registered");
                    break;
                default:
                    LOG.error("Something went wrong: " + KeeperException.create(Code.get(rc), path));
            }
        }
    };

    String name;

    /**
     * Registering the new worker, which consists of adding a worker
     * znode to /workers.
     */
    public void register(){
        name = "worker-" + serverId;
        /*
        This creates a znode with the path /workers/worker-<serverid>. This is the worker informing the master of its existence that that it
        is availible for the master to assign tasks to.
        */
        zk.create("/workers/" + name,
                "Idle".getBytes(),
                Ids.OPEN_ACL_UNSAFE,
                CreateMode.EPHEMERAL,
                createWorkerCallback, null);
    }

    StringCallback createWorkerCallback = new StringCallback() {
        public void processResult(int rc, String path, Object ctx, String name) {
            switch (Code.get(rc)) {
                case CONNECTIONLOSS:
                    /*
                     * Try again. Note that registering again is not a problem.
                     * If the znode has already been created, then we get a
                     * NODEEXISTS event back.
                     */
                    register();

                    break;
                case OK:

                    break;
                case NODEEXISTS:
                    LOG.warn("Already registered: " + serverId);

                    break;
                default:
                    LOG.error("Something went wrong: ",
                            KeeperException.create(Code.get(rc), path));
            }
        }
    };

    StatCallback statusUpdateCallback = new StatCallback() {
        public void processResult(int rc, String path, Object ctx, Stat stat) {
            switch(Code.get(rc)) {
                case CONNECTIONLOSS:
                    updateStatus((String)ctx);
                    return;
            }
        }
    };

    String status;
    synchronized private void updateStatus(String status) {
        if (status == this.status) {
            /*
            This changes the data of the /worker/ child node of this worker. That data represents the status of the worker. If the status is "idle" 
            that means that the worker is not doing anything and is availible to recieve new tasks. If the status is "working" that means that this
            worker is working, and the new tasks should preferably be assigned to another worker.
            */
            zk.setData("/workers/" + name, status.getBytes(), -1,
                    statusUpdateCallback, status);
        }
    }

    public void setStatus(String status) {
        this.status = status;
        updateStatus(status);
    }

    private int executionCount;

    synchronized void changeExecutionCount(int countChange) {
        executionCount += countChange;
        if (executionCount == 0 && countChange < 0) {
            // we have just become idle
            setStatus("Idle");
        }
        if (executionCount == 1 && countChange > 0) {
            // we have just become idle
            setStatus("Working");
        }
    }
    /*
     ***************************************
     ***************************************
     * Methods to wait for new assignments.*
     ***************************************
     ***************************************
     */

    Watcher newTaskWatcher = new Watcher(){
        public void process(WatchedEvent e) {
            if(e.getType() == EventType.NodeChildrenChanged) {
                assert new String("/assign/worker-"+ serverId ).equals( e.getPath() );

                getTasks();
            }
        }
    };

    void getTasks(){
        /*
        This tries to get the children of this worker's assign node. Those children are the tasks that this worker has to complete. This is how the
        worker recieves tasks from the master.
        */
        zk.getChildren("/assign/worker-" + serverId,
                newTaskWatcher,
                tasksGetChildrenCallback,
                null);
    }


    protected ChildrenCache assignedTasksCache = new ChildrenCache();

    ChildrenCallback tasksGetChildrenCallback = new ChildrenCallback() {
        public void processResult(int rc, String path, Object ctx, List<String> children){
            switch(Code.get(rc)) {
                case CONNECTIONLOSS:
                    getTasks();
                    break;
                case OK:
                    if(children != null){
                        if (children.size() != 0) {
                            String logString = "Worker-" + serverId + ": Just recieved tasks: ";
                            for (String child : children) logString += child + " ";
                            LOG.info(logString);
                        }
                        executor.execute(new Runnable() {
                            List<String> children;
                            DataCallback cb;

                            /*
                             * Initializes input of anonymous class
                             */
                            public Runnable init (List<String> children, DataCallback cb) {
                                this.children = children;
                                this.cb = cb;

                                return this;
                            }

                            public void run() {
                                if(children == null) {
                                    return;
                                }

                                setStatus("Working");
                                for(String task : children){
                                    /*
                                    The gets the data for a particular task znode that was assigned to this worker. That data will contain the particulars
                                    of the request of the client.
                                    */
                                    zk.getData("/assign/worker-" + serverId  + "/" + task,
                                            false,
                                            cb,
                                            task);
                                }
                            }
                        }.init(assignedTasksCache.addedAndSet(children), taskDataCallback));
                    }
                    break;
                default:
                    System.out.println("getChildren failed: " + KeeperException.create(Code.get(rc), path));
            }
        }
    };

    DataCallback taskDataCallback = new DataCallback() {
        public void processResult(int rc, String path, Object ctx, byte[] data, Stat stat){
            switch(Code.get(rc)) {
                case CONNECTIONLOSS:
                    /*
                    See previous method for zookeeper usage.
                    */
                    zk.getData(path, false, taskDataCallback, null);
                    break;
                case OK:
                    /*
                     *  Executing a task in this example is simply printing out
                     *  some string representing the task.
                     */
                    LOG.info("Worker-" + serverId
                            + " just recieved assignment information for task "
                            + path.substring(path.indexOf("/"))
                            + " ASSIGNMENT: " + new String(data));
                    executor.execute( new Runnable() {
                        byte[] data;
                        Object ctx;

                        /*
                         * Initializes the variables this anonymous class needs
                         */
                        public Runnable init(byte[] data, Object ctx) {
                            this.data = data;
                            this.ctx = ctx;

                            return this;
                        }

                        public void run() {
                            //parse the request into tokens
                            String request = new String(data);
                            String[] tokens = request.split(";");
                            String requestType = tokens[0];

                            String response = requestType + ";";

                            //deal with request based on method / parameter tokens
                            switch(requestType) {
                                case "INSERT":
                                    map.put(tokens[1], new BigDecimal(tokens[2]));
                                    LOG.info("Worker-" + serverId + " just stored " + "key:" + tokens[1] + ", value:" + tokens[2]);
                                    response += tokens[1] + ";worker-" + serverId + ";Insert key: " + tokens[1] + ", value: " + tokens[2] + " SUCCESS";
                                    break;
                                case "DELETE":
                                    map.remove(tokens[1]);
                                    LOG.info("Worker-" + serverId + " just deleted entry for key:" + tokens[1]);
                                    response += tokens[1] + ";Delete key: " + tokens[1] + " SUCCESS";
                                    break;
                                case "RETRIEVE":
                                    String value = map.get(tokens[1]).toString();
                                    LOG.info("Worker-" + serverId
                                            + " just retrieved value (" + value + ") for key " + tokens[1]
                                            + " to return to master");
                                    response += value + ";" + "Retrieve key: " + tokens[1] + ", Value:" + value + ", SUCCESS";
                                    break;
                                case "COMPUTE":
                                    String operator = tokens[1];
                                    String computationString = "";
                                    response += operator + ";";
                                    String logString;
                                    String[] operands = tokens[2].split(", ");
                                    switch(operator) {
                                        case "/":
                                        case "-":
                                            computationString += map.get(operands[0]).toString();
                                            for (int i = 1; i < operands.length; i++) computationString += ", " + map.get(operands[i]).toString();
                                            response += computationString + ";" + computationString;
                                            LOG.info("Worker-" + serverId
                                                    + " just retrieved values for request: " + request
                                                    + ": VALUES: " + computationString
                                                    + " to return to master");
                                            break;
                                        case "+":
                                            logString = " SUBCALCULATION: +:";
                                            BigDecimal sum = new BigDecimal(0);
                                            for (String operand : operands) {
                                                BigDecimal nextNumber = map.get(operand);
                                                logString += nextNumber.toString() + ", ";
                                                sum = sum.add(nextNumber);
                                                computationString += nextNumber.toString() + ", ";
                                            }
                                            logString = logString.substring(0, logString.length() - 2);
                                            logString += " = " + sum.toString();
                                            computationString = computationString.substring(0, computationString.length() - 2);
                                            LOG.info("Worker-" + serverId + logString);
                                            LOG.info("Worker-" + serverId
                                                    + " retrieved info to return to master "
                                                    + "REQUEST: " + request
                                                    + ", INFO: sum:" + sum.toString()
                                                    + ", components:" + computationString);
                                            response += sum.toString() + ";" + computationString;
                                            break;
                                        case "*":
                                            logString = " SUBCALCULATION: *:";
                                            BigDecimal product = new BigDecimal(1);
                                            for (String operand : operands) {
                                                BigDecimal nextNumber = map.get(operand);
                                                logString += nextNumber.toString() + ", ";
                                                product = product.multiply(nextNumber);
                                                computationString += nextNumber.toString() + ", ";
                                            }
                                            logString = logString.substring(0, logString.length() - 2);
                                            logString += " = " + product.toString();
                                            computationString = computationString.substring(0, computationString.length() - 2);
                                            LOG.info("Worker-" + serverId + logString);
                                            LOG.info("Worker-" + serverId
                                                    + " recieved info for master "
                                                    + "REQUEST: " + request
                                                    + ", INFO: product:" + product.toString()
                                                    + ", components:" + computationString);
                                            response += product.toString() + ";" + computationString;
                                            break;
                                        default:
                                            break;
                                    }
                                    response += ";worker-" + serverId;
                                    break;
                                default:
                                    break;
                            }
                            /*
                            This creates a znode with the path /results/<taskname>. The data for this znode will the be worker's response
                            to the tasks assigned to it by the master. The master will read the data of this znode and take it from there to get
                            the results back to the client.
                            */
                            zk.create("/results/" + (String) ctx, response.getBytes(), Ids.OPEN_ACL_UNSAFE,
                                    CreateMode.EPHEMERAL, taskResultsCreateCallback, response);
                            /*
                            This deletes the task node that was assigned to the worker. Once the worker already completed the task and made a /results/ znode
                            there is no reason that the task znode should stick aroung. Cleanup.
                            */
                            zk.delete("/assign/worker-" + serverId + "/" + (String) ctx,
                                    -1, taskVoidCallback, null);
                        }
                    }.init(data, ctx));

                    break;
                default:
                    LOG.error("Failed to get task data: ", KeeperException.create(Code.get(rc), path));
            }
        }
    };

    StringCallback taskResultsCreateCallback = new StringCallback(){
        public void processResult(int rc, String path, Object ctx, String name) {
            switch(Code.get(rc)) {
                case CONNECTIONLOSS:
                    /*
                    See previous method for zookeeper usage.
                    */
                    zk.create(path + "/results", "done".getBytes(), Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL,
                            taskResultsCreateCallback, null);
                    break;
                case OK:
                    LOG.info("Worker-" + serverId + " Created results znode correctly (returning info to the master): " + path + " DATA: " + (String) ctx);
                    break;
                case NODEEXISTS:
                    LOG.warn("Node exists: " + path);
                    break;
                default:
                    LOG.error("Failed to create task data: ", KeeperException.create(Code.get(rc), path));
            }

        }
    };

    VoidCallback taskVoidCallback = new VoidCallback(){
        public void processResult(int rc, String path, Object rtx){
            switch(Code.get(rc)) {
                case CONNECTIONLOSS:
                    break;
                case OK:
                    LOG.info("Worker-" + serverId
                            + " just deleted assignment znode: " + path);
                    break;
                default:
                    LOG.error("Failed to delete task data" + KeeperException.create(Code.get(rc), path));
            }
        }
    };

    public void initialize() {
        bootstrap();
        register();
        getTasks();
    }

    public void kill() throws InterruptedException, KeeperException {
        executor.shutdown();
        /*
        This deletes the assign node for this worker. Since this worker is about to close the connection to zookeeper, there
        is no reason to keep the assign znode there. Aye you'll say what happens when the master already assigned it a task and now
        this is deleting the assign znode? Well I'm the one who wrote the code for the master too (sort of partially) and I'm the one who
        wrote the bash script, and I'm only going to call this method when I'm shutting now the master as well.
        */
        zk.delete("/assign/worker-" + serverId, -1);
        /*
        This closes the connection to zookeeper.
        */
        zk.close();
    }

    /**
     * Closes the ZooKeeper session.
     */
    @Override
    public void close()
            throws IOException
    {
        LOG.info( "Closing" );
        try{
            /*
            This closes the connection to zookeeper.
            */
            zk.close();
        } catch (InterruptedException e) {
            LOG.warn("ZooKeeper interrupted while closing");
        }
    }

    /**
     * Main method showing the steps to execute a worker.
     *
     * @param args
     * @throws Exception
     */
    public static void main(String args[]) throws Exception {
        final Worker w = new Worker(args[0]);
        w.startZK();
        while(!w.isConnected()) Thread.sleep(100);
        w.initialize();
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(10000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                try {
                    w.kill();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (KeeperException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }
}