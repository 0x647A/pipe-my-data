# Common Data Formats

## 1. CSV (Comma-Separated Values)

**CSV** is a simple text format for tabular data where each line corresponds to a row and columns are separated by commas.

Example:

```csv
Name,Age,Occupation
Alice,30,Engineer
Bob,25,Data Scientist
Carol,28,Designer
```

## 2. JSON (JavaScript Object Notation)

**JSON** is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It represents data as key-value pairs.

Example:

```json
[
  {
    "Name": "Alice",
    "Age": 30,
    "Occupation": "Engineer"
  },
  {
    "Name": "Bob",
    "Age": 25,
    "Occupation": "Data Scientist"
  },
  {
    "Name": "Carol",
    "Age": 28,
    "Occupation": "Designer"
  }
]
```

## 3. Parquet

**Parquet** is a columnar storage file format optimized for use with data processing frameworks. It provides efficient data compression and encoding schemes to handle complex data.

Example:

Parquet files are binary and not human-readable. Below is an illustration of how data might be structured in a Parquet file:

```diff
+-------+-----+--------------+
|  Name | Age |  Occupation  |
+-------+-----+--------------+
| Alice |  30 | Engineer     |
|  Bob  |  25 | Data Scientist|
| Carol |  28 | Designer     |
+-------+-----+--------------+
```

## 4. Avro

**Avro** is a row-oriented remote procedure call and data serialization framework developed within Apache's Hadoop project. It uses JSON for defining data types and protocols, and serialized data is in a compact binary format.

Example:

An Avro schema and corresponding data example:

Schema (in JSON):

```json
{
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "Name", "type": "string"},
    {"name": "Age", "type": "int"},
    {"name": "Occupation", "type": "string"}
  ]
}
```

Data (binary, not human-readable):

```json
{ "Name": "Alice", "Age": 30, "Occupation": "Engineer" }
{ "Name": "Bob", "Age": 25, "Occupation": "Data Scientist" }
{ "Name": "Carol", "Age": 28, "Occupation": "Designer" }
```

## 5. ORC (Optimized Row Columnar)

**ORC** is a columnar storage file format optimized for Hadoop workloads. It offers high compression and improved performance for reading and writing operations.

Example:

ORC files are also binary and not human-readable. An example representation:

```diff
+-------+-----+--------------+
|  Name | Age |  Occupation  |
+-------+-----+--------------+
| Alice |  30 | Engineer     |
|  Bob  |  25 | Data Scientist|
| Carol |  28 | Designer     |
+-------+-----+--------------+
```

## 6. XML (eXtensible Markup Language)

**XML** is a markup language that defines rules for encoding documents in a format that is both human-readable and machine-readable. It is used to represent complex data structures.

Example:

```xml
<Employees>
  <Employee>
    <Name>Alice</Name>
    <Age>30</Age>
    <Occupation>Engineer</Occupation>
  </Employee>
  <Employee>
    <Name>Bob</Name>
    <Age>25</Age>
    <Occupation>Data Scientist</Occupation>
  </Employee>
  <Employee>
    <Name>Carol</Name>
    <Age>28</Age>
    <Occupation>Designer</Occupation>
  </Employee>
</Employees>
```

### Summary

Each of these formats has its own use cases and advantages:

- **CSV**: Simple and easy to use, but lacks support for complex data types.
- **JSON**: Great for APIs and web applications, supports nested structures.
- **Parquet**: Efficient for analytical queries, supports complex data types.
- **Avro**: Good for data serialization, compact binary format.
- **ORC**: Optimized for Hadoop, provides efficient storage and retrieval.
- **XML**: Flexible and self-describing, suitable for hierarchical data.

# Methods for reading and writing data from files in PySpark

In PySpark, the operations of reading from and writing to files are essential for data processing. PySpark supports many file formats, including CSV, JSON, Parquet, Avro, and more.

## Reading data from a file

1. **CSV**

```python
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("ReadCSVExample").getOrCreate()

# Read data from a CSV file
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Display a few rows from the DataFrame
df.show()
```
### Explanation:

- `header=True`: This option indicates that the first row of the CSV file contains the column names.
- `inferSchema=True`: This option tells PySpark to automatically infer the data types of the columns based on the data.

2. **JSON**

```python
# Read data from a JSON file
df = spark.read.json("path/to/file.json")

# Display a few rows from the DataFrame
df.show()
```

3. **Parquet**

```python
# Read data from a Parquet file
df = spark.read.parquet("path/to/file.parquet")

# Display a few rows from the DataFrame
df.show()
```
4. **Avro**

```python
# Add support for the Avro format (requires the avro package to be installed)
df = spark.read.format("avro").load("path/to/file.avro")

# Display a few rows from the DataFrame
df.show()
```

## Writing Data to a File

1. **CSV**

```python
# Write DataFrame to a CSV file
df.write.csv("path/to/output.csv", header=True)
```
2. **JSON**

```python
# Write DataFrame to a JSON file
df.write.json("path/to/output.json")
```

3. **Parquet**

```python
# Write DataFrame to a Parquet file
df.write.parquet("path/to/output.parquet")
```

4. **Avro**

```python
# Add support for the Avro format (requires the avro package to be installed)
df.write.format("avro").save("path/to/output.avro")
```

### Additional options for reading and writing

When reading and writing data, PySpark offers many additional options. For example:

- **Separator (for CSV)**

```python
df = spark.read.option("sep", ";").csv("path/to/file.csv", header=True)
```

- **Multiple Files**

```python
df = spark.read.csv(["path/to/file1.csv", "path/to/file2.csv"], header=True)
```

- **Mode** (for writing: append, overwrite, error, ignore)

```python
df.write.mode("overwrite").csv("path/to/output.csv", header=True)
```

- **Compression** (for writing)

```python
df.write.option("compression", "gzip").csv("path/to/output.csv", header=True)
```

### Full Example

Below is a full example showing how to read data from a CSV file, process the data, and write it to a Parquet file:

``` python
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("FullExample").getOrCreate()

# Read data from a CSV file
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Process the data (example transformation)
df_filtered = df.filter(df["column_name"] > 100)

# Write the processed data to a Parquet file
df_filtered.write.parquet("path/to/output.parquet")

# Stop the Spark session
spark.stop()
```

The methods for reading and writing data in PySpark are versatile and allow for easy manipulation of large datasets, which is crucial in Big Data processing.