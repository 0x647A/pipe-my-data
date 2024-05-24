# Project Overview: Tweet Data Processing and Analysis with PySpark

Datasets from: [Kaggle - Covid19_tweets](https://www.kaggle.com/datasets/ziadfellahidrissi/covid19-tweets), [Kaggle - Financial Tweets](https://www.kaggle.com/datasets/davidwallach/financial-tweets), [Kaggle - GRAMMYs tweets](https://www.kaggle.com/datasets/mathurinache/grammys-tweets)

## Project Structure

The project is designed to load, clean, analyze, and search tweet data using PySpark. The project structure is modular, with separate files for each major functionality:

1. **loader.py**: Handles data loading.
2. **data_cleaner.py**: Contains data cleaning methods.
3. **tweet_analyzer.py**: Provides data analysis methods.
4. **tweets_search.py**: Offers search functionalities.
5. **main.py**: Orchestrates the entire process.

## Files and Functionalities

### loader.py

This file contains the `TweetLoader` class responsible for loading datasets from CSV files and combining them into a single DataFrame. Preliminary cleaning is also done in this stage to avoid excessive data loss when handling null values after merging the datasets.

- **TweetLoader Class**:
  - Constants for dataset labels: `COVID_LABEL`, `GRAMMYS_LABEL`, `STOCKERBOT_LABEL`.
  - Methods to load individual datasets: `loadCovid()`, `loadGrammys()`, `loadStockerbot()`.
  - `loadAllDatasets()`: Combines all datasets into a single DataFrame using `unionByName` with `allowMissingColumns=True`.

### data_cleaner.py

This file contains the `DataCleaner` class that provides methods to clean the DataFrame.

- **DataCleaner Class**:
  - `clean_hashtags(df)`: Cleans the `hashtags` column using regex and splits it into a list.
  - `convert_column_types(df)`: Converts date columns to `DateType` and numerical columns to `LongType`.
  - `clean_data(df)`: Applies all cleaning steps to the DataFrame.

### tweet_analyzer.py

This file contains the `TweetAnalyzer` class that provides methods for analyzing the DataFrame.

- **TweetAnalyzer Class**:
  - Constants for column names: `HASHTAG_COLUMN`, `IS_RETWEET_COLUMN`, `SOURCE_COLUMN`, `USER_FOLLOWERS`, `USER_NAME`, `USER_LOCATION`.
  - `count_hashtags()`: Counts occurrences of hashtags.
  - `count_retweets()`: Counts the number of retweets.
  - `count_sources()`: Counts the number of tweets from each source.
  - `avg_followers_per_location()`: Calculates the average number of followers per location.

### tweets_search.py

This file contains the `TweetsSearch` class that provides methods for searching the DataFrame.

- **TweetsSearch Class**:
  - Constants for column names: `TEXT`, `USER_LOCATION`.
  - `search_by_word(word)`: Searches for tweets containing a specific word.
  - `search_by_words(words)`: Searches for tweets containing any of the specified words.
  - `search_by_word_and_location(word, location)`: Searches for tweets containing a specific word from a specific location.

### main.py

This file orchestrates the entire process by creating a Spark session, loading the datasets, cleaning them, performing analysis, and executing searches.

- **Main Script**:
  - Creates a Spark session.
  - Instantiates `TweetLoader`, `DataCleaner`, `TweetAnalyzer`, and `TweetsSearch` classes.
  - Loads and combines datasets.
  - Cleans the combined DataFrame.
  - Performs various analyses and displays the results.
  - Executes searches based on words and locations and displays the results.
  - Stops the Spark session.

## Execution Flow

1. **Loading Data**:
   - The `TweetLoader` class is used to load and combine datasets from CSV files.
   - Preliminary cleaning is performed in the loader to avoid excessive data loss from null values after merging datasets.

2. **Cleaning Data**:
   - The combined DataFrame is cleaned using the `DataCleaner` class, which includes cleaning hashtags and converting column types.

3. **Analyzing Data**:
   - The `TweetAnalyzer` class performs various analyses, such as counting hashtags, retweets, sources, and calculating the average number of followers per location.

4. **Searching Data**:
   - The `TweetsSearch` class provides search functionalities to find tweets based on specific words and locations.

5. **Output**:
   - The results of analyses and searches are displayed using the `show()` method and printed to the console.

## Best Practices and Notes

1. **Order of `show()` and `printSchema()`**:
   - `show()`: This method is a transformation in PySpark that triggers the computation of the DataFrame and displays its content. Since it produces a detailed log, it's better to call this method first.
   - `printSchema()`: This method is a simple Python function that displays the schema of the DataFrame. It should be called after `show()` to avoid getting buried in logs, making it easier to view both outputs sequentially.

2. **Preliminary Cleaning**:
   - Preliminary cleaning is performed in the loader because merging datasets with many null values can result in significant data loss. By handling initial cleaning before merging, we ensure that we retain as much valuable data as possible.

## Usage

To run the project, execute the `main.py` script. Ensure that all necessary CSV files are in the correct paths and that PySpark is properly installed and configured in your environment.

## Benefits

- **Modular Design**: Each functionality is encapsulated in its respective file, making the codebase easy to understand and maintain.
- **Scalability**: New datasets, cleaning methods, analyses, and search functionalities can be easily added.
- **Efficiency**: Leveraging PySpark for processing large datasets ensures high performance and scalability.

This project provides a comprehensive framework for loading, cleaning, analyzing, and searching tweet data using PySpark, making it a robust solution for tweet data processing tasks.
