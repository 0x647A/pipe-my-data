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
    location_search_result = search.search_by_word_and_location("covid", "New York")

    # Display the search results
    print("Search by Word 'covid':")
    word_search_result.show()

    print("Search by Words ['covid', 'pandemic', 'virus']:")
    words_search_result.show()

    print("Search by Word 'covid' and Location 'New York':")
    location_search_result.show()

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()

# Hashtag Counts:                                                                                                                    
# 
# +--------------------+-----+                                                                                                       
# |            hashtags|count|
# +--------------------+-----+
# |                   0| 1421|
# |             GRAMMYs| 1285|
# |           labelNone|  309|
# |                   1|  265|
# |             Grammys|  130|
# |                   2|   97|
# |      protectedFalse|   79|
# |         linkUrlNone|   77|
# |      linkTcourlNone|   64|
# |                   3|   54|
# |             grammys|   37|
# |favouritesCount93219|   30|
# |linkTcourlhttpstc...|   27|
# |                   4|   26|
# |                   5|   22|
# |profileBannerUrlNone|   20|
# |label_typesnscrap...|   14|
# |linkTcourlhttpstc...|   13|
# |urlhttpstwitterco...|   13|
# |urlhttpstwitterco...|   13|
# +--------------------+-----+
# only showing top 20 rows
#
# Number of Retweets:
# 0
#
# Number of Verified User:
# 146
#
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
#
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
#
# Search by Word 'covid':
# +----+----------+-------+---------------+----+----+----------+------------+---------+----------+--------------+----+---------------+---------+-----------+--------+-----------+-----+--------------+-----------+----------------+-------------+--------------+-----------+-----+--------------------+--------+--------+----------+-------------+--------------------+------------+--------------+------------+---------------+-------------+--------------------+----------+---------+-------+-------------+--------+
# | url|      date|content|renderedContent|  id|user|replyCount|retweetCount|likeCount|quoteCount|conversationId|lang|         source|sourceUrl|sourceLabel|outlinks|tcooutlinks|media|retweetedTweet|quotedTweet|inReplyToTweetId|inReplyToUser|mentionedUsers|coordinates|place|            hashtags|cashtags|category| user_name|user_location|    user_description|user_created|user_followers|user_friends|user_favourites|user_verified|                text|is_retweet|timestamp|symbols|company_names|verified|
# +----+----------+-------+---------------+----+----+----------+------------+---------+----------+--------------+----+---------------+---------+-----------+--------+-----------+-----+--------------+-----------+----------------+-------------+--------------+-----------+-----+--------------------+--------+--------+----------+-------------+--------------------+------------+--------------+------------+---------------+-------------+--------------------+----------+---------+-------+-------------+--------+
# |NULL|2021-11-24|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|Twitter Web App|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|[ConversationsDai...|    NULL| grammys|Cyrus Webb|  Mississippi|Welcome! I am a #...|  2009-01-30|         11326|       12376|           8388|        False|Wednesday's editi...|     False|     NULL|   NULL|         NULL|    NULL|
# +----+----------+-------+---------------+----+----+----------+------------+---------+----------+--------------+----+---------------+---------+-----------+--------+-----------+-----+--------------+-----------+----------------+-------------+--------------+-----------+-----+--------------------+--------+--------+----------+-------------+--------------------+------------+--------------+------------+---------------+-------------+--------------------+----------+---------+-------+-------------+--------+
#
# Search by Words ['covid', 'pandemic', 'virus']:
# +----+----------+-------+---------------+----+----+----------+------------+---------+----------+--------------+----+-------------------+---------+-----------+--------+-----------+-----+--------------+-----------+----------------+-------------+--------------+-----------+-----+--------------------+--------+--------+---------------------+--------------------+--------------------+------------+--------------+------------+---------------+-------------+--------------------+----------+---------+-------+-------------+--------+--------------------+
# | url|      date|content|renderedContent|  id|user|replyCount|retweetCount|likeCount|quoteCount|conversationId|lang|             source|sourceUrl|sourceLabel|outlinks|tcooutlinks|media|retweetedTweet|quotedTweet|inReplyToTweetId|inReplyToUser|mentionedUsers|coordinates|place|            hashtags|cashtags|category|            user_name|       user_location|    user_description|user_created|user_followers|user_friends|user_favourites|user_verified|                text|is_retweet|timestamp|symbols|company_names|verified|       words_in_text|
# +----+----------+-------+---------------+----+----+----------+------------+---------+----------+--------------+----+-------------------+---------+-----------+--------+-----------+-----+--------------+-----------+----------------+-------------+--------------+-----------+-----+--------------------+--------+--------+---------------------+--------------------+--------------------+------------+--------------+------------+---------------+-------------+--------------------+----------+---------+-------+-------------+--------+--------------------+
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|   Twitter for iPad|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|[GrammysLakersTan...|    NULL| grammys|        Russell Mucki|     Kampala, Uganda|Am a singer, mult...|  2021-05-18|           652|         576|            140|        False|Share the love &a...|     False|     NULL|   NULL|         NULL|    NULL|[Share, the, love...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL| Twitter for iPhone|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [GRAMMYs]|    NULL| grammys|                kayla|          Denver, CO|Temple University...|  2015-02-28|           330|         266|          17294|        False|the way pipe down...|     False|     NULL|   NULL|         NULL|    NULL|[the, way, pipe, ...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|     Hootsuite Inc.|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|[GrammysAfricaBoo...|    NULL| grammys|         METROFM SABC|        South Africa|South Africa's nu...|  2012-02-07|       2031993|          41|           2438|         True|We celebrate all ...|     False|     NULL|   NULL|         NULL|    NULL|[We, celebrate, a...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|Twitter for Android|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|  [GRAMMYsBallonDor]|    NULL| grammys|        Kylie Minogue|              Albina|     Britney Spears"|  2021-11-10|            48|         241|           3597|        False|Even the #GRAMMYs...|     False|     NULL|   NULL|         NULL|    NULL|[Even, the, #GRAM...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL| Twitter for iPhone|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|         [npGRAMMYs]|    NULL| grammys|     Tunicia Phillips|Johannesburg, Sou...|M&G - Environment...|  2011-05-31|          3162|        5003|           9010|        False|#np Here we are a...|     False|     NULL|   NULL|         NULL|    NULL|[#np, Here, we, a...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|    Twitter Web App|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [GRAMMYs]|    NULL| grammys|            The Sauce|      Nairobi, Kenya|Your plug for the...|  2012-04-10|          9149|         843|            923|        False|Nominations for t...|     False|     NULL|   NULL|         NULL|    NULL|[Nominations, for...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL| Twitter for iPhone|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|  [GRAMMYsBTSSCAMMY]|    NULL| grammys|Cindy 신디 💟 🅑🅣🅢⁷| Bangtan, California|A-YO!! OT⁷ stan w...|  2021-03-26|            33|         365|           1306|        False|WTF? #GRAMMYs mad...|     False|     NULL|   NULL|         NULL|    NULL|[WTF?, #GRAMMYs, ...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|Twitter for Android|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|[GRAMMYstheWorldb...|    NULL| grammys|             PEͥLAͣHͫ|       Lagos Nigeria|Trying to put me ...|  2019-09-07|           266|         395|           1649|        False|@RecordingAcad #G...|     False|     NULL|   NULL|         NULL|    NULL|[@RecordingAcad, ...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL| Twitter for iPhone|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [GRAMMYs]|    NULL| grammys|       Joshua Andrews|      Chesapeake, VA|• Jesus is #1 🙌?...|  2010-09-19|           775|         799|          34516|        False|HER BEST ALBUM AN...|     False|     NULL|   NULL|         NULL|    NULL|[HER, BEST, ALBUM...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL| Twitter for iPhone|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [grammys]|    NULL| grammys|                 Kath|Brooklyn Heights, NY|Good coffee ☕️, g...|  2009-03-02|          1258|        1707|         101782|        False|This is a categor...|     False|     NULL|   NULL|         NULL|    NULL|[This, is, a, cat...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|Twitter for Android|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [GRAMMYs]|    NULL| grammys|   Fernanda || 💿🇨🇴|            Colombia|                   a|  2021-09-02|           678|        1194|          11679|        False|#GRAMMYs FLOP htt...|     False|     NULL|   NULL|         NULL|    NULL|[#GRAMMYs, FLOP, ...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL| Twitter for iPhone|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [Grammys]|    NULL| grammys|         BareKey 🐻🔑|       Jozi, Gauteng|Live first, tweet...|  2021-01-09|           179|         167|             85|        False|They should’ve no...|     False|     NULL|   NULL|         NULL|    NULL|[They, should’ve,...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL| Twitter for iPhone|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|[GrammysFckUGrammys]|    NULL| grammys| 💛THEE K-12 is th...|       United States|Democrat 💙 USAF ...|  2013-01-05|          4516|        5003|         247088|        False|Fck Joe Rogan &am...|     False|     NULL|   NULL|         NULL|    NULL|[Fck, Joe, Rogan,...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|Twitter for Android|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [GRAMMYs]|    NULL| grammys|                  igo|  Marina del Rey, CA|LG & LDR LTDA com...|  2018-12-29|          1428|        1328|           7978|        False|@elizgrant_ best ...|     False|     NULL|   NULL|         NULL|    NULL|[@elizgrant_, bes...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|   Twitter for iPad|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [GRAMMYs]|    NULL| grammys| TYLER THEE MF STA...|                 ATL|#BlackLivesMatter...|  2019-10-06|            30|         266|          47459|        False|Planet HER winnin...|     False|     NULL|   NULL|         NULL|    NULL|[Planet, HER, win...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|    Twitter Web App|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|[WandaVisionGramm...|    NULL| grammys|           Random Guy|   177a Bleecker St.|looking out the w...|  2013-02-24|            13|         174|          14380|        False|Look at this beau...|     False|     NULL|   NULL|         NULL|    NULL|[Look, at, this, ...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL| Twitter for iPhone|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [GRAMMYs]|    NULL| grammys|   ᴍᴏᴄʜᴀ ᴄʜᴏᴄᴏʟᴀᴛᴀ ☕️|             Wakanda|Variety is the sp...|  2010-11-24|           768|         741|          73844|        False|This will forever...|     False|     NULL|   NULL|         NULL|    NULL|[This, will, fore...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL|            Echobox|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [GRAMMYs]|    NULL| grammys|              Rappler|         Philippines|The Social News N...|  2011-07-07|       3516624|         409|           7964|         True|Did your favorite...|     False|     NULL|   NULL|         NULL|    NULL|[Did, your, favor...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL| Twitter for iPhone|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|[WizkidRonaldoDJN...|    NULL| grammys|           oluwazhini|      Lagos, Nigeria|*creative choreog...|  2019-09-04|            77|         135|           7518|        False|🎵; eh God by @Ki...|     False|     NULL|   NULL|         NULL|    NULL|[🎵;, eh, God, by...|
# |NULL|2021-11-27|   NULL|           NULL|NULL|NULL|      NULL|        NULL|     NULL|      NULL|          NULL|NULL| Twitter for iPhone|     NULL|       NULL|    NULL|       NULL| NULL|          NULL|       NULL|            NULL|         NULL|          NULL|       NULL| NULL|           [GRAMMYs]|    NULL| grammys|     Fadhil Ramadhani|Jakarta Capital R...|Views and opinion...|  2009-09-26|           131|         231|           2067|        False|Just saying it ri...|     False|     NULL|   NULL|         NULL|    NULL|[Just, saying, it...|
# +----+----------+-------+---------------+----+----+----------+------------+---------+----------+--------------+----+-------------------+---------+-----------+--------+-----------+-----+--------------+-----------+----------------+-------------+--------------+-----------+-----+--------------------+--------+--------+---------------------+--------------------+--------------------+------------+--------------+------------+---------------+-------------+--------------------+----------+---------+-------+-------------+--------+--------------------+
# only showing top 20 rows
#
# Search by Word 'covid' and Location 'New York':
# +---+----+-------+---------------+---+----+----------+------------+---------+----------+--------------+----+------+---------+-----------+--------+-----------+-----+--------------+-----------+----------------+-------------+--------------+-----------+-----+--------+--------+--------+---------+-------------+----------------+------------+--------------+------------+---------------+-------------+----+----------+---------+-------+-------------+--------+
# |url|date|content|renderedContent| id|user|replyCount|retweetCount|likeCount|quoteCount|conversationId|lang|source|sourceUrl|sourceLabel|outlinks|tcooutlinks|media|retweetedTweet|quotedTweet|inReplyToTweetId|inReplyToUser|mentionedUsers|coordinates|place|hashtags|cashtags|category|user_name|user_location|user_description|user_created|user_followers|user_friends|user_favourites|user_verified|text|is_retweet|timestamp|symbols|company_names|verified|
# +---+----+-------+---------------+---+----+----------+------------+---------+----------+--------------+----+------+---------+-----------+--------+-----------+-----+--------------+-----------+----------------+-------------+--------------+-----------+-----+--------+--------+--------+---------+-------------+----------------+------------+--------------+------------+---------------+-------------+----+----------+---------+-------+-------------+--------+
# +---+----+-------+---------------+---+----+----------+------------+---------+----------+--------------+----+------+---------+-----------+--------+-----------+-----+--------------+-----------+----------------+-------------+--------------+-----------+-----+--------+--------+--------+---------+-------------+----------------+------------+--------------+------------+---------------+-------------+----+----------+---------+-------+-------------+--------+
