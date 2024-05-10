# PostgreSQL
PostgreSQL, often referred to as Postgres, is one of the most advanced open-source database management systems. It originated as a scientific project at the University of California, Berkeley, in the 1980s, with its first version released in 1996. Since then, thanks to continuous development supported by an active and committed community, PostgreSQL has become a highly respected solution for enterprises and individual users worldwide.

PostgreSQL is an advanced open-source database management system. It supports advanced data types, extensibility, ACID transactions support, high availability and fault tolerance, SQL compliance, and offers a wide range of security options.

## PostgreSQL Basics
### Basic Commands
- `psql`: a command-line tool for PostgreSQL, enabling interaction with the database.
- `CREATE DATABASE database_name;`: creates a new database.
- `DROP DATABASE database_name;`: deletes a database.
- `CREATE TABLE table_name (column1 type1, column2 type2, ...);`: creates a new table.
- `DROP TABLE table_name;`: deletes a table.
- `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);`: inserts data into a table.
- `SELECT * FROM table_name;`: selects and displays all records from a table.
- `UPDATE table_name SET column1 = value1 WHERE condition;`: updates data in a table.
- `DELETE FROM table_name WHERE condition;`: deletes data from a table.

### Connecting to the Database – Client Tool**

psql: An interactive command-line tool for PostgreSQL, allowing connection to the database, executing queries, and managing the database. To connect, use the command `psql -h host -p port -U user -d database`.

### Useful Meta-Commands

- `\?`: Displays help about psql meta-commands.
- `\c [database] [user]`: Connects to another database as a different user.
- `\dt`: Displays a list of tables in the current database.
- `\l`: Displays a list of all databases.
- `\d [table_name]`: Shows the structure of a table (columns, data types, etc.).

### PostgreSQL Directory Structure
- **Data Directory (`PGDATA`)**

    This is the main directory where database data is stored, including configuration files (postgresql.conf, pg_hba.conf, and pg_ident.conf), log files, table data files, and indexes. This is the heart of the PostgreSQL installation, where all important data is stored and managed.
- **Bin Directory**

    Contains PostgreSQL executable files, including psql, the database server (postgres), and tools for administration and maintenance, such as pg_dump (for creating backups) and pg_restore (for restoring from backups).
- **Log Directory**

    Often located within PGDATA, but can be configured to use a different location. Stores log files, where database operations, warnings, and errors are recorded.
- **Lib Directory**

    Contains shared libraries used by PostgreSQL, including extension modules that can be added to the database.
- **Config Files**

    In the data directory (PGDATA), there are key configuration files. postgresql.conf allows for the configuration of most aspects of the database server's operation, pg_hba.conf controls authentication and authorization, and pg_ident.conf manages the mapping of user identifiers.

### PostgreSQL Cluster
The PostgreSQL cluster, in the context of database management, refers to a group of database servers working together to provide greater performance, reliability, and scalability. The components of a PostgreSQL cluster can vary depending on the needs and architecture of the system. Below I present the main elements that make up a PostgreSQL cluster:
- **Database Server (Database Server)**

This is the fundamental element of every cluster, consisting of one or more physical servers or virtual instances on which PostgreSQL software operates. Each database server stores part or all of the data and handles queries to the database.
- **Replication**

The replication mechanism allows for copying data from one database server (master) to one or more servers (slaves). PostgreSQL offers several replication methods, such as logical replication and streaming replication, to ensure data redundancy, high availability, and distribution of read query load.
- **Cluster Management**

Various tools can be used to manage the PostgreSQL cluster, which help automate deployment, configuration, monitoring, and scaling management. Examples of such tools include Patroni, PgBouncer, Pgpool-II, and others.
- **Load Balancer**

A load balancer is used to distribute incoming queries to the cluster among different servers to optimize resource usage and ensure high availability. This can be software or hardware.
- **Data Storage**

Refers to the physical or virtual data storage, such as hard drives, SSDs, or cloud-based solutions, where database data is stored.
- **Monitoring and Alerting**

Monitoring systems, such as Prometheus in combination with Grafana or Zabbix, are crucial for efficient management of the PostgreSQL cluster. They allow for tracking performance, system health, and other key metrics in real-time and sending alerts in case of detected problems.
- **Backup and Restoration**

Backup and restoration strategies are essential for ensuring the continuity of operations and data security in the PostgreSQL cluster. They can include cold backups, hot backups, and checkpoints.
- **Security**

