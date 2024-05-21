# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType, StringType, StructType, StructField, IntegerType
from compound_interest_udf import CompoundInterestUDF

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Apply compound interest UDF") \
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
    StructField("interest", DoubleType(), True)
])

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Apply UDF for fixed periods 10, 20, 30, 60 years
df_with_interest = df \
    .withColumn("interest_10_years", calculate_compound_interest_udf(col("money"), col("interest"), udf(lambda: 10, IntegerType())())) \
    .withColumn("interest_20_years", calculate_compound_interest_udf(col("money"), col("interest"), udf(lambda: 20, IntegerType())())) \
    .withColumn("interest_30_years", calculate_compound_interest_udf(col("money"), col("interest"), udf(lambda: 30, IntegerType())())) \
    .withColumn("interest_60_years", calculate_compound_interest_udf(col("money"), col("interest"), udf(lambda: 60, IntegerType())()))

# Show results
df_with_interest.show()

# Stop Spark session
spark.stop()

# +---+---------+---------+------+--------+------------------+------------------+------------------+------------------+
# | id|     name|  surname| money|interest| interest_10_years| interest_20_years| interest_30_years| interest_60_years|
# +---+---------+---------+------+--------+------------------+------------------+------------------+------------------+
# |  1|      Jan| Kowalski|1000.0|    0.05| 1628.894626777442|2653.2977051444223| 4321.942375150667|18679.185894122995|
# |  2|     Anna|    Nowak|1500.0|    0.04|2220.3664273775166| 3286.684714550131| 4865.096265041312|15779.441112079283|
# |  3|    Piotr|Zielinski|2000.0|    0.03|2687.8327586882447|  3612.22246933883| 4854.524942379325|11783.206208091493|
# |  4|Katarzyna|   Wójcik|2500.0|    0.06| 4477.119241357136|  8017.83868053212|14358.727932283145| 82469.22713333131|
# +---+---------+---------+------+--------+------------------+------------------+------------------+------------------+
