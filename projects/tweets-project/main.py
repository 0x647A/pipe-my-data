from pyspark.sql import SparkSession
from loader.tweets_loader import TweetLoader
from cleaner.tweets_cleaner import DataCleaner
from analysers.tweets_analyser import TweetsAnalyser
from analysers.tweets_searcher import TweetsSearch

def main():
    # Create a Spark session
    spark = SparkSession.builder \
        .appName("CSV to DataFrame") \
        .getOrCreate()

    # Instantiate the TweetLoader class
    loader = TweetLoader(spark)

    # Load and combine all datasets
    combined_df = loader.loadAllDatasets()

    # Clean the combined DataFrame using DataCleaner
    cleaned_df = DataCleaner.clean_data(combined_df)

    # Instantiate the TweetAnalyzer class
    analyser = TweetsAnalyser(cleaned_df)

    # Perform analysis
    hashtag_counts = analyser.count_hashtags()
    retweet_count = analyser.count_retweets()
    verified_user_count = analyser.count_user_verified()
    source_counts = analyser.count_sources()
    avg_followers_per_location = analyser.avg_followers_per_location()

    # Display the analysis results
    print("Hashtag Counts:")
    hashtag_counts.show()

    print("Number of Retweets:")
    print(retweet_count)

    print("Number of Verified User:")
    print(verified_user_count)

    print("Source Counts:")
    source_counts.show()

    print("Average Followers per Location:")
    avg_followers_per_location.show()

    # Instantiate the TweetsSearch class
    search = TweetsSearch(cleaned_df)

    # Perform searches
    word_search_result = search.search_by_word("covid")
    words_search_result = search.search_by_words(["covid", "pandemic", "virus"])
    filtered_tweets = search.filter_tweets(keyword="music", location="Los Angeles")

    # Display the search results
    print("Search by Word 'covid':")
    word_search_result.show()

    print("Search by Words ['covid', 'pandemic', 'virus']:")
    words_search_result.show()

    print("Search by Word 'music' and Location 'Los Angeles':")
    filtered_tweets.show(truncate=False)

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()

# Hashtag Counts:                                                                                                                                                                                                                                                                                                           

# +-----------------+-----+                                                                                                                                                                                                                                                                                                 
# |          hashtag|count|
# +-----------------+-----+
# |          grammys| 2014|
# |              bts|   29|
# |            music|   24|
# |  singyourdialect|   18|
# |        cryptoban|   18|
# |grammynominations|   17|
# |      blackfriday|   15|
# | btsxlatelateshow|   15|
# |          scammys|   13|
# |     thanksgiving|   12|
# |           wizkid|   11|
# |      taylorswift|   11|
# |            false|   11|
# |     evermoreaoty|   11|
# |    biracialspace|   11|
# |     btsxlatelate|   11|
# |       aroojaftab|   10|
# |          hawkeye|   10|
# |             btsv|   10|
# |         evermore|    9|
# +-----------------+-----+
# only showing top 20 rows

# Number of Retweets:
# 0

# Number of Verified User:
# 146

# Source Counts:
# +-------------------+-----+                                                                                                                                                                                                                                                                                               
# |             source|count|
# +-------------------+-----+
# | Twitter for iPhone| 1246|
# |    bibeypost_stock| 1020|
# |    whatsonthorold2|  990|
# |       mmahotstuff1|  928|
# |    MareaInformativ|  651|
# |      reurope_stock|  647|
# |       optioncharts|  624|
# |       ConsumerFeed|  413|
# |Twitter for Android|  403|
# |    dispatchtribune|  386|
# |      OlympiaReport|  377|
# |    TranscriptDaily|  374|
# |        ledgerzette|  372|
# |    EnterpriseLeade|  369|
# |         ZolmaxNews|  350|
# |    TheMarketsDaily|  347|
# |     ThisLincolnian|  340|
# |    Twitter Web App|  339|
# |         WeekHerald|  339|
# |       TickerReport|  335|
# +-------------------+-----+
# only showing top 20 rows

# Average Followers per Location:
# +--------------------+------------------+
# |       user_location|     avg_followers|
# +--------------------+------------------+
# |      Emeryville, CA|       1.1809198E7|
# |       Hollywood, CA|         7530393.0|
# |        Santa Monica|         3510179.0|
# |               Any. |         3097773.0|
# |    Karachi,Pakistan|         1885672.5|
# |      𝘌 𝘢 𝘳 𝘵 𝘩|         1676598.0|
# |   Naccache, Lebanon|         1402002.0|
# |turn on notificat...|         1237486.0|
# |         Philippines|         895102.25|
# |   Jakarta-Indonesia|          415851.0|
# |  Salatiga - Jakarta|          405366.0|
# |               Kenya|          402574.0|
# |     London, England| 393556.9090909091|
# |   IG: SelenaFanClub|          362233.0|
# |Turn on notificat...|          350037.0|
# |              Dublin|          310878.0|
# |           WORLDWIDE|          266581.0|
# |     Southern Africa|          245710.0|
# |         Los Angeles|222908.72727272726|
# |San Francisco, LA...|          219217.0|
# +--------------------+------------------+
# only showing top 20 rows