Includes the configuration of security at the network level (firewalls, VPN), authentication and authorization of access to the database, encryption of data in transit and at rest, and management of patches and software updates.
- **Scalability**

The cluster must be designed with scalability in mind, both vertically (by adding resources to existing servers) and horizontally (by adding additional servers to the cluster).

## Advanced Topics
### High-Level Architecture of PostgreSQL Database
The architecture of PostgreSQL is based on the client-server model. The database server manages the database files, accepts queries from multiple clients simultaneously, processes these queries, and returns the results. Clients can connect to the server using a network interface or through a local file system interface.

- **Server Processes**

Each client connection to the PostgreSQL server is handled by a separate server process. This model of isolated processes ensures safety and stability, as errors in one process do not directly affect other processes.
- **Data Storage**

PostgreSQL uses its own file management system, storing data in files within the data directory known as PGDATA.
- **MVCC (Multiversion Concurrency Control)**

A mechanism of multiversion concurrency control that allows for reading data without blocking them and writing without disrupting reads, ensuring high performance and scalability.

### Connecting to the Database and `work_mem` Memory

- **Connecting to the Database**

A client connects to the PostgreSQL server, and the server creates a new server process (backend) to handle this connection. Various methods can be used for authenticating clients, such as password, Kerberos, or SSL certificates.
- **`work_mem Memory`**

The work_mem parameter specifies the amount of memory that can be used by a single operation, such as sorting or join operations, within a single query. Optimal configuration of work_mem is crucial for performance, as too low a value may lead to frequent disk usage, and too high a value to excessive consumption of server memory.

### Query Processing
- **Parsing**

The query is analyzed syntactically and semantically, checking the correctness of syntax and the availability of referenced objects.
- **Optimization**

The query planner selects the most efficient way to execute the query, creating an execution plan. This process takes into account data statistics and various data access strategies.
- **Execution** 

`pg_stat_statements` is an extension in PostgreSQL that provides a way to track execution statistics of all SQL statements executed by a database server. It's invaluable for performance monitoring and analysis, helping database administrators (DBAs) identify slow or inefficient queries that might be affecting the database performance.

### File and Page Structure
- **PGDATA**
The PGDATA directory in PostgreSQL contains all the data, configurations, and log files necessary for the database operation. Here are the main directories and files typically found in PGDATA:
    - `base`

    Contains the data of all databases. Each database has its own subdirectory inside this directory, identified by OID (Object Identifier).
    - `global`

    Stores global data, such as user roles and permissions information, which are common to the entire PostgreSQL cluster.
    - `pg_wal` (in older versions pg_xlog)

    Contains the Write-Ahead Logging (WAL) transaction logs. These files are crucial for data recovery and replication.
    - `pg_multixact`

    Stores information about multi-transaction states used for managing shared row-level locks.
    - `pg_subtrans`

    Contains information about subtransactions that are part of larger transactions.
    - `pg_tblspc`

    Contains symbolic links to tablespaces that may be located outside the main data directory. Tablespaces allow storing database data on different storage devices.
    - `pg_twophase`

    Stores data about transactions that are in the process of preparing for a two-phase commit.
    - `pg_commit_ts` and `pg_replslot`

    Contain information used for replication and tracking commit timestamps.
    - `pg_dynshmem`

    Stores data related to dynamic shared memory used by PostgreSQL processes.
    - `pg_notify`

    Contains information about LISTEN/NOTIFY notifications.
    - `pg_serial`

    Stores information used for optimizing access to sequences.
    - `pg_snapshots`

    Contains saved data snapshots used in specific operations.
    - `pg_stat` and `pg_stat_tmp`

    Store statistical data about the database's operation, which can be used for monitoring and optimization.
    - `postgresql.conf`

    The main configuration file for the PostgreSQL database.
    - `pg_hba.conf`

    The access control configuration file, specifying which user roles can connect to the database, from what addresses, and with what authentication methods.
    - `pg_ident.conf`

    The identifier mapping configuration file, allowing the mapping of external user names to database roles.
- **Page Structure**: PostgreSQL stores data in 8KB blocks.

    - `Data Pages`
    
    PostgreSQL stores data in 8KB blocks (by default), known as pages. The page structure includes a header that stores metadata, and a data segment where records are actually stored.
    - `Row-level Locking`
    
    Thanks to MVCC, PostgreSQL locks at the row level, minimizing conflicts with concurrent data access.

## Administration and Management
### Creation and Configuration

