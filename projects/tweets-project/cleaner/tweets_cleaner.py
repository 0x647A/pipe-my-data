from pyspark.sql import DataFrame
from pyspark.sql.functions import regexp_replace, split, col
from pyspark.sql.types import DateType, LongType

class DataCleaner:

    @staticmethod
    def clean_hashtags(df: DataFrame) -> DataFrame:
        # Clean the 'hashtags' column using regexp and split
        df_cleaned = df.withColumn("cleaned_hashtags", regexp_replace(col("hashtags"), "[\[\]']", ""))

        # Split by comma
        df_split = df_cleaned.withColumn("hashtag_list", split(col("cleaned_hashtags"), ","))

        # Explode to separate the list into individual rows
        df_exploded = df_split.withColumn("hashtag", explode(col("hashtag_list")))

        # Group and count hashtags
        df_count = df_exploded.groupBy("hashtag").count()

        # Sort the results
        df_sorted = df_count.orderBy(col("count").desc())
        
        return df_sorted

    @staticmethod
    def convert_column_types(df: DataFrame) -> DataFrame:
        # Convert date columns to DateType
        df = df.withColumn('date', col('date').cast(DateType()))
        df = df.withColumn('user_created', col('user_created').cast(DateType()))
        
        # Convert numerical columns to LongType or IntegerType
        df = df.withColumn('user_favourites', col('user_favourites').cast(LongType()))
        df = df.withColumn('user_friends', col('user_friends').cast(LongType()))
        df = df.withColumn('user_followers', col('user_followers').cast(LongType()))

        return df

    @staticmethod
    def clean_data(df: DataFrame) -> DataFrame:
        # Apply all cleaning steps
        df = DataCleaner.clean_hashtags(df)
        df = DataCleaner.convert_column_types(df)
        return df
