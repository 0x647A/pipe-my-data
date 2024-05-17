# Union, Join, Aggregation and Functions in PySpark

Dataset from: 
[Kaggle - Pizza Price Data](https://www.kaggle.com/datasets/knightbearr/pizza-price-prediction-real-data),
[Kaggle - Netflix Data: Cleaning, Analysis and Visualization](https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization)

## Union

**What it is:**

Union is an operation on DataFrames in PySpark that combines two or more DataFrames into one, retaining all rows from both DataFrames. The union operation does not remove duplicates; it concatenates rows in the order they appear in the input DataFrames.

**Use Case:**

Union is used when we want to combine data from two or more sources that have the same structure (the same columns). For example, we might have sales data from different months that we want to combine into a single DataFrame.

**Example:**

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("UnionExample").getOrCreate()

# Creating two DataFrames
data1 = [("Grażyna", 34), ("Henryk", 45)]
data2 = [("Teresa", 23), ("Dariusz", 30)]

df1 = spark.createDataFrame(data1, ["Name", "Age"])
df2 = spark.createDataFrame(data2, ["Name", "Age"])

# Union operation
df_union = df1.union(df2)
df_union.show()
```
**Types:**

- `union()`: Combines all rows from both DataFrames without removing duplicates.
- `unionByName()`: Similar to union, but matches columns based on names rather than order.

**Disadvantages:**

- May lead to duplicates if they are not removed after the union operation.
- Both DataFrames must have the same number of columns and the same data types.

**Advantages:**

- Simple to use when the data structure is the same.
- Efficient for combining data from similar sources.

## Join

**What it is:**

Join is an operation on DataFrames that combines two DataFrames based on a common column or columns. It is similar to the JOIN operation in SQL.

**Use Case:**

Join is used when we want to combine data from two DataFrames based on a common key. For example, we might have customer information in one DataFrame and their orders in another, and we want to combine this data to get a complete picture of transactions.

**Example:**
```python
# Creating two DataFrames
data_customers = [("Barbara", 1), ("Jan", 2)]
data_orders = [(1, "Laptop"), (2, "Phone")]

df_customers = spark.createDataFrame(data_customers, ["Name", "CustomerID"])
df_orders = spark.createDataFrame(data_orders, ["CustomerID", "Product"])

# Join operation
df_join = df_customers.join(df_orders, "CustomerID")
df_join.show()
```
**Types:**

- **Inner Join:** Returns only rows that have matching keys in both DataFrames.
- **Left Join (Left Outer Join):** Returns all rows from the left DataFrame, and matched rows from the right DataFrame.
- **Right Join (Right Outer Join):** Returns all rows from the right DataFrame, and matched rows from the left DataFrame.
- **Full Join (Full Outer Join):** Returns all rows from both DataFrames, filling in missing values with NULLs.
- **Cross Join:** Returns the Cartesian product of both DataFrames, meaning every row from the first DataFrame is combined with every row from the second DataFrame.
- **Left Semi Join:** Returns only the rows from the left DataFrame where there are matching rows in the right DataFrame.
- **Left Anti Join:** Returns only the rows from the left DataFrame where there are no matching rows in the right DataFrame.

**Disadvantages:**

- Can be computationally expensive for large datasets as it requires sorting and matching rows.
- Requires well-defined keys for effective data merging.
- Causes **data shuffling**, which is detrimental to performance. Shuffling can significantly increase processing time and memory usage, and in some cases, can lead to job failures.

**Advantages:**

- Highly flexible, allowing various types of data matching.
- Useful for data analysis when data is split across different DataFrames.

## Aggregation

Aggregation is a fundamental concept in data processing and analysis that involves combining multiple values to produce a single summary result. This process helps to derive meaningful insights from large datasets by summarizing data points into more understandable and actionable information.

### Types of Aggregation Operations

1. **Summarizations**

Aggregation often involves summarizing data through various statistical measures such as sum, average, count, maximum, and minimum. These measures provide a high-level overview of the dataset's characteristics.

   - **sum()**: Sums the values in a column.
   - **count()**: Counts the number of elements in a column.
   - **mean()**: Calculates the average value in a column.
   - **max()**: Finds the maximum value in a column.
   - **min()**: Finds the minimum value in a column.

2. **Group Aggregations**

Data can be grouped based on specific criteria (e.g., by category, date, or any other dimension). Aggregations are then performed within these groups to understand the distribution and characteristics of each group.

   - **groupBy()**: Groups rows based on one or more columns and allows aggregation functions to be applied to these groups.
   - **agg()**: Allows multiple aggregation functions to be applied to different columns simultaneously.

3. **Window Functions**

Aggregation can significantly reduce the amount of data that needs to be processed or visualized, making it easier to identify trends and patterns in large datasets.

   - **window()**: Creates time frames for calculations such as moving averages.
   - **row_number()**: Assigns a unique number to rows within each group.
   - **rank()**: Assigns a rank to rows within each group, with rows having the same value receiving the same rank.

### Examples

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, avg, max, min

# Create a Spark session
spark = SparkSession.builder.appName("AggregationExample").getOrCreate()

# Sample data
data = [("Alice", 50), ("Bob", 40), ("Alice", 45), ("Bob", 50), ("Alice", 60)]
columns = ["Name", "Score"]
df = spark.createDataFrame(data, columns)

# Summarizations
df.select(sum("Score")).show()  # Sum
df.select(count("Score")).show()  # Count
df.select(avg("Score")).show()  # Average
df.select(max("Score")).show()  # Maximum
df.select(min("Score")).show()  # Minimum

# Group Aggregations
df.groupBy("Name").agg(sum("Score").alias("TotalScore"), avg("Score").alias("AverageScore")).show()
```

### Applications

- **Business Intelligence**: Aggregation is widely used in business intelligence to generate reports and dashboards that summarize sales, revenue, customer behavior, and other key metrics.
- **Data Analysis**: Aggregates provide essential insights into trends and patterns within data, helping analysts to make informed decisions.
- **Big Data Processing**: In large-scale data environments, aggregation helps in reducing data complexity and volume, making it manageable and easier to analyze.

### Advantages

- **Simplifies Complex Data**: Aggregation simplifies large and complex datasets into digestible summaries.
- **Enables Quick Insights**: Provides a quick overview of key metrics and trends.
- **Improves Data Management**: Reduces data volume, making it easier to store, process, and analyze.

### Disadvantages

- **Loss of Detail**: Aggregating data can lead to the loss of granular details that might be important for certain analyses.
- **Potential for Misinterpretation**: Incorrect aggregation methods can lead to misleading results and interpretations.

## Function

Functions in PySpark are operations that can be applied to columns in DataFrames to transform, manipulate, and analyze data. PySpark provides a wide array of built-in functions, as well as the ability to define your own User Defined Functions (UDFs). These functions are available from the `pyspark.sql.functions` module.

### Types of Functions in PySpark

1. **Built-in Functions**:
   - PySpark offers a comprehensive set of built-in functions optimized for working with large datasets. These include aggregation functions, window functions, mathematical functions, text functions, and more.

2. **Aggregation Functions**:
   - **sum()**: Sums the values in a column.
   - **count()**: Counts the number of elements in a column.
   - **avg()**: Calculates the average value in a column.
   - **max()**: Finds the maximum value in a column.
   - **min()**: Finds the minimum value in a column.

3. **Window Functions**:
   - **row_number()**: Assigns a unique number to rows within each group.
   - **rank()**: Assigns a rank to rows within each group.
   - **dense_rank()**: Assigns a rank to rows within each group without gaps in rank values.

4. **Text Functions**:
   - **concat()**: Concatenates two or more text columns.
   - **substring()**: Extracts a substring from a text column.
   - **length()**: Returns the length of a text string.

5. **Mathematical Functions**:
   - **sqrt()**: Computes the square root of values in a column.
   - **abs()**: Computes the absolute value of a column.
   - **round()**: Rounds the value in a column to a specified number of decimal places.

6. **User Defined Functions (UDFs)**:
   - Allow you to define your own functions that can be applied to DataFrame columns. UDFs are useful when built-in functions do not meet specific requirements.

### Examples

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, max, min, udf
from pyspark.sql.types import IntegerType

# Create a Spark session
spark = SparkSession.builder.appName("FunctionExample").getOrCreate()

# Sample data
data = [("Alina", 50), ("Andrzej", 40), ("Alina", 45), ("Andrzej", 50), ("Alina", 60)]
columns = ["Name", "Score"]
df = spark.createDataFrame(data, columns)

# Aggregation functions
df.select(sum("Score")).show()  # Sum
df.select(avg("Score")).show()  # Average
df.select(max("Score")).show()  # Maximum
df.select(min("Score")).show()  # Minimum

# User Defined Function (UDF)
def increment(value):
    return value + 10

increment_udf = udf(lambda x: increment(x), IntegerType())

df.withColumn("IncrementedScore", increment_udf(col("Score"))).show()
```

### Applications

- **Data Transformation:** Functions are crucial for transforming data into the desired format or structure.
- **Data Analysis:** Enable advanced analyses and computations on large datasets.
- **Data Cleaning:** Assist in identifying and removing erroneous or incomplete data.

### Advantages

- **Performance:** PySpark's built-in functions are optimized for large-scale data processing in a distributed environment.
- **Flexibility:** Ability to create custom user-defined functions tailored to specific needs.
- **Ease of Use:** Simple integration and application of functions to DataFrames in PySpark.

### Disadvantages

- **Complexity:** Defining complex UDFs can be challenging and may require advanced programming knowledge.
- **UDF Performance:** UDFs can be less efficient than built-in functions, especially when applied at scale.