- **Creating PGDATA**

    Data Directory (PGDATA): During the installation of PostgreSQL, the data directory is automatically created or specified by the administrator. This is where PostgreSQL stores its data files, including databases, configuration files, and logs. The location of PGDATA can be specified during the database initialization by using the initdb command, which prepares the data directory for first use.

- **Creating a Database – CREATE DATABASE**

    Basic Database Creation: A new database can be created using the command CREATE DATABASE database_name;. This command creates a database with default settings, based on the template1 template.

    Database from Template: PostgreSQL allows for the creation of a database from an existing template. For example, if you want to create a database with a full set of objects from another database, you can use the command CREATE DATABASE new_database TEMPLATE existing_database;.

    CREATEDB Permission: To allow a user (role) to create databases, you must grant them the CREATEDB permission. This can be done while creating a user (CREATE USER user_name CREATEDB;) or by modifying an existing user (ALTER USER user_name CREATEDB;).

- **Creating Schemas – CREATE SCHEMA**

    Basic Schema Creation: Schemas in PostgreSQL are used to organize and separate namespaces within the database. You can create a schema using the command CREATE SCHEMA schema_name;.

    search_path: The search_path parameter specifies the order in which PostgreSQL looks for objects (tables, functions, etc.) not specified by a full path. You can set this parameter to indicate which schemas should be searched by default, e.g., SET search_path TO schema1, schema2;.

- **Creating Users/Roles – CREATE USER/CREATE ROLE**

    Creating a User: PostgreSQL manages database access through users (roles with login capability). A user can be created with the command CREATE USER user_name WITH PASSWORD 'password';. This command creates a role that can be used to connect to the database.

    Creating a Role: Roles in PostgreSQL are used to group permissions for one or more users. A role can be created without login capability if it is only to manage permissions, using the command CREATE ROLE role_name;.

    Permissions and Roles: After creating roles and users, you can manage permissions using the GRANT and REVOKE commands to control access to the database, tables, views, etc.

- **Database Parameters – ALTER SYSTEM/DATABASE/ROLE and SET Commands**

    ALTER SYSTEM: Allows changing the global configuration settings of the database server, which are saved in the postgresql.auto.conf file. Usage example: ALTER SYSTEM S ET parameter = 'value';. A restart of the PostgreSQL server is required for the changes to take effect.

    ALTER DATABASE: Enables changing settings for a specific database, allowing for configuration adjustment at the database level. Example: ALTER DATABASE database_name SET parameter = 'value';.

    ALTER ROLE: Used to change settings related to a specific role or user, e.g., settings regarding session time limits. Example: ALTER ROLE user_name SET parameter = 'value';.

    SET: Used to change settings in the current session. Example: SET parameter TO 'value';. This is useful when we want to temporarily modify the database behavior without making permanent changes to the configuration.

- **Remote Access Configuration**
    - `pg_hba.conf`

    A configuration file that controls client authentication. Administrators can specify which IP addresses can connect to the database, what methods of authentication to use (e.g., password, peer, md5), and which databases are available to users.
    - `listen_addresses`

    A parameter in the postgresql.conf file that specifies on which network interfaces the PostgreSQL server listens for connections. To enable remote access, the listen_addresses value should be set to '*' or a specific server IP address.

- **pg_service.conf**

    pg_service.conf: A file that allows defining aliases for database connections, simplifying the process of connecting to different servers and databases. Users can specify connection parameters for each "service", and then connect to the database using the service name with the command psql -service=service_name.

- **Tablespaces**

Tablespaces in PostgreSQL are a feature that allows storing data in specified locations on disk. This facilitates better management of physical data storage, e.g., by separating operational data from historical data onto different disks or partitions.
- Creating Tablespaces
    
To create a new tablespace, use the command CREATE TABLESPACE tablespace_name OWNER owner LOCATION 'directory_path';. This operation requires specifying the tablespace name, owner (usually a role), and the path to the directory on the disk where the data will be stored.
- Using Tablespaces
    
When creating a new table or index, you can specify in which tablespace the object's data should be stored, using the TABLESPACE tablespace_name clause. For example: CREATE TABLE table (column1 type1, column2 type2) TABLESPACE tablespace_name;.
- Managing Tablespaces
    
PostgreSQL allows modifying and deleting tablespaces, but these operations should be performed cautiously to avoid data loss. Deleting a tablespace is possible only if it contains no objects.

