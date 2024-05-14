# Exercise:

# Create an RDD that will be filled with tuples of names, surnames, gender, and age (at least 10 records. Tuple4<String, String, String, Integer>). Calculate:

#     The total age of all men
#     The total age of all women
#     The minimum and maximum age in the dataset

# Import necessary libraries from PySpark
from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "People Info App")

# List of data containing name, surname, gender, and age
data = [
    ("Anna", "Kowalska", "F", 28),
    ("Piotr", "Nowak", "M", 35),
    ("Ewa", "Maj", "F", 22),
    ("Tomasz", "Czerwiński", "M", 45),
    ("Olga", "Lewandowska", "F", 30),
    ("Marcin", "Wójcik", "M", 19),
    ("Zofia", "Kamińska", "F", 41),
    ("Marek", "Kowal", "M", 60),
    ("Alicja", "Zając", "F", 18),
    ("Jakub", "Adamczyk", "M", 33)
]

# Create RDD
people_rdd = sc.parallelize(data)

# Filter data based on gender and calculate the total age
total_age_men = people_rdd.filter(lambda x: x[2] == "M").map(lambda x: x[3]).reduce(lambda x, y: x + y)
total_age_women = people_rdd.filter(lambda x: x[2] == "F").map(lambda x: x[3]).reduce(lambda x, y: x + y)

# Calculate the minimum and maximum age
min_age = people_rdd.map(lambda x: x[3]).min()
max_age = people_rdd.map(lambda x: x[3]).max()

# Display the results
print(f"Total age of all men: {total_age_men}")
print(f"Total age of all women: {total_age_women}")
print(f"Minimum age in the dataset: {min_age}")
print(f"Maximum age in the dataset: {max_age}")

# Close SparkContext
sc.stop()

# Results
# Total age of all men: 192
# Total age of all women: 139
# Minimum age in the dataset: 18
# Maximum age in the dataset: 60
