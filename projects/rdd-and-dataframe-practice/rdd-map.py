# Import necessary libraries from PySpark
from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "Name Processing App")

# List of names
names_list = ['anna', 'bartek', 'celina', 'damian', 'ewa']

# Creating an RDD from the list of names
names_rdd = sc.parallelize(names_list)

# Transforming names to uppercase
uppercase_names_rdd = names_rdd.map(lambda name: name.upper())

# Transforming names to uppercase
first_five_names = uppercase_names_rdd.take(5)

# Display the results
print(first_five_names)

# Close SparkContext
sc.stop()

# Results
# ['ANNA', 'BARTEK', 'CELINA', 'DAMIAN', 'EWA']