# Search by Word 'covid':
# +--------------------+----------+-------------+
# |                text| user_name|user_location|
# +--------------------+----------+-------------+
# |Wednesday's editi...|Cyrus Webb|  Mississippi|
# +--------------------+----------+-------------+

# Search by Words ['covid', 'pandemic', 'virus']:
# +--------------------+---------------------+--------------------+
# |                text|            user_name|       user_location|
# +--------------------+---------------------+--------------------+
# |Share the love &a...|        Russell Mucki|     Kampala, Uganda|
# |the way pipe down...|                kayla|          Denver, CO|
# |We celebrate all ...|         METROFM SABC|        South Africa|
# |Even the #GRAMMYs...|        Kylie Minogue|              Albina|
# |#np Here we are a...|     Tunicia Phillips|Johannesburg, Sou...|
# |Nominations for t...|            The Sauce|      Nairobi, Kenya|
# |WTF? #GRAMMYs mad...|Cindy 신디 💟 🅑🅣🅢⁷| Bangtan, California|
# |@RecordingAcad #G...|             PEͥLAͣHͫ|       Lagos Nigeria|
# |HER BEST ALBUM AN...|       Joshua Andrews|      Chesapeake, VA|
# |This is a categor...|                 Kath|Brooklyn Heights, NY|
# |#GRAMMYs FLOP htt...|   Fernanda || 💿🇨🇴|            Colombia|
# |They should’ve no...|         BareKey 🐻🔑|       Jozi, Gauteng|
# |Fck Joe Rogan &am...| 💛THEE K-12 is th...|       United States|
# |@elizgrant_ best ...|                  igo|  Marina del Rey, CA|
# |Planet HER winnin...| TYLER THEE MF STA...|                 ATL|
# |Look at this beau...|           Random Guy|   177a Bleecker St.|
# |This will forever...|   ᴍᴏᴄʜᴀ ᴄʜᴏᴄᴏʟᴀᴛᴀ ☕️|             Wakanda|
# |Did your favorite...|              Rappler|         Philippines|
# |🎵; eh God by @Ki...|           oluwazhini|      Lagos, Nigeria|
# |Just saying it ri...|     Fadhil Ramadhani|Jakarta Capital R...|
# +--------------------+---------------------+--------------------+
# only showing top 20 rows

# Search by Word 'music' and Location 'Los Angeles':
# +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+-----------------------------+
# |text                                                                                                                                                                                                                                                           |user_name                  |user_location                |
# +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+-----------------------------+
# |Congratulations to @sonymusic artists on their 2022 @RecordingAcad #GRAMMYs nominations! https://t.co/7hy922x0Cp                                                                                                                                               |Right Angles               |London, New York, Los Angeles|
# |@latimes A little bit like the 80s and the 90s when black people could really sing. #BTS #GRAMMYs  #music                                                                                                                                                      |J West #TBT #TBH #OOTD #ICO|Los Angeles, CA              |
# |Read below our #GRAMMYs 2022 Nomination Recap and the women creating milestones in music 🎶 https://t.co/YPQFPYMWH7                                                                                                                                            |Girls Behind the Rock Show |Los Angeles, CA              |
# |#GRAMMYs  is not a world wide award it is for white alone you people should stop deceiving us with it that Grammy belongs to everyone @RecordingAcad @ColumbiaRecords Wizkid music and album go so far more than the people nominated on record of the year    |chiz Alexander             |Los Angeles, CA              |
# |Sneak peak!! HOURS🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 release date. Dec 22-22 #GRAMMYs #Maanadu #popmusic #singersongwriter #jamesbene #NewMusicAlert #love https://t.co/ZDLYWoi2sv                                                                                           |James Bene                 |Los Angeles, CA              |
# |"And congrats to @JonBatiste for his additional #GRAMMYs nominations for  Best Improvised Jazz Solo for ""Bigger Than Us"" from #PixarSoul and Best Jazz Instrumental Album for Jazz Selections: Music From and Inspired by Soul! 🎷🎶 https://t.co/8H8paCgGxH"|Disney Music               |Los Angeles, CA              |
# |Jon Batiste, Justin Bieber and H.E.R. lead Grammy Awards nominations https://t.co/b2VWfDDFe4 #GRAMMYs #GrammyAwards #GrammyAwards2022 .@justinbieber .@JonBatiste .@HERMusicx #awards                                                                          |TVMusic Network            |Los Angeles, CA              |
# |Pinching ourselves over the news that our @billieeilish concert film has been nominated at the #GRAMMYs! A huge congratulations to @PatrickTOsborne and the entire #HappierThanEver team https://t.co/xnl9KoJgvl #bestmusicfilm                                |Nexus Studios              |London | Los Angeles | Sydney|
# |Congratulations to our #Grammys nominees @dreamtheaternet, @GojiraMusic, &amp; @WolfVanHalen/@MammothWVH. https://t.co/5v527Aw0p3                                                                                                                              |Cosa Nostra PR             |London and Los Angeles       |
# |Give @jsullivanmusic ALL her things. Goodnight. #GRAMMYs                                                                                                                                                                                                       |Brooke Lynn Hytes          |Los Angeles, CA              |
# +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+-----------------------------+
