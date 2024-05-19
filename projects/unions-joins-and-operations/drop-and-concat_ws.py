# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat_ws, monotonically_increasing_id

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PySparkExample") \
    .getOrCreate()

# Generate sample data
data = [("Jan", "Laputak", 25),
        ("Ania", "Kowalski", 17),
        ("Tomek", "Nowakowski", 34),
        ("Katarzyna", "Kowalska", 19),
        ("Marek", "Nowak", 16)]

# Create DataFrame
columns = ["first_name", "last_name", "age"]
df = spark.createDataFrame(data, columns)

# Add an id column
df = df.withColumn("id", monotonically_increasing_id())

# Combine first name and last name columns into one column
df = df.withColumn("full_name", concat_ws(" ", col("first_name"), col("last_name")))

# Drop the first_name and last_name columns
df = df.drop("first_name", "last_name")

# Filter adults (age >= 18)
adults_df = df.filter(col("age") >= 18)

# Reorder columns: id, full_name, age
final_df = adults_df.select("id", "full_name", "age")

# Show results
final_df.show()

# Stop Spark session
spark.stop()

# +-----------+------------------+---+
# |         id|         full_name|age|
# +-----------+------------------+---+
# | 8589934592|       Jan Laputak| 25|
# |34359738368|  Tomek Nowakowski| 34|
# |51539607552|Katarzyna Kowalska| 19|
# +-----------+------------------+---+
