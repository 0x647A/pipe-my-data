from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

class TweetLoader:
    COVID_LABEL = "covid"
    GRAMMYS_LABEL = "grammys"
    STOCKERBOT_LABEL = "stockerbot"

    def __init__(self, spark_session):
        self.spark = spark_session

    def loadCovid(self):
        return self.spark.read.option("header", "true") \
            .csv("../datasets/covid_tweets_anglais.csv") \
            .withColumn("category", lit(TweetLoader.COVID_LABEL)) \
            .na.drop()

    def loadGrammys(self):
        return self.spark.read.option("header", "true") \
            .csv("../datasets/GRAMMYs_tweets.csv") \
            .withColumn("category", lit(TweetLoader.GRAMMYS_LABEL)) \
            .na.drop()

    def loadStockerbot(self):
        return self.spark.read.option("header", "true") \
            .csv("../datasets/stockerbot-export.csv") \
            .withColumn("category", lit(TweetLoader.STOCKERBOT_LABEL)) \
            .na.drop()

    def loadAllDatasets(self):
        covid_df = self.loadCovid()
        grammys_df = self.loadGrammys()
        stockerbot_df = self.loadStockerbot()

        combined_df = covid_df.unionByName(grammys_df, allowMissingColumns=True) \
                              .unionByName(stockerbot_df, allowMissingColumns=True)
        return combined_df
