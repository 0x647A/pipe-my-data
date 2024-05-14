# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session for processing
spark = SparkSession.builder \
    .appName("MMA Players Analysis") \
    .getOrCreate()

# Load the CSV file into a DataFrame
mma_df = spark.read.csv('dataset/pro_mma_fighters.csv', header=True, inferSchema=True)

# Group the data by the 'country' column and count the number of MMA players in each country
country_count = mma_df.groupBy("country").count()

# Sort the results by the count in descending order to get the countries with the most MMA players on top
sorted_country_count = country_count.orderBy(col("count").desc())

# Display the results. You can specify the number of rows to display within the show() method
sorted_country_count.show()

# Stop the Spark session to free up resources after the computation is finished
spark.stop()

# Results
# +-------------+-----+
# |      country|count|
# +-------------+-----+
# |United States| 2821|
# |       Brazil|  403|
# |      England|  181|
# |        China|  175|
# |        Japan|  145|
# |       Canada|  128|
# |       Russia|  120|
# |    Australia|   64|
# |  Philippines|   60|
# |       Israel|   55|
# |       France|   54|
# |  South Korea|   52|
# |    Indonesia|   51|
# |      Ireland|   39|
# |       Mexico|   39|
# |     Malaysia|   38|
# |       Poland|   37|
# |      Myanmar|   33|
# |        Italy|   32|
# |       Sweden|   30|
# +-------------+-----+
# only showing top 20 rows
