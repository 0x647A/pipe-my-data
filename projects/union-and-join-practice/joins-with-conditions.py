# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, collect_list

# Creating SparkSession
spark = SparkSession.builder \
    .appName("Job Eligibility Example") \
    .getOrCreate()

# Defining data for the first DataFrame
data1 = [("1", "John Smith", 30),
         ("2", "Anna Johnson", 25),
         ("3", "Peter Green", 40)]

# Defining data for the second DataFrame
data2 = [("Developer", 18),
         ("President", 35),
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
# +---+------------+---+
# | id|        name|age|
# +---+------------+---+
# |  1|  John Smith| 30|
# |  2|Anna Johnson| 25|
# |  3| Peter Green| 40|
# +---+------------+---+

# Second DataFrame:
# +---------+---------+
# |      job|age_limit|
# +---------+---------+
# |Developer|       18|
# |President|       35|
# |  Senator|       30|
# +---------+---------+

# Job Eligibility with Jobs List:
# +---+------------+---+-------------------------------+
# |id |name        |age|possible_jobs                  |
# +---+------------+---+-------------------------------+
# |1  |John Smith  |30 |[Developer, Senator]           |
# |2  |Anna Johnson|25 |[Developer]                    |
# |3  |Peter Green |40 |[Developer, President, Senator]|
# +---+------------+---+-------------------------------+
