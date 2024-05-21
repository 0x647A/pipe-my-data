# Task

# Modify the UDF used for interest capitalization so that it can accept an additional value 
# (Int) in the form of annual savings contributions, and then conduct several simulations.

# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType, StringType, StructType, StructField, IntegerType
from compound_interest_udf import CompoundInterestUDF

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Apply compound interest UDF with contributions") \
    .getOrCreate()

# Create an object
compound_interest_UDF = CompoundInterestUDF()

# Register the UDF
calculate_compound_interest_udf = udf(compound_interest_UDF.calculate_compound_interest, DoubleType())
spark.udf.register("calculate_compound_interest", compound_interest_UDF.calculate_compound_interest, DoubleType())

# Data
data = [
    (1, "Jan", "Kowalski", 1000.0, 0.05),
    (2, "Anna", "Nowak", 1500.0, 0.04),
    (3, "Piotr", "Zielinski", 2000.0, 0.03),
    (4, "Katarzyna", "Wójcik", 2500.0, 0.06)
]

# Schema definition
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("surname", StringType(), True),
    StructField("money", DoubleType(), True),
    StructField("interest", DoubleType(), True),
    StructField("annual_contribution", IntegerType(), True)
])

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Apply UDF for fixed periods 10, 20, 30, 60 years with annual contributions
df_with_interest = df \
    .withColumn("interest_10_years", calculate_compound_interest_udf(col("money"), col("interest"), udf(lambda: 10, IntegerType())(), col("annual_contribution"))) \
    .withColumn("interest_20_years", calculate_compound_interest_udf(col("money"), col("interest"), udf(lambda: 20, IntegerType())(), col("annual_contribution"))) \
    .withColumn("interest_30_years", calculate_compound_interest_udf(col("money"), col("interest"), udf(lambda: 30, IntegerType())(), col("annual_contribution"))) \
    .withColumn("interest_60_years", calculate_compound_interest_udf(col("money"), col("interest"), udf(lambda: 60, IntegerType())(), col("annual_contribution")))

# Show results
df_with_interest.show()

# Stop Spark session
spark.stop()

# +---+---------+---------+------+--------+-------------------+------------------+------------------+------------------+------------------+
# | id|     name|  surname| money|interest|annual_contribution| interest_10_years| interest_20_years| interest_30_years| interest_60_years|
# +---+---------+---------+------+--------+-------------------+------------------+------------------+------------------+------------------+
# |  1|      Jan| Kowalski|1000.0|    0.05|                100| 2949.573343010069| 6125.222885947707|11298.021362967065| 55805.47627178125|
# |  2|     Anna|    Nowak|1500.0|    0.04|                200| 4717.636708952906| 9480.525058323914| 16530.76331718452|65281.503633954104|
# |  3|    Piotr|Zielinski|2000.0|    0.03|                300|   6230.1714659327|11915.168186433793|19555.328395632838| 62166.71817976263|
# |  4|Katarzyna|   Wójcik|2500.0|    0.06|                400|10065.776296926635| 23614.92935083623|  47879.3988875368| 308515.5758302141|
# +---+---------+---------+------+--------+-------------------+------------------+------------------+------------------+------------------+
