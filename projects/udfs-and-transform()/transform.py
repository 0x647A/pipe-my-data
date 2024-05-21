# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Create SparkSession
spark = SparkSession.builder \
    .appName("GenerateData") \
    .getOrCreate()

# Generate data
data = [
    (1, "Jan", "Kowalski", 20),
    (2, "Anna", "Nowak", 17),
    (3, "Piotr", "Wiśniewski", 25),
    (4, "Maria", "Wójcik", 15)
]

# Create DataFrame
columns = ["id", "first_name", "last_name", "age"]
df = spark.createDataFrame(data, schema=columns)

# Define the isAdult function
def isAdult(df):
    return df.withColumn('isAdult', when(col("age") >= 18, "T").otherwise("F"))

# Apply the function using transform
df_final = df.transform(isAdult)

# Show the result
df_final.show()

# Stop Spark session
spark.stop()

# +---+----------+----------+---+-------+
# | id|first_name| last_name|age|isAdult|
# +---+----------+----------+---+-------+
# |  1|       Jan|  Kowalski| 20|      T|
# |  2|      Anna|     Nowak| 17|      F|
# |  3|     Piotr|Wiśniewski| 25|      T|
# |  4|     Maria|    Wójcik| 15|      F|
# +---+----------+----------+---+-------+