### Tools and Mechanisms
- **Physical Backup of PostgreSQL – ARCHIVE MODE and pg_basebackup**
    A physical backup involves copying the database files from the disk, which enables quick restoration of the entire database system to the state at the time of the backup.
    - `ARCHIVE MODE`

        To enable complete backups and restoration of the database, PostgreSQL must operate in archiving mode (ARCHIVE MODE). This mode allows for the recording of all changes in WAL logs (transaction logs), which is essential for restoring the database to any point in time (Point-In-Time Recovery, PITR).
        It is activated by changing the archive_mode parameter to on in the postgresql.conf configuration file and specifying the archiving method in the archive_command parameter.
    - `pg_basebackup`

        The pg_basebackup tool is used to create secure physical copies of the entire database. These copies can be used to restore the database on the same or a different server.
        It allows for creating backups on the fly, without the need to stop the database, which is crucial for production systems.

- **Logical Backup – pg_dump, pg_dumpall, and pg_restore**

    A logical backup allows for a more flexible approach to creating backups, enabling the selection of specific databases, tables, or even individual rows for saving in SQL format or other formats, which can then be used to restore data.
    - `pg_dump`

        The pg_dump tool is used for backing up individual databases. It allows selecting the format of the backup file (e.g., SQL, custom, directory), facilitating later data restoration.
        Usage example: pg_dump -U username -d database_name -f backup_file.sql.
    - `pg_dumpall`
    
        The pg_dumpall tool is used for backing up all databases in the PostgreSQL system, including roles and permission information. This is useful, especially during the migration of the entire database server.
        The generated SQL file can then be used to restore the state of the entire PostgreSQL cluster.
    - `pg_restore`

        The pg_restore tool is used to restore data from backups created by pg_dump in formats other than SQL (e.g., custom, directory). It enables selective restoration of specific objects from a backup.
        Usage example: pg_restore -U username -d database_name -1 backup_file.

    The choice between physical and logical backups depends on the system requirements, database size, and backup policy. Physical backups are usually quicker to restore but less flexible. Logical backups offer greater flexibility but can be more time-consuming when restoring large databases. A good practice is to use both methods to ensure comprehensive data security.

- **Shared Memory**

    In the context of an operating system, shared memory allows different processes to access a common address space. Instead of each process having its own, isolated memory space, shared memory segments are available to multiple processes. This mechanism is managed by the operating system, which ensures synchronization of access to memory to avoid conflicts and ensure data consistency.
    - `Shared Buffer`

    The shared buffer in PostgreSQL is a critical component of the database's memory architecture, designed to minimize disk I/O by caching table blocks and indexes. This cache resides in shared memory and is accessible to all database server processes. The mechanism plays a pivotal role in the system's performance by keeping frequently accessed data in RAM, reducing the need for disk reads.

    How the Shared Buffer Works

    When a query requests data, PostgreSQL first checks the shared buffer cache. If the data is found there (a "cache hit"), it can be returned immediately, significantly speeding up the query. If the data is not in the cache (a "cache miss"), it must be read from disk and loaded into the shared buffer. Because accessing data from RAM is much faster than from disk, a high cache hit ratio is crucial for good database performance.

    `Background Writer (bgwriter)`

    The background writer (bgwriter) is a process that helps in reducing the I/O load on the system. It asynchronously writes back dirty (modified) pages from the shared buffer to disk. Dirty pages are those that have been modified in memory but not yet written to disk. The bgwriter process is configured to periodically write these pages to disk, which helps smooth out disk I/O and avoid spikes of write activity. It also ensures that pages are written to disk before they are needed to be evicted from the cache for making room for new pages, thereby avoiding synchronous writes that would stall query processing.

    `Checkpoints`

    Checkpoints are another essential mechanism in PostgreSQL, related to the shared buffer and data durability. A checkpoint is a point in time at which all dirty pages in the shared buffer are written to disk, and the transaction log (WAL) is flushed. This ensures that the database can recover to a consistent state in the event of a crash by replaying the WAL from the last checkpoint.

    Checkpoints occur at configured intervals (specified in the postgresql.conf file) or when the WAL grows beyond a certain size. While necessary for data integrity and recovery, checkpoints can cause a significant I/O load, as many pages may need to be written to disk simultaneously. PostgreSQL includes several settings to manage the impact of checkpoints, such as configuring the maximum amount of WAL to accumulate between checkpoints (checkpoint_segments or max_wal_size in newer versions) and the amount of time the checkpoint spread over (checkpoint_completion_target), aiming to balance between data safety and system performance.
    - `wal buffer`

    In PostgreSQL, the WAL (Write-Ahead Logging) buffer is a crucial component of the WAL mechanism, which aims to ensure data integrity and support recovery operations. WAL is a central aspect of database systems that ensures all transactions are recorded in a transaction log before they are actually committed to the database. This allows for the recovery of all committed transactions that may not have been fully written to disk in the event of a system failure.

    How Does the WAL Buffer Work?

    - Transaction Logging: When a transaction is performed, all changes it introduces are first recorded in the WAL buffer, which is located in RAM. This is a fast operation since it does not require direct disk access at this point.

    - Flush to WAL on Disk: The contents of the WAL buffer are periodically flushed to the physical WAL file on disk. A flush operation can be triggered by various events, such as the commit of a transaction, exceeding a certain data limit in the buffer, or as part of a regular cleanup process.

    - Data Recovery: In case of a failure, the PostgreSQL recovery system uses the WAL records on disk to reconstruct all transactions that were committed but might not have been fully written to the database's data files before the crash.

    Managing WAL in PostgreSQL

    Database administrators can configure WAL behavior through various settings in the postgresql.conf configuration file, such as the size of the WAL buffer, flush policy, and WAL archiving configuration. This allows for tuning the system's performance and reliability to meet specific application and environment requirements.
    - `Locks`
    
    PostgreSQL uses a locking mechanism to manage access to data and resources, preventing conflicts and ensuring transaction integrity. Locks are stored in shared memory, enabling quick coordination between processes.
    Server State Information: Such information as connection registration, query execution statistics, and information about current transactions are stored in shared memory, enabling efficient analysis and system management.
    - `Shared Buffer Cache`
    
    This is a central repository for data blocks read from disk. Thanks to shared memory, different server processes can access the same data in memory without the need to reload it from disk.

