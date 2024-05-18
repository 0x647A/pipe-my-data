# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col, avg, sum, count

# Create a Spark session
spark = SparkSession.builder.appName("Pizza Analysis").getOrCreate()

# Load the CSV file into a DataFrame
file_path = '/datasets/pizza_data.csv'  # Update this to the correct path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Show the DataFrame and its schema
df.show()
df.printSchema()

# Remove the '$' sign from the Price column and cast it to DoubleType
df = df.withColumn('Price', regexp_replace(col('Price'), '\\$', '').cast('double'))

df.show()
df.printSchema()

# Calculate average price, total price, and count of pizzas per company
result = df.groupBy('Company').agg(
    avg('Price').alias('Average_Price'),
    sum('Price').alias('Total_Price'),
    count('Pizza Name').alias('Pizza_Count')
)

# Show the result
result.show()

# Stop the Spark session
spark.stop()

# +--------------+--------------------+----------------+----------------+------+
# |       Company|          Pizza Name|            Type|            Size| Price|
# +--------------+--------------------+----------------+----------------+------+
# |Domino's Pizza|         Hand Tossed|   Cheeses Pizza|  "Small (10"")"| $5.99|
# |Domino's Pizza|         Hand Tossed|   Cheeses Pizza| "Medium (12"")"| $7.99|
# |Domino's Pizza|         Hand Tossed|   Cheeses Pizza|  "Large (14"")"| $9.99|
# |Domino's Pizza|        Handmade Pan|   Cheeses Pizza| "Medium (12"")"| $7.99|
# |Domino's Pizza|  Crunchy Thin Crust|   Cheeses Pizza|  "Small (10"")"| $5.99|
# |Domino's Pizza|  Crunchy Thin Crust|   Cheeses Pizza| "Medium (12"")"| $7.99|
# |Domino's Pizza|  Crunchy Thin Crust|   Cheeses Pizza|  "Large (14"")"| $9.99|
# |Domino's Pizza|      Brooklyn Style|   Cheeses Pizza|  "Large (14"")"| $9.99|
# |Domino's Pizza|      Brooklyn Style|   Cheeses Pizza|"X-Large (16"")"|$11.99|
# |Domino's Pizza|   Gluten Free Crust|   Cheeses Pizza|  "Small (10"")"| $8.99|
# |Domino's Pizza|Spinach & Feta (H...|Specialty Pizzas|  "Small (10"")"|$11.99|
# |Domino's Pizza|Spinach & Feta (H...|Specialty Pizzas| "Medium (12"")"|$13.99|
# |Domino's Pizza|Spinach & Feta (H...|Specialty Pizzas|  "Large (14"")"|$15.99|
# |Domino's Pizza|Spinach & Feta (B...|Specialty Pizzas|"X-Large (16"")"|$17.99|
# |Domino's Pizza|Spinach & Feta (G...|Specialty Pizzas|  "Small (10"")"|$14.99|
# |Domino's Pizza|Wisconsin 6 Chees...|Specialty Pizzas|  "Small (10"")"|$11.99|
# |Domino's Pizza|Wisconsin 6 Chees...|Specialty Pizzas| "Medium (12"")"|$13.99|
# |Domino's Pizza|Wisconsin 6 Chees...|Specialty Pizzas|  "Large (14"")"|$15.99|
# |Domino's Pizza|Wisconsin 6 Chees...|Specialty Pizzas|"X-Large (16"")"|$17.99|
# |Domino's Pizza|Wisconsin 6 Chees...|Specialty Pizzas|  "Small (10"")"|$14.99|
# +--------------+--------------------+----------------+----------------+------+
# only showing top 20 rows

# root
#  |-- Company: string (nullable = true)
#  |-- Pizza Name: string (nullable = true)
#  |-- Type: string (nullable = true)
#  |-- Size: string (nullable = true)
#  |-- Price: string (nullable = true)

# +--------------+--------------------+----------------+----------------+-----+
# |       Company|          Pizza Name|            Type|            Size|Price|
# +--------------+--------------------+----------------+----------------+-----+
# |Domino's Pizza|         Hand Tossed|   Cheeses Pizza|  "Small (10"")"| 5.99|
# |Domino's Pizza|         Hand Tossed|   Cheeses Pizza| "Medium (12"")"| 7.99|
# |Domino's Pizza|         Hand Tossed|   Cheeses Pizza|  "Large (14"")"| 9.99|
# |Domino's Pizza|        Handmade Pan|   Cheeses Pizza| "Medium (12"")"| 7.99|
# |Domino's Pizza|  Crunchy Thin Crust|   Cheeses Pizza|  "Small (10"")"| 5.99|
# |Domino's Pizza|  Crunchy Thin Crust|   Cheeses Pizza| "Medium (12"")"| 7.99|
# |Domino's Pizza|  Crunchy Thin Crust|   Cheeses Pizza|  "Large (14"")"| 9.99|
# |Domino's Pizza|      Brooklyn Style|   Cheeses Pizza|  "Large (14"")"| 9.99|
# |Domino's Pizza|      Brooklyn Style|   Cheeses Pizza|"X-Large (16"")"|11.99|
# |Domino's Pizza|   Gluten Free Crust|   Cheeses Pizza|  "Small (10"")"| 8.99|
# |Domino's Pizza|Spinach & Feta (H...|Specialty Pizzas|  "Small (10"")"|11.99|
# |Domino's Pizza|Spinach & Feta (H...|Specialty Pizzas| "Medium (12"")"|13.99|
# |Domino's Pizza|Spinach & Feta (H...|Specialty Pizzas|  "Large (14"")"|15.99|
# |Domino's Pizza|Spinach & Feta (B...|Specialty Pizzas|"X-Large (16"")"|17.99|
# |Domino's Pizza|Spinach & Feta (G...|Specialty Pizzas|  "Small (10"")"|14.99|
# |Domino's Pizza|Wisconsin 6 Chees...|Specialty Pizzas|  "Small (10"")"|11.99|
# |Domino's Pizza|Wisconsin 6 Chees...|Specialty Pizzas| "Medium (12"")"|13.99|
# |Domino's Pizza|Wisconsin 6 Chees...|Specialty Pizzas|  "Large (14"")"|15.99|
# |Domino's Pizza|Wisconsin 6 Chees...|Specialty Pizzas|"X-Large (16"")"|17.99|
# |Domino's Pizza|Wisconsin 6 Chees...|Specialty Pizzas|  "Small (10"")"|14.99|
# +--------------+--------------------+----------------+----------------+-----+
# only showing top 20 rows

# root
#  |-- Company: string (nullable = true)
#  |-- Pizza Name: string (nullable = true)
#  |-- Type: string (nullable = true)
#  |-- Size: string (nullable = true)
#  |-- Price: double (nullable = true)

# +-----------------+------------------+------------------+-----------+
# |          Company|     Average_Price|       Total_Price|Pizza_Count|
# +-----------------+------------------+------------------+-----------+
# |      IMO's Pizza| 17.10208333333333|410.44999999999993|         24|
# |        Pizza Hut| 13.41539682539683|1690.3400000000006|        126|
# |   Domino's Pizza| 14.29113636363637|1257.6200000000006|         88|
# |Godfather's Pizza|20.271127819548834| 2696.059999999995|        133|
# +-----------------+------------------+------------------+-----------+
