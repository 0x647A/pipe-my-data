from pyspark.sql import DataFrame
from pyspark.sql.functions import regexp_replace, split, col
from pyspark.sql.types import DateType, LongType, IntegerType

class DataCleaner:

    @staticmethod
    def clean_hashtags(df: DataFrame) -> DataFrame:
        # Clean the 'hashtags' column using regexp and split
        df = df.withColumn('hashtags', regexp_replace(col('hashtags'), r'[^\w#]', ''))
        df = df.withColumn('hashtags', split(col('hashtags'), '#').alias('hashtags'))
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
