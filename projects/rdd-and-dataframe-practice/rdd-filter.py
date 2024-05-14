# Import necessary libraries from PySpark
from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "Name Processing App")

# List of names
names_list = ['anna', 'bartek', 'celina', 'damian', 'ewa', 'zoe']

# Creating RDD from the list of names
names_rdd = sc.parallelize(names_list)

# Filter names to only keep those with less than 5 characters
short_names_rdd = names_rdd.filter(lambda name: len(name) < 5)

# Pobranie wszystkich pasujących imion
short_names = short_names_rdd.collect()

# Display the results
print(short_names)

# Close SparkContext
sc.stop()

# Results
# ['anna', 'ewa', 'zoe']
