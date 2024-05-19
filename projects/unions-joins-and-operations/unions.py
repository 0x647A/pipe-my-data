# Import necessary libraries from PySpark
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("PizzaDataProcessing").getOrCreate()

# Load the CSV files into DataFrames
df1 = spark.read.csv("/datasets/pizza_data_part_aa.csv", header=True, inferSchema=True)
df2 = spark.read.csv("/datasets/pizza_data_part_ab.csv", header=True, inferSchema=True)

# Display the number of rows in each DataFrame
rows_df1 = df1.count()
rows_df2 = df2.count()

print(f"Number of rows in df1: {rows_df1}")
print(f"Number of rows in df2: {rows_df2}")

# Perform union
union_df = df1.union(df2)

# Perform unionByName
union_by_name_df = df1.unionByName(df2)

# Display the number of rows after union operations
rows_union = union_df.count()
rows_union_by_name = union_by_name_df.count()

print(f"Number of rows in union_df: {rows_union}")
print(f"Number of rows in union_by_name_df: {rows_union_by_name}")

# Stop the Spark session
spark.stop()

# Number of rows in df1: 185
# Number of rows in df2: 186
# Number of rows in union_df: 371
# Number of rows in union_by_name_df: 371
