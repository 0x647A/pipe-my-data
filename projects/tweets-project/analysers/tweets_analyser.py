from pyspark.sql import DataFrame
from pyspark.sql.functions import col, explode, count, avg

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

    def count_hashtags(self):
        # Explode the list of hashtags and count occurrences
        return self.df.withColumn(self.HASHTAG_COLUMN, explode(col(self.HASHTAG_COLUMN))) \
                      .groupBy(self.HASHTAG_COLUMN) \
                      .agg(count("*").alias("count")) \
                      .orderBy("count", ascending=False)

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
