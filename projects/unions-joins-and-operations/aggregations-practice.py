# Task

# Use the file containing data about pizzerias in the USA to determine
# the maximum, minimum, and average price of a medium pizza.

# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max, min, avg, regexp_replace, trim

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PizzaPriceAnalysis") \
    .getOrCreate()

# Load data from CSV file
file_path = "pizza_data.csv"
pizza_df = spark.read.csv(file_path, header=True, inferSchema=True)

# View the schema of the data
pizza_df.printSchema()

# Display a few rows
pizza_df.show(5)

# Clean up the 'Size' column to remove extra spaces and quotes
pizza_df = pizza_df.withColumn('Size', trim(regexp_replace(col('Size'), '[^a-zA-Z0-9\s]', '')))

# Remove dollar sign and convert 'Price' to float
pizza_df = pizza_df.withColumn('Price', regexp_replace(col('Price'), '[$]', '').cast('float'))

# Verify the data after conversion
pizza_df.show(5)

# Filter only medium pizzas
medium_pizza_df = pizza_df.filter(col('Size').contains('Medium'))

# Check if there are any medium pizzas in the filtered data
medium_pizza_count = medium_pizza_df.count()
print(f"Number of medium pizzas: {medium_pizza_count}")

if medium_pizza_count > 0:
    # Calculate maximum price
    max_price = medium_pizza_df.select(max(col('Price'))).collect()[0][0]

    # Calculate minimum price
    min_price = medium_pizza_df.select(min(col('Price'))).collect()[0][0]

    # Calculate average price
    avg_price = medium_pizza_df.select(avg(col('Price'))).collect()[0][0]

    print(f"Maximum price of medium pizzas: {max_price}")
    print(f"Minimum price of medium pizzas: {min_price}")
    print(f"Average price of medium pizzas: {avg_price}")
else:
    print("No medium pizzas found in the dataset.")

# Stop Spark session
spark.stop()
