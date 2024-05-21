# Task
#
# Return to the Netflix exercise from the previous module. 
# Add code to it that calculates the average length of a movie description 
# (counting in words or characters – your choice ;-)). Use the UDF mechanism for this.

# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
from udfs.udf_functions import DescriptionUDFs

# Initialize SparkSession
spark = SparkSession.builder.appName("NetflixMovies").getOrCreate()

# Path to the CSV file
file_path = "/dataset/netflix1.csv"

# Load data from the CSV file
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Register UDFs
count_words_udf = udf(DescriptionUDFs.count_words, IntegerType())
count_chars_udf = udf(DescriptionUDFs.count_chars, IntegerType())

# Add columns with the word and character count of the description
df = df.withColumn("word_count", count_words_udf(df["listed_in"]))
df = df.withColumn("char_count", count_chars_udf(df["listed_in"]))

# Calculate the average number of words and characters
average_word_count = df.selectExpr("avg(word_count) as avg_word_count").collect()[0]["avg_word_count"]
average_char_count = df.selectExpr("avg(char_count) as avg_char_count").collect()[0]["avg_char_count"]

print(f"Average number of words in description: {average_word_count}")
print(f"Average number of characters in description: {average_char_count}")

# Stop the Spark session
spark.stop()

# Average number of words in description: 4.453759526788761
# Average number of characters in description: 33.41986122170402
