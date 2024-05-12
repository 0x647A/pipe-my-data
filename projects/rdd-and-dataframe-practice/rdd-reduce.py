# Import necessary libraries from PySpark
from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "Sum RDD App")

# List of values
values_list = [10, 20, 30, 40, 50, 60]

# Creating an RDD from the list of values
values_rdd = sc.parallelize(values_list)

# Using the reduce function to sum all values in the RDD
total_sum = values_rdd.reduce(lambda v1, v2: v1 + v2)

# Display the results
print("Sum of all values in the RDD:", total_sum)

# Close SparkContext
sc.stop()

# Results
# Sum of all values in the RDD: 210