## Security and Performance
- **Secure Password Changes, Storage, and the .pgpass File**
    Changing passwords should be done through a secure connection (e.g., SSL) or locally, to avoid password interception over the network. Use the command ALTER USER user_name WITH PASSWORD 'new_password';.
    .pgpass: A file in the user's home directory (~/.pgpass on Linux/Unix and %APPDATA%\postgresql\pgpass.conf on Windows) storing passwords in the format: hostname:port:database:username:password. This allows for automatic authentication without the need to enter a password with each connection.

- **Auditing Access and User Behavior – pgAudit**

    `pgAudit`: The pgAudit extension provides detailed auditing capabilities at the PostgreSQL server level. It allows tracking who made changes to data or database configuration and when, which is crucial for security and regulatory requirements.
    Installing pgAudit requires attaching the extension to the database and configuring parameters in the postgresql.conf file and possibly pg_hba.conf for detailed access control.
    Once configured, audited actions are logged in the server logs, enabling analysis of access and changes to data.

- **Performance Testing Tool – pgbench**

    `pgbench`: Is the standard performance testing tool for PostgreSQL, allowing for database load simulation by performing a series of defined operations.
    This enables the assessment of database server performance under various loads, useful for capacity planning and performance optimization.
    pgbench can be used for conducting both simple tests and more complex scenarios, simulating real user conditions.

- **pg_catalog**

    A special schema within PostgreSQL that contains the system catalog tables and views. These system catalogs are essentially the metadata about the database, detailing its structure and objects such as tables, columns, indexes, and functions. In other words, pg_catalog houses the information PostgreSQL needs to understand its own operation and the user-defined objects it contains.

- **Table Defragmentation – VACUUM, AUTOVACUUM and VACUUM FULL**
    - `VACUUM`
    
    The VACUUM command is used to reclaim space taken by "dead" rows that resulted from deleting or updating records. This improves query performance and disk space management.
    Reclaims space occupied by dead rows, allowing it to be reused by new rows.
    Does not block read or write operations on the table during its operation.
    Is the preferred method for maintaining database performance without impacting data availability.
    - `AUTOVACUUM`
    
    PostgreSQL also offers the AUTOVACUUM mechanism, which automatically triggers the VACUUM process in the background without user intervention, helping maintain optimal performance and space management.
    - `VACUUM FULL`

    In addition to the functions offered by VACUUM, VACUUM FULL thoroughly cleans the table, freeing up disk space and returning it to the operating system.
    This causes table locking during operation, which can affect system availability.
    Is used less frequently, mainly in situations where maximum disk space recovery is necessary.

