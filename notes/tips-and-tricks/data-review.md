# Initial Data Review

At the very beginning of working with data, the most crucial step is reviewing the available data. Data review is a key step that allows us to understand the structure, quality, and content of the data. This enables us to:

1. **Understand Data Structure**: We get to know the columns, data types, and relationships between them, which is essential for further analysis.
2. **Identify Missing and Erroneous Data**: We can find missing values, duplicates, and potential errors, allowing for their early removal or consideration in the analysis.
3. **Determine Data Distribution**: Statistical analysis helps us understand data distribution, which is important for selecting appropriate analysis methods.
4. **Detect Anomalies**: Identifying anomalies helps us understand if the data is representative and if it requires special treatment.
5. **Plan the Analysis**: Reviewing the data helps us better plan the next analytical steps, including the selection of appropriate methods and tools.

## Examples of Data Review in PySpark

### 1. **Loading Data**
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataReview").getOrCreate()
df = spark.read.csv("path_to_file.csv", header=True, inferSchema=True)
```
Loading data from a CSV file into a PySpark DataFrame. The options header=True and inferSchema=True ensure that the first row is treated as column headers and that data types are automatically determined.

### 2. **Displaying Schema**
```python
df.printSchema()
```
Displaying the structure of the DataFrame, including column names and their data types. This helps understand what data is available and how it is organized.

### 3. **Data Preview**
```python
df.show(5)
```
Displaying the first 5 rows of the DataFrame. This provides a quick preview of the data content and checks if the data was correctly loaded.

### 4. **Basic Statistics**
```python
df.describe().show()
```
Displaying basic statistics (such as count, mean, standard deviation, min, and max) for all numeric columns in the DataFrame. This helps in quickly understanding the data distribution.

### 5. **Counting Unique Values**
```python
df.groupBy("column_name").count().show()
```
Counting unique values in a selected column. This helps understand the diversity of data in a particular column and detect potential issues like duplicates.

### 6. **Finding Missing Values**
```python
from pyspark.sql.functions import col, sum

df.select([sum(col(c).isNull().cast("int")).alias(c) for c in df.columns]).show()
```
Counting missing values in each column. This helps identify columns with a large number of missing data, which may require cleaning or imputation.

### 7. **Displaying Distribution of Categorical Data**
```python
df.groupBy("categorical_column").count().orderBy("count", ascending=False).show()
```
Displaying the distribution of data in categorical columns. This helps understand how often each category occurs, which can be crucial for further analysis.

## Summary
Reviewing data at the beginning of a project is an essential step that allows for a better understanding of the available data and the identification of potential issues. 