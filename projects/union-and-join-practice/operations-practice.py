# Task
#
# Load the file with Netflix titles (netflix_titles.csv) into a DataFrame.
# Examine the data structure (schema, number of records, etc.).
# Replace nulls with the string "NULL".
# Check how many movies there are by type (column "type").
# Check how many titles were directed by each director (column "director").
# Create statistics by year – how many movies were made per year (displayed in chronological order).
# Determine how many movies are assigned to each genre (listed_in).

# Import necessary libraries from PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

# Initialize Spark session
spark = SparkSession.builder.appName("NetflixTitles").getOrCreate()

# Load the CSV file into a DataFrame
df = spark.read.csv("/datasets/netflix1.csv", header=True, inferSchema=True)

# Examine the data structure
df.printSchema()
record_count = df.count()
print(f"Number of records: {record_count}")

# Replace nulls with the string "NULL"
df = df.fillna("NULL")

# Count the number of each type (Movie, TV Show)
type_counts = df.groupBy("type").count()
type_counts.show()

# Count the number of titles directed by each director
director_counts = df.groupBy("director").count().orderBy(col("count").desc())
director_counts.show()

# Statistics by year – how many films were made per year (displayed in chronological order)
titles_per_year = df.groupBy("release_year").count().orderBy("release_year")
titles_per_year.show()

# Count the number of titles assigned to each genre (listed_in)
genre_counts = df.withColumn("genre", when(col("listed_in").isNull(), "NULL").otherwise(col("listed_in"))) \
                 .groupBy("genre").count().orderBy(col("count").desc())
genre_counts.show()

# Stop the Spark session
spark.stop()

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

# Number of records: 8791
# +-------------+-----+
# |         type|count|
# +-------------+-----+
# |      TV Show| 2664|
# |        Movie| 6126|
# |William Wyler|    1|
# +-------------+-----+

# +--------------------+-----+
# |            director|count|
# +--------------------+-----+
# |           Not Given| 2588|
# |       Rajiv Chilaka|   20|
# | Alastair Fothergill|   18|
# |Raúl Campos, Jan ...|   18|
# |        Marcus Raboy|   16|
# |         Suhas Kadav|   16|
# |           Jay Karas|   14|
# | Cathy Garcia-Molina|   13|
# |     Youssef Chahine|   12|
# |     Martin Scorsese|   12|
# |         Jay Chapman|   12|
# |    Steven Spielberg|   11|
# |    Don Michael Paul|   10|
# |Mark Thornton, To...|   10|
# |        David Dhawan|    9|
# |    Robert Rodriguez|    8|
# |         Troy Miller|    8|
# |      Kunle Afolayan|    8|
# |     Fernando Ayllón|    8|
# |         Hakan Algül|    8|
# +--------------------+-----+
# only showing top 20 rows

# +------------+-----+
# |release_year|count|
# +------------+-----+
# |        1925|    1|
# |        1942|    2|
# |        1943|    3|
# |        1944|    2|
# |        1945|    4|
# |        1946|    2|
# |        1947|    1|
# |        1954|    2|
# |        1955|    3|
# |        1956|    2|
# |        1958|    3|
# |        1959|    1|
# |        1960|    4|
# |        1961|    1|
# |        1962|    3|
# |        1963|    2|
# |        1964|    2|
# |        1965|    2|
# |        1966|    1|
# |        1967|    5|
# +------------+-----+
# only showing top 20 rows

# +--------------------+-----+
# |               genre|count|
# +--------------------+-----+
# |Dramas, Internati...|  362|
# |       Documentaries|  359|
# |     Stand-Up Comedy|  334|
# |Comedies, Dramas,...|  274|
# |Dramas, Independe...|  252|
# |            Kids' TV|  219|
# |Children & Family...|  215|
# |Children & Family...|  201|
# |Documentaries, In...|  186|
# |Dramas, Internati...|  180|
# |Comedies, Interna...|  176|
# |Comedies, Interna...|  152|
# |              Dramas|  137|
# |Dramas, Internati...|  134|
# |Action & Adventur...|  132|
# |  Action & Adventure|  128|
# |International TV ...|  121|
# |Comedies, Dramas,...|  116|
# |            Comedies|  110|
# |Crime TV Shows, I...|  110|
# +--------------------+-----+
# only showing top 20 rows
