# Import necessary modules from PySpark and the random module from Python's standard library
from pyspark.sql import SparkSession, Row
import random

# Initialize the Spark session
spark = SparkSession.builder.appName('first_app').master('local').getOrCreate()

# Function to generate random first and last names
def generate_name():
    first_names = ["Anna", "Jan", "Maria", "Piotr", "Katarzyna", "Tomasz", "Agnieszka", "Marcin", "Ewa", "Michał"]
    last_names = ["Kowalski", "Nowak", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski", "Zieliński", "Szymański", "Woźniak"]
    return random.choice(first_names), random.choice(last_names)

# Generate data: create a list of Row objects each representing one person with a name and age
data = [Row(first_name=generate_name()[0], last_name=generate_name()[1], age=random.randint(16, 90)) for _ in range(15)]

# Create a DataFrame from the list of Row objects
df_people = spark.createDataFrame(data)

# Display the data in the DataFrame
df_people.show()

# Display only first name and last name in DataFrame
# df_people.select("first_name", "last_name").show()

# Stop the Spark session to free up resources
spark.stop()