from pyspark.sql import DataFrame
from pyspark.sql.functions import col, explode, count, avg, regexp_replace, lower, trim

class TweetsAnalyser:
    HASHTAG_COLUMN = "hashtags"
    IS_RETWEET_COLUMN = "is_retweet"
    IS_VERIFIED_COLUMN = "user_verified"
    SOURCE_COLUMN = "source"
    USER_FOLLOWERS = "user_followers"
    USER_NAME = "user_name"
    USER_LOCATION = "user_location"

    def __init__(self, df: DataFrame):
        self.df = df

    def count_hashtags(self) -> DataFrame:
        # Cleaning the hashtag column
        df_cleaned = self.df.withColumn("cleaned_hashtags", regexp_replace(col(self.HASHTAG_COLUMN), "[\[\]']", ""))
        
        # Splitting by comma
        df_split = df_cleaned.withColumn("hashtag_list", split(col("cleaned_hashtags"), ","))
        
        # Exploding the list of hashtags
        df_exploded = df_split.withColumn("hashtag", explode(col("hashtag_list")))
        
        # Removing white spaces and converting to lowercase
        df_trimmed = df_exploded.withColumn("hashtag", lower(trim(col("hashtag"))))
        
        # Filtering unwanted hashtags
        df_filtered = df_trimmed.filter(
            (col("hashtag") != "") &
            (col("hashtag").rlike("^[a-zA-Z0-9_]+$")) &  # Only alphanumeric characters and underscores
            (~col("hashtag").rlike("^[0-9]+$")) &        # Exclude single numbers
            (~col("hashtag").rlike("http"))              # Exclude links and URLs
        )
        
        # Grouping and counting hashtags
        df_count = df_filtered.groupBy("hashtag").count()
        
        return df_count.orderBy(col("count").desc())

    def count_retweets(self):
        # Count the number of retweets
        return self.df.filter(col(self.IS_RETWEET_COLUMN) == True).count()

    def count_user_verified(self):
        # Count the number of verified user
        return self.df.filter(col(self.IS_VERIFIED_COLUMN) == True).count()

    def count_sources(self):
        # Count the number of tweets from each source
        return self.df.groupBy(self.SOURCE_COLUMN) \
                      .agg(count("*").alias("count")) \
                      .orderBy("count", ascending=False)

    def avg_followers_per_location(self):
        # Filter non-null usernames and locations, remove duplicates, and calculate average followers per location
        filtered_df = self.df.filter(col(self.USER_NAME).isNotNull() & col(self.USER_LOCATION).isNotNull()) \
                             .dropDuplicates([self.USER_NAME, self.USER_LOCATION])

        return filtered_df.groupBy(self.USER_LOCATION) \
                          .agg(avg(self.USER_FOLLOWERS).alias("avg_followers")) \
                          .orderBy("avg_followers", ascending=False)
