# Task
1. Building a virtual machine or a Linux container.
2. Installing PostgreSQL and creating a database.
3. Loading data into the database with a Python script. 

# Solution
## Building a virtual machine or a Linux container
1. Choosing a container as the project's foundation, where Ubuntu version 22.04 was installed.

    To achieve this, I wrote a Dockerfile recipe, which creates a container image based on Ubuntu version 22.04, with a PostgreSQL database server installed.

    1. `FROM ubuntu:22.04`

        Begins the image build from the base image of Ubuntu version 22.04. This is the starting point for all subsequent instructions.

    2. `RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql`

        Executes package index update using apt-get update, then installs the PostgreSQL database server without interactive queries (sets DEBIAN_FRONTEND=noninteractive), which is useful when building Docker images where manual response to installer questions is not possible.

    3. `USER postgres`

        Changes the user executing commands to postgres, which is the default user for PostgreSQL. This ensures that when the container is started, the PostgreSQL server runs with appropriate permissions.

    4. `CMD /usr/lib/postgresql/14/bin/postgres --config-file=/etc/postgresql/14/main/postgresql.conf`

        Specifies the default command to be executed when the container is started. In this case, it is starting the PostgreSQL server with a specified configuration file. Note that the PostgreSQL version (here 14) must match the one installed in the previous step. This may require an update if the versions in the Ubuntu repositories have changed.

    5. `EXPOSE 5432`

        Informs Docker that the container will listen on port 5432, which is the default port for PostgreSQL. This does not open the port externally; it only serves as documentation for someone running the container that port 5432 should be forwarded or opened.
    
    ### Starting the container
    1. Save the Dockerfile
        First, save the above code in a file named `Dockerfile` (without extension). Make sure this file is saved in an empty directory, which will be used only for this purpose. For example, let's name this directory psql-basics.

    2. Open a terminal or command prompt
        Navigate to the directory where the Dockerfile is saved using the `cd` command in the terminal (Linux/Mac) or command prompt (Windows).

    3. Build the Docker image
        Run the following command in the terminal, being in the directory with the Dockerfile. Remember to replace psql-basics:1.0 with the name you want to give your image along with the tag:
        ```bash
        docker build -t psql-basics:1.0 .
        ```
        The dot at the end represents the current directory, where Docker looks for the Dockerfile. This command builds the image based on the instructions in the Dockerfile and tags it as `psql-basics:1.0`.

    4. Run the Docker container
        After building the image, you can run a container based on it, using the command:
        ```bash
        docker run -d -p 5432:5432 --name psql-container psql-basics:1.0
        ```
        `-d` runs the container in the background (detached mode),

        `-p` 5432:5432 maps the container's port 5432 to port 5432 on your host machine, allowing connections to PostgreSQL from outside the container,

        `--name my-postgres-container` gives the container a name my-postgres-container for easier management,
        
        `psql-basics:1.0` is the name of the previously built image.

        Remember, you need to have Docker installed on your machine to perform the steps above.

    5. To run commands inside a running container, you need to execute this:
        ```bash
        docker exec -it <container name or ID> psql
        ```
        `docker exec`: This is a Docker command that allows you to run a command inside a running container.

        `-it`: This option is actually two flags combined.
            
        - `-i` or --interactive keeps STDIN open even if not attached. This means you can interact with the command as if it were running in your terminal.
        - `-t` or `--tty` allocates a pseudo-TTY, which makes the container's shell interactive. It simulates a terminal, like what you'd get when you use an SSH session. This is useful for commands that require user interaction or that produce formatted output.

        `<container name or ID>`: This is the name or ID of the Docker container you're targeting with the command. Docker container names and IDs are unique, so this specifies exactly which container you're intending to run your command in.

        `psql`: This is the command being executed inside the container. psql is the interactive terminal for working with PostgreSQL. By running this command, you're starting a PostgreSQL client session connected to a PostgreSQL server. The client will connect using default parameters for the server, database, and authentication, unless these are configured differently in the container environment.

    ### Issues:
    - The Ubuntu image did not have package metadata, so it was necessary to run apt-get update before installing the package.

## Installing PostgreSQL and creating a database

