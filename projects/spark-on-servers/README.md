# Running Apache Spark on a Server

It's time to address the topic of Spark on a server. A long time ago, I tried to do this on my own computer, but due to the complexity of the process (hey, don't blame me! I was a student then!), I failed. Java, dependencies, and PySpark defeated me.

Nowadays, it seems like a much easier process, but due to my DevOps spirit, I prefer to run everything in Docker because it's simply easier for me that way. Therefore, this note will contain only the dry theory and nothing practical.

## Transferring the Application to the Server

To transfer the `app.jar` file from your local computer to the server, you can use the `scp` (secure copy) command. Here's an example command:

```bash
scp path/to/your/app.jar username@server_address:/path/on/server/
```

*Replace path/to/your/app.jar with the path to your JAR file, username with your server username, server_address with your server's address, and /path/on/server/ with the desired path on the server.

## How Spark Runs

1. **Submitting the Application**:
   - The user sends the `app.jar` file from their local computer to the Driver.
   - The Driver is the main component of the Spark application, managing the execution of the entire job.
   - To transfer the `app.jar` file to the server from a local computer, we can use tools like `scp`.

2. **Resource Management by YARN**:
   - YARN (Yet Another Resource Negotiator) is a resource management framework in Hadoop.
   - After submitting the application, YARN allocates the necessary resources to run the job.
   - YARN manages both the allocation and monitoring of resources during job execution.

## What is YARN

YARN is a resource management system used in Hadoop that allows running different types of applications on a cluster. It enables:
- **Resource Management**: Allocating resources to various applications running on the cluster.
- **Job Scheduling**: Deciding when and where to run individual tasks.
- **Monitoring**: Tracking resources and job states to ensure efficient utilization.

## Alternatives to YARN

Instead of YARN, Spark can also be run on other platforms:
- **Kubernetes**: A popular container orchestration system.
- **Mesos**: A cluster resource management system.
- **Local Computer**: Spark can be run locally for testing or development purposes.

## `spark-submit`

`spark-submit` is the tool used to run Spark applications. When we invoke `spark-submit`, the process is as follows:
- The application is sent to the Driver.
- The Driver communicates with the resource manager (e.g., YARN) to allocate resources.
- The resource manager launches tasks on various nodes in the cluster.

### Options for `spark-submit`:
- `--master`: Specifies the master URL (e.g., `yarn`, `mesos`, `k8s`, `local`).
- `--deploy-mode`: Deployment mode (`client` or `cluster`).
  - `Client`: Driver runs locally. It starts the master where we wanted and gives us direct access to the logs (especially use for development)
  - `Cluster`: Driver runs on the cluster nodes. Access to log via YARN.
- `--driver-memory`: Amount of memory for the Driver.
- `--driver-cores`: Number of CPU cores for the Driver.
- `--num-executors`: Number of executors.
- `--executor-memory`: Amount of memory for each executor.
- `--executor-cores`: Number of CPU cores for each executor.
- `--total-executor-cores`: Total number of CPU cores for all executors.
- `--class`: Main class of the application.
- `--jars`: Additional JARs required by the application.
- `--verbose`: Enables verbose mode.
- `--files`: Additional files to be available to the application.

### Example Spark-Submit Script

```bash
#!/bin/bash

spark-submit \
  --class com.example.MyApp \
  --master yarn \
  --deploy-mode cluster \
  --driver-memory 4g \
  --driver-cores 2 \
  --num-executors 10 \
  --executor-memory 8g \
  --executor-cores 4 \
  --total-executor-cores 40 \
  --jars additional.jar \
  --verbose \
  app.jar
```

## Example Spark Application Code
```python
from pyspark import SparkConf, SparkContext

def main():
    # Spark application configuration
    conf = SparkConf().setAppName("WordCount").setMaster("yarn")
    sc = SparkContext(conf=conf)

    # Reading the text file
    input_file = "path/to/input.txt"
    output_file = "path/to/output"
    text_file = sc.textFile(input_file)

    # Data processing - counting words
    counts = text_file.flatMap(lambda line: line.split(" ")) \
                      .map(lambda word: (word, 1)) \
                      .reduceByKey(lambda a, b: a + b)

    # Saving results to a file
    counts.saveAsTextFile(output_file)

    # Stopping the Spark context
    sc.stop()

if __name__ == "__main__":
    main()
```

