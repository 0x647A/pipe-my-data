# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, explode

# Initialize Spark session
spark = SparkSession.builder \
    .appName("NetflixDataAnalysis") \
    .getOrCreate()

# Load data into a DataFrame
file_path = "/datasets/netflix1.csv"
df = spark.read.option("header", "true").csv(file_path)

# Review data using show and printSchema
df.show(10)
df.printSchema()

# Replace nulls with 'N.A.'
df_filled = df.na.fill("N.A.")

# Convert 'listed_in' column from string to array by splitting on commas
df_split = df_filled.withColumn("listed_in_array", split(col("listed_in"), ", "))

# Explode the 'listed_in_array' column
df_exploded = df_split.withColumn("single_listed_in", explode(col("listed_in_array")))

# Select only the 'show_id' and 'single_listed_in' columns
df_final = df_exploded.select("show_id", "single_listed_in")

# Show the final DataFrame
df_final.show(10, truncate=False)

# Count each of gentre
df_gentre = df_final.groupBy("single_listed_in").count()

# Show the dataset
df_gentre.show(10)

# Stop the Spark session
spark.stop()

# +-------+-------+--------------------+-------------------+--------------+----------+------------+------+---------+--------------------+
# |show_id|   type|               title|           director|       country|date_added|release_year|rating| duration|           listed_in|
# +-------+-------+--------------------+-------------------+--------------+----------+------------+------+---------+--------------------+
# |     s1|  Movie|Dick Johnson Is Dead|    Kirsten Johnson| United States| 9/25/2021|        2020| PG-13|   90 min|       Documentaries|
# |     s3|TV Show|           Ganglands|    Julien Leclercq|        France| 9/24/2021|        2021| TV-MA| 1 Season|Crime TV Shows, I...|
# |     s6|TV Show|       Midnight Mass|      Mike Flanagan| United States| 9/24/2021|        2021| TV-MA| 1 Season|TV Dramas, TV Hor...|
# |    s14|  Movie|Confessions of an...|      Bruno Garotti|        Brazil| 9/22/2021|        2021| TV-PG|   91 min|Children & Family...|
# |     s8|  Movie|             Sankofa|       Haile Gerima| United States| 9/24/2021|        1993| TV-MA|  125 min|Dramas, Independe...|
# |     s9|TV Show|The Great British...|    Andy Devonshire|United Kingdom| 9/24/2021|        2021| TV-14|9 Seasons|British TV Shows,...|
# |    s10|  Movie|        The Starling|     Theodore Melfi| United States| 9/24/2021|        2021| PG-13|  104 min|    Comedies, Dramas|
# |   s939|  Movie|Motu Patlu in the...|        Suhas Kadav|         India|  5/1/2021|        2019| TV-Y7|   87 min|Children & Family...|
# |    s13|  Movie|        Je Suis Karl|Christian Schwochow|       Germany| 9/23/2021|        2021| TV-MA|  127 min|Dramas, Internati...|
# |   s940|  Movie|Motu Patlu in Won...|        Suhas Kadav|         India|  5/1/2021|        2013| TV-Y7|   76 min|Children & Family...|
# +-------+-------+--------------------+-------------------+--------------+----------+------------+------+---------+--------------------+
# only showing top 10 rows

# root
#  |-- show_id: string (nullable = true)
#  |-- type: string (nullable = true)
#  |-- title: string (nullable = true)
#  |-- director: string (nullable = true)
#  |-- country: string (nullable = true)
#  |-- date_added: string (nullable = true)
#  |-- release_year: string (nullable = true)
#  |-- rating: string (nullable = true)
#  |-- duration: string (nullable = true)
#  |-- listed_in: string (nullable = true)

# +-------+------------------------+
# |show_id|single_listed_in        |
# +-------+------------------------+
# |s1     |Documentaries           |
# |s3     |Crime TV Shows          |
# |s3     |International TV Shows  |
# |s3     |TV Action & Adventure   |
# |s6     |TV Dramas               |
# |s6     |TV Horror               |
# |s6     |TV Mysteries            |
# |s14    |Children & Family Movies|
# |s14    |Comedies                |
# |s8     |Dramas                  |
# +-------+------------------------+
# only showing top 10 rows

# +-------------------+-----+
# |   single_listed_in|count|
# +-------------------+-----+
# |  Romantic TV Shows|  370|
# |Science & Nature TV|   92|
# | Action & Adventure|  859|
# |    Korean TV Shows|  151|
# |      Documentaries|  868|
# |           TV Shows|   16|
# |           Comedies| 1674|
# |     Anime Features|   71|
# |      Sports Movies|  219|
# |               N.A.|    2|
# +-------------------+-----+
# only showing top 10 rows
