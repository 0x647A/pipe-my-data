from pyspark.sql import DataFrame
from pyspark.sql.functions import col, array_intersect, split, lit

class TweetsSearch:
    TEXT = "text"
    USER_LOCATION = "user_location"

    def __init__(self, df: DataFrame):
        self.df = df

    def search_by_word(self, word: str) -> DataFrame:
        # Search for tweets containing the word
        return self.df.filter(col(self.TEXT).contains(word))

    def search_by_words(self, words: list) -> DataFrame:
        # Convert the list of words into an array and search for tweets containing any of the words
        words_array = lit(words)
        return self.df.withColumn("words_in_text", split(col(self.TEXT), " ")) \
                      .filter(array_intersect(col("words_in_text"), words_array).isNotNull())

    def search_by_word_and_location(self, word: str, location: str) -> DataFrame:
        # Search for tweets containing the word and from a specific location
        return self.df.filter(col(self.TEXT).contains(word) & col(self.USER_LOCATION).contains(location))
