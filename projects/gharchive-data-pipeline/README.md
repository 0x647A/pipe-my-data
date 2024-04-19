# Task
### Create a data pipeline that:
1.  Will fetch data from https://www.gharchive.org/. 
The data will be downloaded hourly.

2. The data should be aggregated at the repository and user level.

For the `repository`, the structure should look as follows:

- date in the format 2020-01-01-15 where 15 is the hour
- projectID
- projectName
- number of unique users who starred the repository
- unique number of users who forked
- number of created issues
- number of created Pull Requests

For the `user`:

- date in the format 2020-01-01-15  where 15 is the hour
- userID
- userLogin
- number of starred projects
- number of created issues
- number of created pull requests

The data should be fetched using Python.

3. Loading data into the database with a Python script. 

# Solution

## gharchive-downloader.py

1. **Import necessary modules**:
   - `import requests`: Imports the `requests` library for sending HTTP requests in Python.
   - `from datetime import datetime, timedelta`: Imports `datetime` and `timedelta` for date and time manipulation.

2. **Define the `download_gharchive_data` function**:
   - Designed to download GitHub Archive data for a specified hour.
   - `hour`: A parameter expecting a datetime string in `YYYY-MM-DD-HH` format.

3. **Construct the URL**:
   - `url = f"https://data.gharchive.org/{hour}.json.gz"`: Constructs the URL pointing to the `.json.gz` file for the specified `hour`.

4. **Determine the local filename**:
   - `local_filename = url.split('/')[-1]`: Extracts the filename from the URL to save the file locally.

5. **Send an HTTP GET request**:
   - `with requests.get(url, stream=True) as r`: Sends a GET request and streams the response content.

6. **Check for request success**:
   - `r.raise_for_status()`: Checks the response's status code and raises an exception for error codes.

7. **Write the response content to a file**:
   - `with open(local_filename, 'wb') as f`: Opens a file in binary write mode to store the downloaded data.
   - Streams and writes the content in chunks to the file with `for chunk in r.iter_content(chunk_size=8192): f.write(chunk)`.

8. **Return the local filename**:
   - Returns the name of the file where the data has been saved.

9. **Calculate the hour for the download**:
   - `hour = (datetime.now() - timedelta(hours=3)).strftime('%Y-%m-%d-%H')`: Determines the datetime for 3 hours ago, formatted as `YYYY-MM-DD-HH`.

10. **Call the function and print the result**:
    - `downloaded_file = download_gharchive_data(hour)`: Downloads the data for the specified hour.
    - `print(f"Downloaded {downloaded_file}")`: Indicates the name of the downloaded file.

This code downloads data from the GitHub Archive for a specific hour and saves it locally, providing the filename of the downloaded file as output.

## process-data.py

1. **Import the Pandas Library**:
   - `import pandas as pd`: This line imports the Pandas library, which is essential for data manipulation and analysis in Python.

2. **Define the `process_data_with_pandas` Function**:
   - This function is designed to process JSON data, specifically structured for GitHub Archive data, and aggregate it at both repository and user levels.

3. **Read the JSON File**:
   - `df = pd.read_json(filename, lines=True)`: Reads the JSON file specified by the `filename` parameter. The `lines=True` argument indicates that the file is in a JSON Lines format (one JSON object per line).

4. **Extract Repository and User Information**:
   - The next three lines extract specific pieces of data from nested JSON objects within the DataFrame `df` and create new columns:
     - `df['repo_id'] = df['repo'].apply(lambda x: x['id'])`: Extracts the repository ID from the `repo` column.
     - `df['repo_name'] = df['repo'].apply(lambda x: x['name'])`: Extracts the repository name from the `repo` column.
     - `df['user_id'] = df['actor'].apply(lambda x: x['id'])`: Extracts the user ID from the `actor` column.

5. **Aggregate Data for Projects (Repositories)**:
   - `projects_agg = df.groupby('repo_id').agg(...)`: This line groups the DataFrame by repository ID and aggregates various metrics for each repository:
     - `projectID` and `projectName` are extracted directly since they're identical within each group.
     - `uniqueStargazers` counts the number of unique users who starred the repository.
     - `uniqueForks` counts the number of unique users who forked the repository.
     - `issuesCount` counts the number of issues created.
     - `pullRequestsCount` counts the number of pull requests created.

