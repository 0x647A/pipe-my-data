# Hadoop

Apache Hadoop is a software framework for storing and processing large data sets (big data) in a distributed manner across clusters of computers built from simple hardware. Hadoop is an open-source project managed by the Apache Software Foundation.

### Hadoop consists of four main modules:

1. **Hadoop Common** - Contains libraries and utilities needed for other Hadoop modules.
2. **Hadoop Distributed File System (HDFS)** - A distributed file system that stores data across multiple machines, ensuring very high access throughput.
3. **Hadoop YARN** - A resource management platform that coordinates the work of clusters.
4. **Hadoop MapReduce** - A programming model for processing data in a distributed manner.

### Key features of Hadoop:

- **Scalability**: Hadoop operates on clusters from a few to thousands of machines, offering scalability at the hardware level.
- **Fault tolerance**: Automatically stores multiple copies of data on different machines to ensure resilience against hardware failures.
- **Efficiency**: Effectively processes gigabytes, terabytes, or even petabytes of data.
- **Low cost**: Since Hadoop is open-source software, it can run on standard hardware, reducing costs.

### Applications of Hadoop:

- **Large-scale data processing**: Analysis of logs, processing social media data, signal processing.
- **Data warehousing**: As a system for storing and analyzing data from various sources.
- **Real-time data processing**: Although Hadoop is typically associated with batch processing, extensions such as Apache Storm and Apache Flink allow for real-time data stream processing.

Hadoop has become the foundation for many other big data technologies, including NoSQL databases, data analysis platforms, and the Apache Spark ecosystem. Its ability to process and store vast amounts of data makes it a key tool in the era of big data.

Apache Hadoop consists of several key components that together provide its powerful functionality for processing and storing data on a large scale.

## Hadoop YARN (Yet Another Resource Negotiator)

YARN is a resource management system that introduces the concept of separating resource management functions and scheduling/managing tasks. Its main goal is to increase the scalability and flexibility of the Hadoop cluster. YARN consists of three main components:

- **ResourceManager (RM)**: A global management element that allocates resources throughout the system, based on policies and application requirements.
- **NodeManager (NM)**: An agent running on each node in the cluster, responsible for monitoring resource consumption on the node and reporting to the ResourceManager.
- **ApplicationMaster (AM)**: An instance launched for each application, which negotiates resources with the ResourceManager and works with the NodeManager to execute and monitor tasks.

## Hadoop Distributed File System (HDFS)

HDFS is a distributed file system designed to store very large files with high access throughput. It is characterized by the following features:

- **High fault tolerance**: Automatically replicates data blocks on multiple machines to ensure resilience to failures.
- **Scalability**: Can scale to thousands of nodes in a cluster, supporting petabytes of data.
- **Optimization for large files**: Designed to store large files, with a typical block size of data being 128 MB or more.

## MapReduce Model

MapReduce is a programming model and implementation for processing and generating large data sets. MapReduce jobs are divided into two main stages: Map and Reduce.

- **Map Stage**: In this phase, input data is divided into smaller subsets, which are then processed by mapping functions in parallel. Each mapping function processes a small piece of data and generates key/value pairs as a result.

- **Reduce Stage**: In the reduction phase, all key/value pairs with the same key are grouped together. For each key, a reducing function is called to merge related values into a smaller number of values or a single result.

#### Example MapReduce Workflow:

- **Input**: Input data is divided into blocks of data and distributed across the nodes of the cluster.
- **Map**: Each block of data is processed by a mapping function, which creates key/value pairs.
- **Shuffle**: Key/value pairs are sorted and grouped by key.
- **Reduce**: For each set of values associated with the same key, a reducing function generates a resulting data set.

The MapReduce model enables scalable and flexible processing of large data sets, distributing the workload across many nodes and efficiently managing resources and processing.

Here's a simple example of a MapReduce algorithm in Python, which calculates the number of occurrences of each word in a text. The algorithm is divided into three main parts: mapping, shuffling, and reducing.

### Step 1: Mapping

In this phase, the input text is split into smaller parts, and each part is processed to create key-value pairs, where the key is a word, and the value is the number 1, indicating a single occurrence of that word.

```python
# Input text
text = "hello world hello"

# Mapping function
def map_function(text):
    # Split text into words
    words = text.split()
    # For each word, return a pair (word, 1)
    return [(word, 1) for word in words]

mapped_results = map_function(text)
print("Mapping:", mapped_results)
```
### Step 2: Shuffling

This phase involves sorting and grouping the output of the mapping phase by key (in this case, by word), preparing it for the reducing phase.
```python
# Function to group words
def shuffle_and_sort(mapped_results):
    sorted_results = sorted(mapped_results)
    grouped_results = {}
    for key, value in sorted_results:
        if key in grouped_results:
            grouped_results[key].append(value)
        else:
            grouped_results[key] = [value]
    return grouped_results

shuffled_and_sorted_results = shuffle_and_sort(mapped_results)
print("Shuffling and Sorting:", shuffled_and_sorted_results)
```
### Step 3: Reducing

In the reducing phase, we aggregate the values for each key (word) to calculate their total occurrences in the text.
```python
# Reducing function
def reduce_function(grouped_results):
    reduced_results = {}
    for key, values in grouped_results.items():
        reduced_results[key] = sum(values)
    return reduced_results

reduced_results = reduce_function(shuffled_and_sorted_results)
print("Reducing:", reduced_results)
```

Summary of the Algorithm's Operation:

- `Mapping`: The text is split into words, and then a pair (word, 1) is created for each word.
- `Shuffling and Sorting`: The mapping results are sorted and grouped by words.
- `Reducing`: We aggregate the values for each word to compute the total number of its occurrences.
