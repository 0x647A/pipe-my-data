# UDF and the `transform` function in PySpark

The dataset from: 
[Kaggle - Netflix Data: Cleaning, Analysis and Visualization](https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization)

## User-Defined Functions (UDF)

### What is an UDF?
User-Defined Functions (UDF) are custom functions defined by the user that allow for performing non-standard operations on data in a PySpark DataFrame. UDFs enable using Python functions directly in Spark queries.

### Example Syntax
To create, register, and invoke an UDF in PySpark, follow these steps:

1. **Create the function**: Define the Python function that will be your UDF.
2. **Register the UDF**: Register the function as an UDF, specifying the return type.
3. **Invoke the UDF**: Use the registered UDF in a Spark query.

Example:
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

# Create SparkSession
spark = SparkSession.builder.appName("UDF Example").getOrCreate()

# Example Python function
def square(x):
    return x * x

# Register the UDF
square_udf = udf(square, IntegerType())

# Create DataFrame
data = [(1,), (2,), (3,)]
df = spark.createDataFrame(data, ["value"])

# Use the UDF in the DataFrame
df.withColumn('squared', square_udf(df['value'])).show()
```
### Ways to Create UDFs: Class-Based and Lambda

In PySpark, you can create UDFs using two methods: 

- **class-based functions**:
```python
# Define class-based function
def multiply_by_two(x):
    return x * 2

# Register the UDF
multiply_by_two_udf = udf(multiply_by_two, IntegerType())

# Use the UDF
df.withColumn('doubled', multiply_by_two_udf(df['value'])).show()
```
- **lambda functions**:
```python
# Register the UDF using a lambda function
add_one_udf = udf(lambda x: x + 1, IntegerType())

# Use the UDF
df.withColumn('incremented', add_one_udf(df['value'])).show()
```

### When to Use UDFs?

UDFs are used when you need to perform custom operations on data that are not available in PySpark's built-in functions. Examples include:

- Custom text processing.
- Mathematical operations not supported by built-in functions.
- Data processing that requires specific business logic.

### Advantages and Disadvantages of UDFs

#### Advantages:

- Flexibility in defining custom operations.
- Ability to use complex business logic.

#### Disadvantages:

- Lower performance compared to built-in Spark functions as UDFs are not optimized.
- Lack of support for vectorized operations, which can lead to lower efficiency in processing large datasets.
- Serialization difficulties with Python functions across the Spark cluster.

### Types of UDFs in PySpark

In PySpark, there are different types of UDFs depending on the data types and usage context:

- **Scalar UDF**: Operates on individual values and returns a single value.
- **Grouped Aggregate UDF**: Operates on groups of data and returns one value per group.
- **Pandas UDF**: Utilizes the Pandas library for vectorized operations, allowing for more efficient data processing.

## `transform()`

### What is the transform Function?

The `transform()` function in PySpark is used to apply a function to each element in an array column. It is a high-level expression that simplifies working with arrays in DataFrames. Additionally, the `transform()` function allows for chaining custom transformations, making it easier to apply multiple operations in sequence.

### Example Syntax

To use the `transform()` function, import it from the pyspark.sql.functions module:

```python
from pyspark.sql.functions import transform

# Example DataFrame with an array column
df = spark.createDataFrame([([1, 2, 3],), ([4, 5, 6],)], ['data'])

# Apply the transform function to the 'data' column
df.withColumn('transformed_data', transform('data', lambda x: x + 1)).show()

# Chaining multiple transformations
df.withColumn('transformed_data', transform('data', lambda x: x + 1)) \
  .withColumn('transformed_data', transform('transformed_data', lambda x: x * 2)).show()
```
### When to Use the transform Function?

The `transform()` function is used when you need to perform operations on each element in an array column. Examples include:

- Transforming each element of an array according to specific logic.
- Filtering and mapping data within arrays.
- Chaining multiple transformations to apply a sequence of operations on array elements.

### Advantages and Disadvantages of the `transform()` Function

#### Advantages:

- Simplifies operations on arrays without needing to explode them into individual rows.
- Better performance compared to using UDFs since it is optimized for vectorized operations.
- Allows chaining custom transformations, making it easier to manage complex transformation logic.

#### Disadvantages:

- Limited to operations on array columns.
- May be less intuitive for users unfamiliar with higher-order functions in PySpark.

## Additional - `@staticmethod`

### TLTR
`@staticmethod` - Decorator indicating that the following method is static and does not require an instance of the class to be called.

Using the `@staticmethod` decorator in Python provides a way to define methods that belong to a class but do not require access to any instance-specific data (i.e., they do not require self). 

### Why Use `@staticmethod`?

- **No Instance Dependency**: Static methods do not require access to instance variables or methods. They are independent and can be called on the class itself, not needing an instance of the class. This makes it clear that the method does not modify the state of the instance.

- **Namespace Organization**: Using static methods helps organize related functions under a class namespace, making the code more modular and readable. It indicates that these functions logically belong to the class but do not depend on instance-specific data.

- **Code Clarity**: By using @staticmethod, you make it explicit that these methods are utility functions that do not alter or rely on the instance state. This improves the readability and maintainability of the code.

- **But seriously, I used it just to practice it :)**

### How to Use @staticmethod

To use `@staticmethod`, you simply decorate the method inside the class with `@staticmethod`. 

- **With `@staticmethod`**: You can call methods without creating an instance of the class. The methods are directly assigned to the class.
- **Without `@staticmethod`**: You need to create an instance of the class to call its methods. The methods must take self as the first argument.

Using `@staticmethod` simplifies the code if the method does not need access to instance data. In our case, the functions `count_words` and `count_chars` do not need access to instance data, so using `@staticmethod` is more appropriate.