6. **Aggregate Data for Users**:
   - `users_agg = df.groupby('user_id').agg(...)`: Similar to repositories, this line groups the DataFrame by user ID and aggregates various metrics for each user:
     - `userID` and `userLogin` are extracted directly.
     - `starredProjects` counts the number of unique projects the user has starred.
     - `createdIssues` and `createdPullRequests` count the number of issues and pull requests created by the user, respectively.

7. **Return the Aggregated Data**:
   - The function returns two DataFrames: `projects_agg` and `users_agg`, which contain aggregated data at the repository and user levels, respectively.

8. **Call the Function**:
   - `process_data_with_pandas('2024-04-07-15.json.gz')`: Calls the `process_data_with_pandas` function with a filename. This example uses a file named `2024-04-07-15.json.gz`, which is assumed to be in the JSON Lines format containing GitHub Archive data.

This code demonstrates how to process and aggregate GitHub Archive data using Pandas, focusing on repository and user activities.

### Fun fact!

After running this code, one gz data package was processed for about 2 hours

```bash
└─$ time python3 process-data.py

real    6269.37s
user    6266.74s
sys     3.11s
cpu     100%
```

## create-tables.sql

The provided code consists of two SQL `CREATE TABLE` statements, which are used to define the structure of two tables: `projects` and `users`. These tables are intended to store aggregated data related to GitHub projects (repositories) and users, respectively.

1. **Creating the `projects` Table**

- **`CREATE TABLE projects`**: This statement initiates the creation of a table named `projects`.
  
- **Columns**:
  - `projectID BIGINT PRIMARY KEY`: Defines a column named `projectID` that stores a large integer (`BIGINT`). This column is designated as the primary key, meaning it will uniquely identify each row in the table.
  - `projectName TEXT`: Defines a column named `projectName` that stores text, intended for the name of the project.
  - `uniqueStargazers INT`: Defines a column named `uniqueStargazers` to store an integer (`INT`) representing the count of unique users who have starred the project.
  - `uniqueForks INT`: Similar to `uniqueStargazers`, this column stores the count of unique users who have forked the project.
  - `issuesCount INT`: Stores the count of issues created in the project.
  - `pullRequestsCount INT`: Stores the count of pull requests created in the project.

2. **Creating the `users` Table**

- **`CREATE TABLE users`**: This statement initiates the creation of a table named `users`.
  
- **Columns**:
  - `userID BIGINT PRIMARY KEY`: Defines a column named `userID` with the same properties as `projectID` but for users.
  - `userLogin TEXT`: Stores the login name of the user.
  - `starredProjects INT`: Counts the number of projects that the user has starred.
  - `createdIssues INT`: Counts the number of issues created by the user.
  - `createdPullRequests INT`: Counts the number of pull requests created by the user.


This SQL code is designed to set up a database schema for storing and querying aggregated data on GitHub projects and user activities. Each table is structured to hold key metrics that provide insights into the popularity and contribution patterns related to repositories and users on GitHub.
The database that will be used to store data is Postgres, which I configured in this project: [psql-basics](../psql-basics/README.md)

### Issues

```bash
psycopg2.errors.InsufficientPrivilege: permission denied for table projects
```
The error message you're encountering, psycopg2.errors.InsufficientPrivilege: permission denied for table projects, suggests that the database user you're using to connect to your PostgreSQL database does not have the necessary permissions to access or modify the projects table.

This problem can be resolved by granting the appropriate permissions to the user. The specific permissions you need to grant depend on the operations you wish to perform on the projects table. For example, if you need to perform SELECT, INSERT, UPDATE, and DELETE operations, you would need to grant those specific privileges.

You can switch the user using the following SQL command:
```sql
set role daria;
```

## load-to-db.py

This Python code demonstrates how to insert data into a PostgreSQL database using the `psycopg2` library. It is intended for inserting aggregated data into two tables: `projects` and `users`. Here's a step-by-step explanation:

1. **Import psycopg2 Library**

    - **`import psycopg2`**: Imports the `psycopg2` library, which is a PostgreSQL adapter for Python. This library allows for connecting to and interacting with PostgreSQL databases from Python code.

2. **Define the `load_data_to_db` Function**

    - The name of the function suggests that it is responsible for loading previously aggregated data into the database.

