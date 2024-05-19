# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, collect_list

# Creating SparkSession
spark = SparkSession.builder \
    .appName("Job Eligibility Example") \
    .getOrCreate()

# Defining data for the first DataFrame
data1 = [("1", "Janusz Grażyniak", 30),
         ("2", "Anna Czkawka", 25),
         ("3", "Piotr Ziółkowski", 40)]

# Defining data for the second DataFrame
data2 = [("Programista", 18),
         ("Prezydent", 35),
         ("Senator", 30)]

# Defining schemas
schema1 = ["id", "name", "age"]
schema2 = ["job", "age_limit"]

# Creating DataFrames
df1 = spark.createDataFrame(data1, schema1)
df2 = spark.createDataFrame(data2, schema2)

# Displaying DataFrames using the show method
print("First DataFrame:")
df1.show()

print("Second DataFrame:")
df2.show()

# Performing join to see which jobs these people are eligible for
job_eligibility = df1.crossJoin(df2).filter(df1.age >= df2.age_limit)

# Grouping possible jobs into a list for each person
jobs_list = job_eligibility.groupBy("id") \
    .agg(collect_list("job").alias("possible_jobs"))

# Displaying the results
print("Job Eligibility with Jobs List:")
jobs_list.show(truncate=False)

# Stopping the SparkSession
spark.stop()

# First DataFrame:
# +---+----------------+---+
# | id|            name|age|
# +---+----------------+---+
# |  1|Janusz Grażyniak| 30|
# |  2|    Anna Czkawka| 25|
# |  3|Piotr Ziółkowski| 40|
# +---+----------------+---+

# Second DataFrame:
# +-----------+---------+
# |        job|age_limit|
# +-----------+---------+
# |Programista|       18|
# |  Prezydent|       35|
# |    Senator|       30|
# +-----------+---------+

# Job Eligibility with Jobs List:
# +---+---------------------------------+
# |id |possible_jobs                    |
# +---+---------------------------------+
# |1  |[Programista, Senator]           |
# |2  |[Programista]                    |
# |3  |[Programista, Prezydent, Senator]|
# +---+---------------------------------+
