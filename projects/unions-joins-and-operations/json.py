# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

# Initialize Spark session
spark = SparkSession.builder.appName("Nested JSON to DataFrame").getOrCreate()

# Create a list with nested JSON data
data = [
    '{"name": "Genowefa", "time": "2023-05-18 10:00:00"}',
    '{"name": "Artur", "time": "2023-05-18 11:00:00"}',
    '{"name": "Krzysztof", "time": "2023-05-18 12:00:00"}'
]

# Load data into a DataFrame with a `value` column
nested_df = spark.createDataFrame(data, "string").toDF("value")

# Display the contents of the DataFrame
nested_df.show(truncate=False)

# Define the JSON schema
schema = StructType([
    StructField("name", StringType(), True),
    StructField("time", StringType(), True)
])

# Transform the `value` column into separate `name` and `time` columns
json_df = nested_df.withColumn("jsonData", from_json(col("value"), schema)) \
                   .select("jsonData.*")

# Convert the `time` column to TimestampType
json_df = json_df.withColumn("time", col("time").cast(TimestampType()))

# Display the contents of the DataFrame
json_df.show(truncate=False)

# Display the schema of the DataFrame
json_df.printSchema()

# +----------------------------------------------------+
# |value                                               |
# +----------------------------------------------------+
# |{"name": "Genowefa", "time": "2023-05-18 10:00:00"} |
# |{"name": "Artur", "time": "2023-05-18 11:00:00"}    |
# |{"name": "Krzysztof", "time": "2023-05-18 12:00:00"}|
# +----------------------------------------------------+

# +---------+-------------------+
# |name     |time               |
# +---------+-------------------+
# |Genowefa |2023-05-18 10:00:00|
# |Artur    |2023-05-18 11:00:00|
# |Krzysztof|2023-05-18 12:00:00|
# +---------+-------------------+

# root
#  |-- name: string (nullable = true)
#  |-- time: timestamp (nullable = true)