2. After installing PostgreSQL, as documented in the Dockerfile, it was time to create the database and role to proceed with the next step, which is loading data from CSV.
    1. Installing PostgreSQL client locally on the machine from which the Python script will be run:
    ```bash
    sudo apt-get install postgresql-client
    ```
    2. Creating a database and role in PostgreSQL within the container:
    ```bash
    sudo -u postgres psql
    ```
    This command launches the PostgreSQL command-line client, psql, as the system user postgres, who is the default superuser for the PostgreSQL database system. Using sudo -u postgres allows the psql command to be executed with postgres user permissions. This is a common way to access the PostgreSQL database management system for performing administrative tasks.
    ```sql
    create database daria;
    ```
    After launching the psql client, this command creates a new database named "daria". This command must be executed from within the psql client and usually by a user with the appropriate permissions, in this case, postgres, unless permissions have been granted to another user.
    ```sql
    create user daria with encrypted password 'mypass';
    ```
    This command creates a new user (sometimes referred to as a role in PostgreSQL) named "daria" with the password mypass. The password is encrypted before being stored in the database, enhancing security. Creating a user allows for the control of access to the database and its resources by different users.
    ```sql
    grant all privileges on database daria to daria;
    ```
    This command grants all privileges on the database "daria" to the user "daria". This means that "daria" can perform all operations on this database, including creating, modifying, deleting tables and other objects, as well as managing the permissions of other users in the context of this database.

    3. Connecting from the PostgreSQL client on the local machine to the PostgreSQL instance in the container:
    ```bash
    docker run -v ${PWD}/pg_hba.conf:/etc/postgresql/14/main/pg_hba.conf -v ${PWD}/postgresql.conf:/etc/postgresql/14/main/postgresql.conf -d -p 5432:5432 psql-basics:1.0 
    ```
    The command runs a Docker container using the image psql-basics:1.0, configuring it specifically for PostgreSQL server needs by mounting two configuration files from the host to the container and running the container in detached mode, exposing port 5432.
    ```bash
    psql -h 127.0.0.1 daria daria
    ```
    The command launches the PostgreSQL command-line client, psql, to establish a connection with the database.

    ### Issues:
    - Exposing the PostgreSQL server outside the container required setting `listen_addresses = '*'` in `postgres.conf`.
    - Enabling login from outside required setting `host all all 0.0.0.0/0 scram-sha-256` in file `pg_hba.conf`.

## Loading data into the database with a Python script

3. The data chosen for loading into the database was obtained from Kaggle. Specifically, it is a dataset containing Formula 1 drivers: [Kaggle - Formula 1 2010-2021](https://www.kaggle.com/datasets/ahmetburabua/formula-1-20102021).
    1. Initially, create a table for the data
    ```sql
    CREATE TABLE driver
    (
    id integer PRIMARY KEY,
    name character varying(75),
    surname character varying(75),
    nationality character varying(3),
    points float,
    year integer
    );
    ```
    2. Writing a Python script that loads data into the previously created table
        1. Importing necessary libraries
        `import pandas as pd` Imports the Pandas library, enabling data manipulation and analysis.
        `from sqlalchemy import create_engine` Imports create_engine from SQLAlchemy, enabling the creation of a database connection.
        `from os import environ` Imports the environ function from the os module, which allows access to the operating system's environment variables.

        2. Reading authentication data from environment variables:
        ```python
        PG_USER = environ["PG_USER"]
        PG_PASS = environ["PG_PASS"]
        ```
        Reads the PostgreSQL user's name and password from the environment variables.

        This approach ensures that database login details are not hard-coded in the script, enhancing security.

        3. Loading data from a CSV file into a Pandas DataFrame:
        ```python
        df_to_insert = pd.read_csv("data/driver_standings_2010-2021.csv")
        ```
        Loads data from a CSV file into a DataFrame, allowing for further processing.

        4. Creating a connection to the PostgreSQL database:
        ```python
        engine = create_engine(f'postgresql://{PG_USER}:{PG_PASS}@localhost:5432/daria')
        ```
        Creates a database engine using the environment variables for authentication details. The connection URL format specifies the protocol (postgresql), username, password, host address (localhost), port (5432), and database name (daria).

        5. Inserting data from the DataFrame into the database:
        ```python
        df_to_insert.to_sql("driver", con=engine, if_exists='replace')
        ```
        The to_sql method inserts data from the DataFrame into the driver table in the database. If the table exists, it is replaced with new data. This behavior is specified by the if_exists='replace' parameter.

        6. Running the program
        In the terminal, navigate to the directory containing the code and run the command:
        ```bash
        PG_USER=daria PG_PASS=daria python3 csv_loader.py
        ```

    ### Issues:
    - `;` after each query and command in PostgreSQL.
    - Assigning variables in the shell: `variable=value`.