3. **Establish Database Connection**

    - **`conn = psycopg2.connect(...)`**: Establishes a connection to a PostgreSQL database. The connection parameters such as `dbname`, `user`, `password`, and `host` need to be replaced with actual values specific to the target database.
  
    - **`cur = conn.cursor()`**: Creates a cursor object using the connection. This cursor is used to execute SQL commands.

4. **Insert Data into the `projects` Table**

    - **Iterate over `projects_agg` DataFrame**: The code iterates through each row of the `projects_agg` DataFrame (which is assumed to have been defined earlier and contains aggregated project data).
    
    - **`cur.execute(...)` for `projects`**: For each row in `projects_agg`, an SQL `INSERT` command is executed to insert the data into the `projects` table. If a conflict on the `projectID` occurs (meaning the record already exists), the existing record is updated with the new values.
    
    - The SQL command uses placeholders (`%s`) for parameters to prevent SQL injection, and the actual values are supplied via a tuple that follows the command string.

5. **Insert Data into the `users` Table**

    - **Iterate over `users_agg` DataFrame**: Similarly, the code iterates through each row of the `users_agg` DataFrame, which contains aggregated user data.
    
    - **`cur.execute(...)` for `users`**: Executes an SQL `INSERT` command for each row in `users_agg` to insert data into the `users` table. It follows the same conflict resolution strategy as with `projects`, updating existing records if necessary.

6. **Commit Transactions and Close Connection**

    - **`conn.commit()`**: Commits all executed transactions to the database. This is necessary for the changes to be saved.
    
    - **`cur.close()`, `conn.close()`**: Closes the cursor and the connection to the database, releasing resources.

This code is designed for batch processing and inserting or updating records in a PostgreSQL database. It is useful for scenarios where aggregated data needs to be persisted in a structured format, enabling efficient data storage and retrieval. The use of `psycopg2` and parameterized SQL queries ensures safe and efficient database operations.

### Issues

1. You must be logged in to the correct database, in this case use the command:
```sql
\c <database name>
```

2. `psycopg2.ProgrammingError: can't adapt type 'dict'`

The error message psycopg2.ProgrammingError: can't adapt type 'dict' typically occurs when you're using the psycopg2 library in Python to interact with a PostgreSQL database, and you attempt to pass a Python dictionary directly to a SQL query without proper adaptation. psycopg2 does not know how to handle Python dictionaries by default as it expects data types that it can map directly to SQL types.

## main.py

The provided Python code outlines a basic workflow for downloading, processing, and loading GitHub Archive data into a database. It is structured into a main script that coordinates the flow between three key operations, each handled by a separate module. Here's a breakdown of the code in English:

1. **Import Modules**

    - `import gharchive_downloader`: Imports a custom module named `gharchive_downloader`, which is presumably responsible for downloading data from the GitHub Archive.
    - `import process_data`: Imports the `process_data` module, which likely contains functions for processing or transforming the downloaded data.
    - `import load_to_db`: Imports the `load_to_db` module, which is expected to handle the insertion of processed data into a database.

2. **Define the `main` Function**

    - The `main` function encapsulates the workflow of the script. It serves as the entry point for the operations that download, process, and load the data.

3.  **Workflow Steps**

    1. **Download GitHub Archive Data**:
        - `filename = gharchive_downloader.download_gharchive_data()`: Calls a function from the `gharchive_downloader` module to download data from the GitHub Archive. The function returns the name of the file where the data is saved, which is stored in the variable `filename`.

    2. **Process the Downloaded Data**:
        - `projects_agg, users_agg = process_data.process_data_with_pandas(filename)`: This line calls a function from the `process_data` module, passing the downloaded file's name as an argument. The function is expected to process the data and return two objects: `projects_agg` and `users_agg`, which represent aggregated data for projects (repositories) and users, respectively.

    3. **Load Processed Data into the Database**:
        - `load_to_db.insert_data_into_db(projects_agg, users_agg)`: Calls a function from the `load_to_db` module to insert the processed data into a database. The function takes the aggregated project and user data as parameters.

4. **Run the Script**

    - `if __name__ == "__main__": main()`: This conditional statement checks if the script is being run as the main program and not being imported as a module. If it is the main program, it calls the `main` function to execute the workflow.

This Python script demonstrates a streamlined process for handling data from the GitHub Archive. It utilizes modular programming practices by dividing the workflow into distinct steps (downloading, processing, and loading data) and handling each step in a separate module. This approach enhances the clarity, maintainability, and scalability of the code.