## Example Bash Script to Run the Spark Application
A bash script that runs the above Spark application using spark-submit:
```bash
#!/bin/bash

# Path to the application JAR file
APP_JAR="path/to/your/app.jar"

# Path to the input file
INPUT_FILE="path/to/input.txt"

# Path to the output directory
OUTPUT_DIR="path/to/output"

spark-submit \
  --class WordCount \
  --master yarn \
  --deploy-mode cluster \
  --driver-memory 4g \
  --driver-cores 2 \
  --num-executors 10 \
  --executor-memory 8g \
  --executor-cores 4 \
  --total-executor-cores 40 \
  $APP_JAR $INPUT_FILE $OUTPUT_DIR
```

## Sample Output from Running spark-submit
When you run a Spark application using `spark-submit`, you will see a series of log messages that provide details about the application's execution. Below is a sample output that you might see when running the provided PySpark word count example.

```text
20/05/21 10:30:12 INFO SparkContext: Running Spark version 3.1.1
20/05/21 10:30:12 INFO ResourceUtils: ==============================================================

20/05/21 10:30:12 INFO SparkContext: Submitted application: WordCount
20/05/21 10:30:12 INFO ResourceAllocationManager: Allocating resources for application WordCount
20/05/21 10:30:13 INFO YarnAllocator: Will request 10 executor containers, each with 4 cores and 8 GB memory
20/05/21 10:30:14 INFO YarnAllocator: Container requested: 10
20/05/21 10:30:15 INFO YarnAllocator: Container allocation successful for 10 executors
20/05/21 10:30:15 INFO SparkContext: Spark UI available at http://node:4040

20/05/21 10:30:16 INFO ExecutorAllocationManager: Starting 10 executors
20/05/21 10:30:18 INFO BlockManagerMasterEndpoint: Registering block manager
20/05/21 10:30:18 INFO BlockManagerMaster: Registered BlockManager
20/05/21 10:30:19 INFO YarnSchedulerBackend$YarnDriverEndpoint: Registered executor
20/05/21 10:30:19 INFO YarnScheduler: Successfully registered with YARN ResourceManager

20/05/21 10:30:20 INFO DAGScheduler: Got job 0 (reduce at WordCount.py:15) with 2 output partitions
20/05/21 10:30:20 INFO DAGScheduler: Submitting 2 missing tasks from ResultStage 0 (reduce at WordCount.py:15) (2 tasks)
20/05/21 10:30:20 INFO TaskSchedulerImpl: Adding task set 0.0 with 2 tasks

20/05/21 10:30:21 INFO YarnScheduler: Starting task 0.0 in stage 0.0 (TID 0, executor 1)
20/05/21 10:30:21 INFO YarnScheduler: Starting task 1.0 in stage 0.0 (TID 1, executor 2)

20/05/21 10:30:23 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 2000 ms on executor 1 (1/2)
20/05/21 10:30:23 INFO TaskSetManager: Finished task 1.0 in stage 0.0 (TID 1) in 1800 ms on executor 2 (2/2)
20/05/21 10:30:23 INFO YarnScheduler: Completed TaskSet 0.0 in 3000 ms

20/05/21 10:30:23 INFO DAGScheduler: ResultStage 0 (reduce at WordCount.py:15) finished in 3.0 s
20/05/21 10:30:23 INFO DAGScheduler: Job 0 finished: reduce at WordCount.py:15, took 3.5 s

20/05/21 10:30:24 INFO SparkContext: Invoking stop() from shutdown hook
20/05/21 10:30:24 INFO YarnAllocator: Sending Stop request to executors
20/05/21 10:30:24 INFO SparkContext: Successfully stopped SparkContext

20/05/21 10:30:24 INFO ShutdownHookManager: Shutdown hook called
20/05/21 10:30:24 INFO ShutdownHookManager: Deleting directory /tmp/spark-1234
20/05/21 10:30:24 INFO ShutdownHookManager: Application finished successfully

20/05/21 10:30:24 INFO YarnClientSchedulerBackend: Shutdown successful
```

### This output includes:

- Information about the SparkContext and the Spark version.
- Messages indicating the allocation of resources and containers in YARN.
- Information about the registration and starting of executors.
- Details on the submission and completion of tasks and stages.
- Messages confirming the stopping and cleanup of the Spark application.

## Comparison of JAR and Fat JAR

- **JAR (Java Archive)**: A standard format for packaging Java applications, containing code, resources, and metadata.
- **Fat JAR**: A special type of JAR that includes all dependencies of the application, making it easier to distribute and run in different environments without additional configuration.

### Advantages of Fat JAR:

- Easier distribution and execution.
- Reduces the risk of dependency version conflicts.

### Disadvantages of Fat JAR:

- Larger file size, which can affect transfer times.
- May contain unnecessary dependencies, increasing memory usage.