### Backup
A standby database in PostgreSQL, and generally in database management systems, refers to a copy of the primary database that is kept up-to-date either through continuous streaming of changes (streaming replication) or by applying changes at regular intervals (log shipping). Standby databases are primarily used for redundancy, disaster recovery, and load balancing of read queries.
Types of Standby Databases in PostgreSQL
- **Hot Standby**
    
    A hot standby system allows the standby database to accept read-only queries while it is being updated with changes from the primary database. This not only provides a high availability solution but also helps in distributing the query load. Hot standby is facilitated by streaming replication, where changes are sent in real-time from the primary to the standby server.
- **Warm Standby** 
    
    In a warm standby configuration, the standby server is not available for queries. It is simply kept up-to-date with the primary database and can be quickly promoted to a primary role if the current primary server fails. This setup is less resource-intensive than a hot standby but doesn't offer the same level of service availability or load distribution.

Use Cases for Standby Databases

- High Availability: Standby databases are a cornerstone of high availability setups. In the event of a primary database failure, the standby can be promoted to become the new primary, ensuring minimal downtime.

- Disaster Recovery: Standby databases can be located in different geographical locations. In case of a site-wide disaster, the remote standby database can ensure that data is not lost and that services can be restored quickly.

- Read Scalability: Hot standby databases can handle read queries, thus offloading the primary database and improving the application's overall performance. This is particularly useful for read-heavy applications.

- Backup: Although not a replacement for traditional backups, standby databases can be used for creating backups without affecting the performance of the primary database. This is because backups can be taken directly from the standby database.

Managing Standby Databases

Creating and managing a standby database in PostgreSQL involves setting up replication from the primary database, monitoring the replication lag to ensure that the standby is keeping up with the primary, and managing failovers when the primary database is not available. PostgreSQL offers several tools and settings for managing standby databases, such as the recovery.conf configuration file for controlling the standby server's behavior and various replication modes to balance between performance and data freshness.

### Optimalization
Optimizing PostgreSQL performance involves tuning a variety of configuration parameters to better match your hardware and workload. The impact of these adjustments can be significant, but it's essential to test changes in a development environment before applying them in production, as the optimal settings can vary widely depending on specific use cases. Here are some fundamental parameters that commonly affect PostgreSQL performance, along with a rough idea of the resources they might require:
1. `shared_buffers`

    Description: Sets the amount of memory the database server uses for shared memory buffers.
    Performance Impact: Increasing shared_buffers can significantly improve database performance, especially for read-heavy workloads, by reducing disk I/O.
    Resource Consideration: Typically set to around 25% to 40% of the total system memory on a dedicated database server. Going beyond this might not yield better performance due to diminishing returns and the effectiveness of the operating system's cache.
2. `work_mem`

    Description: Determines the amount of memory used for internal sort operations and hash tables before writing to temporary disk files.
    Performance Impact: Increasing work_mem allows PostgreSQL to perform more operations in memory, which can speed up queries that require sorts or joins. However, setting it too high can lead to excessive memory consumption if many queries are running simultaneously.
    Resource Consideration: work_mem is allocated per sort/join operation, so its total impact depends on the number of concurrent operations. It's often started at a few megabytes but may be increased based on workload and available memory.
3. `maintenance_work_mem`

    Description: Specifies the maximum amount of memory for maintenance operations, such as VACUUM, CREATE INDEX, and ALTER TABLE ADD FOREIGN KEY.
    Performance Impact: Higher values can make maintenance operations faster, which is particularly beneficial for large databases.
    Resource Consideration: This setting can be higher than work_mem, as maintenance operations are less frequent. A good starting point might be around 10% of the total system memory.
4. `wal_buffers`

    Description: Determines the amount of memory used for WAL (Write-Ahead Logging) records before writing them to disk.
    Performance Impact: Increasing wal_buffers can reduce disk I/O for transaction logs, improving write performance.
    Resource Consideration: The default setting is typically adequate for most workloads, but it can be increased up to 16MB if you have a high write workload and sufficient memory.
5. `effective_cache_size`

    Description: Gives the planner an estimate of the effective size of the disk cache that is available to a single query.
    Performance Impact: Setting this value appropriately can help the query planner choose more efficient query plans.
    Resource Consideration: This is not a direct memory setting but informs the planner about available memory. Setting this to about 50%-75% of the total system memory is a common recommendation.
6. `checkpoint_segments/max_wal_size`

    Description: Controls the maximum size of WAL files between automatic WAL checkpoints.
    Performance Impact: Increasing these settings allows more transactions to occur between checkpoints, reducing the I/O load associated with checkpoints but at the risk of longer recovery times.
    Resource Consideration: Higher settings require more disk space for WAL storage. The choice should balance between write performance and recovery time/disk space considerations.