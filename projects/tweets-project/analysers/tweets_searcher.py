from pyspark.sql import DataFrame
from pyspark.sql.functions import col, array_intersect, split, lit, lower

class TweetsSearch:
    TEXT = "text"
    USER_LOCATION = "user_location"

    def __init__(self, df: DataFrame):
        self.df = df

    def search_by_word(self, word: str) -> DataFrame:
        # Search for tweets containing the word
        return self.df.filter(col(self.TEXT).contains(word)).select("text", "user_name", "user_location")

    def search_by_words(self, words: list) -> DataFrame:
        # Convert the list of words into an array and search for tweets containing any of the words
        words_array = lit(words)
        return self.df.withColumn("words_in_text", split(col(self.TEXT), " ")) \
                      .filter(array_intersect(col("words_in_text"), words_array).isNotNull()).select("text", "user_name", "user_location")

    def filter_tweets(self, keyword: str, location: str) -> DataFrame:
        # Filtering based on keyword and location
        df_filtered = self.df.filter(
            (lower(col(self.TEXT)).contains(keyword.lower())) &
            (lower(col(self.USER_LOCATION)).contains(location.lower()))
        )
        return df_filtered.select("text", "user_name", "user_location")
