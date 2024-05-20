# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType, StructType, StructField, IntegerType
from udfs.initials_udf import InitialsUDF

# Creating a Spark session
spark = SparkSession.builder \
    .appName("Apply initials UDF") \
    .getOrCreate()

# Create an object
initialsUDF = InitialsUDF()

# Registering the UDF
get_initials_udf = udf(initialsUDF.get_initials, StringType())
spark.udf.register("get_initials", initialsUDF.get_initials, StringType())

# Data
data = [
    (1, "Jan", "Kowalski", 30),
    (2, "Anna", "Nowak", 25),
    (3, "Piotr", "Zielinski", 40),
    (4, "Katarzyna", "Wójcik", 35)
]

# Schema definition
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("surname", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Creating DataFrame
df = spark.createDataFrame(data, schema)

# Applying the UDF
df_with_initials = df.withColumn("initials", get_initials_udf(col("name"), col("surname")))
df_with_initials.show()

# +---+---------+---------+---+--------+
# | id|     name|  surname|age|initials|
# +---+---------+---------+---+--------+
# |  1|      Jan| Kowalski| 30|      JK|
# |  2|     Anna|    Nowak| 25|      AN|
# |  3|    Piotr|Zielinski| 40|      PZ|
# |  4|Katarzyna|   Wójcik| 35|      KW|
# +---+---------+---------+---+--------+
