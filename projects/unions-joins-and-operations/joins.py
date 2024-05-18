# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Creating SparkSession
spark = SparkSession.builder \
    .appName("DataFrame Join Examples") \
    .getOrCreate()

# Defining data for the first DataFrame
data1 = [("1", "Jan Kowalski", 30),
         ("2", "Anna Nowak", 25),
         ("3", "Piotr Zielinski", 40)]

# Defining data for the second DataFrame
data2 = [("1", "Developer"),
         ("2", "Analyst"),
         ("4", "Manager")]

# Defining schemas
schema1 = ["id", "name", "age"]
schema2 = ["id", "job"]

# Creating DataFrames
df1 = spark.createDataFrame(data1, schema1)
df2 = spark.createDataFrame(data2, schema2)

# Displaying DataFrames using the show method
print("First DataFrame:")
df1.show()

print("Second DataFrame:")
df2.show()

# Performing joins
inner_join = df1.join(df2, df1.id == df2.id, "inner")
left_join = df1.join(df2, df1.id == df2.id, "left")
right_join = df1.join(df2, df1.id == df2.id, "right")
full_join = df1.join(df2, df1.id == df2.id, "outer")
cross_join = df1.crossJoin(df2)
semi_join = df1.join(df2, df1.id == df2.id, "leftsemi")
anti_join = df1.join(df2, df1.id == df2.id, "leftanti")

# Displaying the results of the joins
print("Inner Join:")
inner_join.show()

print("Left Join:")
left_join.show()

print("Right Join:")
right_join.show()

print("Full Join:")
full_join.show()

print("Cross Join:")
cross_join.show()

print("Semi Join:")
semi_join.show()

print("Anti Join:")
anti_join.show()

# Stopping the SparkSession
spark.stop()

# First DataFrame:
# +---+---------------+---+
# | id|           name|age|
# +---+---------------+---+
# |  1|   Jan Kowalski| 30|
# |  2|     Anna Nowak| 25|
# |  3|Piotr Zielinski| 40|
# +---+---------------+---+

# Second DataFrame:
# +---+---------+
# | id|      job|
# +---+---------+
# |  1|Developer|
# |  2|  Analyst|
# |  4|  Manager|
# +---+---------+

# Inner Join:
# +---+------------+---+---+---------+
# | id|        name|age| id|      job|
# +---+------------+---+---+---------+
# |  1|Jan Kowalski| 30|  1|Developer|
# |  2|  Anna Nowak| 25|  2|  Analyst|
# +---+------------+---+---+---------+

# Left Join:
# +---+---------------+---+----+---------+
# | id|           name|age|  id|      job|
# +---+---------------+---+----+---------+
# |  1|   Jan Kowalski| 30|   1|Developer|
# |  2|     Anna Nowak| 25|   2|  Analyst|
# |  3|Piotr Zielinski| 40|NULL|     NULL|
# +---+---------------+---+----+---------+

# Right Join:
# +----+------------+----+---+---------+
# |  id|        name| age| id|      job|
# +----+------------+----+---+---------+
# |   1|Jan Kowalski|  30|  1|Developer|
# |   2|  Anna Nowak|  25|  2|  Analyst|
# |NULL|        NULL|NULL|  4|  Manager|
# +----+------------+----+---+---------+

# Full Join:
# +----+---------------+----+----+---------+
# |  id|           name| age|  id|      job|
# +----+---------------+----+----+---------+
# |   1|   Jan Kowalski|  30|   1|Developer|
# |   2|     Anna Nowak|  25|   2|  Analyst|
# |   3|Piotr Zielinski|  40|NULL|     NULL|
# |NULL|           NULL|NULL|   4|  Manager|
# +----+---------------+----+----+---------+

# Cross Join:
# +---+---------------+---+---+---------+
# | id|           name|age| id|      job|
# +---+---------------+---+---+---------+
# |  1|   Jan Kowalski| 30|  1|Developer|
# |  1|   Jan Kowalski| 30|  2|  Analyst|
# |  1|   Jan Kowalski| 30|  4|  Manager|
# |  2|     Anna Nowak| 25|  1|Developer|
# |  2|     Anna Nowak| 25|  2|  Analyst|
# |  2|     Anna Nowak| 25|  4|  Manager|
# |  3|Piotr Zielinski| 40|  1|Developer|
# |  3|Piotr Zielinski| 40|  2|  Analyst|
# |  3|Piotr Zielinski| 40|  4|  Manager|
# +---+---------------+---+---+---------+

# Semi Join:
# +---+------------+---+
# | id|        name|age|
# +---+------------+---+
# |  1|Jan Kowalski| 30|
# |  2|  Anna Nowak| 25|
# +---+------------+---+

# Anti Join:
# +---+---------------+---+
# | id|           name|age|
# +---+---------------+---+
# |  3|Piotr Zielinski| 40|
# +---+---------------+---+
