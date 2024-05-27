from pyspark.sql import DataFrame
from pyspark.sql.functions import regexp_replace, split, col, explode, lower, trim
from pyspark.sql.types import DateType, LongType

class DataCleaner:

    @staticmethod
    def clean_hashtags(df: DataFrame) -> DataFrame:
        # Clean the 'hashtags' column using regexp and split
        df = df.withColumn("cleaned_hashtags", regexp_replace(col("hashtags"), "[\[\]']", ""))
        # Split by comma
        df = df.withColumn("hashtag_list", split(col("cleaned_hashtags"), ","))
        # Explode to separate the list into individual rows
        df = df.withColumn("hashtag", explode(col("hashtag_list")))
        # Remove white spaces and convert to lowercase
        df = df.withColumn("hashtag", lower(trim(col("hashtag"))))
        # Filtering unwanted hashtags
        df = df.filter(
            (col("hashtag") != "") &
            (col("hashtag").rlike("^[a-zA-Z0-9_]+$")) &  # Only alphanumeric characters and underscores
            (~col("hashtag").rlike("^[0-9]+$")) &        # Exclude single numbers
            (~col("hashtag").rlike("http"))              # Exclude links and URLs
        )
        return df

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
