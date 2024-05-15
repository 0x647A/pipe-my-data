# The first step with basic data structure in Apache Spark

In this directory, you will find the code that allowed me to familiarize myself with Spark's data structures such as RDD and DataFrame.

The dataset I downloaded from: [Kaggle](https://www.kaggle.com/datasets/binduvr/pro-mma-fighters?resource=download)

## Understanding Basic Data Structures in Apache Spark

Apache Spark provides several data structures that cater to different needs for data processing and analysis. The primary structures are RDD, DataFrame, and Dataset. Each has its own unique features and use cases in the Spark ecosystem.

### RDD (Resilient Distributed Dataset)

- **Definition**: RDD is the fundamental data structure of Apache Spark. It is an immutable distributed collection of objects, which can be processed in parallel.
- **Features**: RDDs provide low-level functionality and fine-grained control over data processing. They allow user-defined transformations and actions and can be created through deterministic operations on either data in stable storage or other RDDs.
- **Use Cases**: RDDs are best used when you need complete control over data processing details, and when you are working with unstructured data like media streams or text files.

### DataFrame

- **Definition**: A DataFrame is a distributed collection of data organized into named columns. It is conceptually equivalent to a table in a relational database or a data frame in R/Python, but with richer optimizations under the hood.
- **Features**: DataFrames allow for high-level abstractions and provide built-in methods for many transformations and actions. They are optimized by Spark’s Catalyst optimizer, which generates an efficient query plan to process the data.
- **Use Cases**: DataFrames are ideal for handling structured and semi-structured data. They simplify handling of large datasets and are generally faster than RDDs due to their built-in optimization.

### Dataset

- **Definition**: Datasets are a combination of DataFrame’s optimization and RDD’s functional programming interface. They are strongly typed like RDDs but at the same time offer the operational benefits of DataFrames.
- **Features**: Datasets provide type safety, which is not available in DataFrames, and are optimized by the Catalyst query optimizer, similar to DataFrames.
- **Use Cases**: Datasets are generally used when you need type safety for JVM objects (especially in Scala or Java API) and want to take advantage of Catalyst’s optimization capabilities.

### Important! 

In Apache Spark, although Datasets (including DataFrames) provide a more optimized and high-level interface for data processing, they are fundamentally based on RDDs (Resilient Distributed Datasets) underneath. RDD is the core data abstraction in Spark, offering a resilient and distributed collection of objects. Datasets and DataFrames were introduced to provide a higher level of abstraction, enabling more optimized data processing and better support for query optimization. However, every operation performed on Datasets or DataFrames eventually gets transformed into operations on RDDs. This allows them to leverage the same fault-tolerant and distributed computation capabilities that are key features of RDDs.

## The questions I asked myself while working with data structures in Spark: 

## Why did I use SparkContext when working with RDDs, and SparkSession when working with DataFrames?

Apache Spark offers two primary ways to interact with its features: **SparkContext** and **SparkSession**. Each serves a distinct role in the Spark ecosystem, and choosing the right one depends on the specific needs of your application.

### SparkContext

- **Usage**: SparkContext is the original entry point for Spark functionalities and is still used for working with RDDs (Resilient Distributed Datasets). RDDs are the fundamental data abstraction in Spark, offering low-level processing and fine-grained control over data operations.
- **Features**: RDDs allow detailed transformation and action operations on distributed data. This control is crucial for complex data processing tasks where full control over data handling and execution is needed.
- **Context**: SparkContext is necessary for applications that require direct RDD manipulations for intricate processing needs and where the developer needs precise control over the execution.

### SparkSession

- **Introduced**: SparkSession was introduced in Spark 2.0 as a unified entry point to all Spark functionalities, simplifying interaction by encapsulating SparkContext, SQLContext, and HiveContext.
- **Usage**: It is used for working with DataFrame and Dataset APIs, which provide higher-level data abstractions. SparkSession makes it easier to configure and execute Spark operations.
- **Features**: DataFrames and Datasets benefit from advanced optimizations such as the Catalyst Optimizer and Tungsten execution engine. These features typically result in better performance and easier usability compared to RDDs.
- **Recommendation**: For most modern Spark applications, especially those that do not require low-level transformations provided by RDDs, using SparkSession is advisable as it enhances code simplicity and execution efficiency.

## collect() or take(num)?

For educational purposes, I used the take() method once and the collect() method another time.

### What is `collect()`?
The `collect()` method is used to retrieve all elements of an RDD from the cluster to a single list on a local computer. It is one of the actions in Spark, meaning it triggers the computation of transformations that have been defined on the RDD.

### What is `take(num)`?
The `take(num)` method in Apache Spark is used to retrieve a specified number of items from the beginning of an RDD (Resilient Distributed Dataset), DataFrame, or Dataset. This is useful in scenarios where you need a quick preview of the contents of a large dataset, but do not want to overload local memory by processing the entire set.

### Notes on using `collect()`:
- **Scalability**: Using `collect()` is discouraged with very large datasets as it brings all data to a single node, which can lead to local memory overload and slow down the process.
- **Practical Application**: In practical, production applications, instead of `collect()`, operations like `take()`, which retrieves only a few top elements, are more commonly used, or results are saved to a file using methods such as `saveAsTextFile()`.

### Nodes on using `take(num)`
When you invoke `take(num)`, Spark performs an action that returns the first `num` elements of the dataset. Unlike the `collect()` method, which retrieves all elements of the dataset into local memory, `take(num)` limits the number of processed and returned elements, making it more efficient and less resource-intensive.
- **Preliminary data analysis**: When you start working with a large dataset and want to quickly understand its characteristics without straining resources.
- **Testing and debugging**: When you are writing and testing new Spark code, take() allows you to quickly check if the data is being processed as expected.
- **Minimizing resources**: In environments with limited resources, take() helps avoid memory overload, which is risky when using collect().

### Conclusion
- **Using the take(num) method**: I used the take(num) method in one example to quickly retrieve a small, manageable number of items from an RDD (Resilient Distributed Dataset). This method is particularly useful for educational demonstrations where the goal is to understand the data or debug the application without the overhead of loading a large dataset into memory. For instance, take(5) would retrieve the first five elements of the RDD, allowing students to see a sample of the data almost instantaneously.

- **Using the collect() method**: In a different scenario, I used the collect() method to gather all elements from the RDD to the local driver node. This approach is suitable when the dataset is small enough to fit into memory, and we want to perform operations that require access to the entire dataset. In an educational setting, collect() can be used to illustrate the results of data transformations comprehensively. However, it is also an opportunity to discuss the potential risks of memory overload and inefficiencies when working with larger datasets.