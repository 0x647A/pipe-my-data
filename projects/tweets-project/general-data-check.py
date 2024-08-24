from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("CSV to DataFrame") \
    .getOrCreate()

# Load data from CSV files into DataFrames
covid_tweets_df = spark.read.csv("datasets/covid_tweets_anglais.csv", header=True, inferSchema=True)
grammys_tweets_df = spark.read.csv("datasets/GRAMMYs_tweets.csv", header=True, inferSchema=True)
stockerbot_df = spark.read.csv("datasets/stockerbot-export.csv", header=True, inferSchema=True)

# Display data and schema for each DataFrame
print("COVID Tweets DataFrame:")
covid_tweets_df.show()
covid_tweets_df.printSchema()

print("GRAMMYs Tweets DataFrame:")
grammys_tweets_df.show()
grammys_tweets_df.printSchema()

print("Stockerbot DataFrame:")
stockerbot_df.show()
stockerbot_df.printSchema()

# Stop the Spark session
spark.stop()
