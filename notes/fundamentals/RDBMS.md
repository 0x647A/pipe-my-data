# RDBMS Fundamentals
RDBMS, which stands for Relational Database Management System, is a type of database management system (DBMS) that stores data in structures known as tables. These tables are interconnected through relationships, facilitating efficient data storage and manipulation. Here are a few key concepts and fundamentals of RDBMS that are worth knowing:

## 1. Tables
The primary data storage structure in an RDBMS is the table. A table consists of rows and columns, where each row represents a single record, and each column represents a specific data field. Every table in the database should have a unique name.

## 2. Keys
- **Primary Key**: A unique identifier for a record in a table. It cannot contain null values, and each value must be unique.
- **Foreign Key**: A column or a set of columns in one table that refers to the primary key of another table. Foreign keys are used to link tables.

## 3. Relationships
RDBMS utilizes relationships between tables to organize data. The most common types of relationships are:
- **One-to-One (1:1)**: Each record in Table A is linked to no more than one record in Table B, and vice versa.
- **One-to-Many (1:N)**: Each record in Table A can be linked to multiple records in Table B, but a record in Table B can be linked to only one record in Table A.
- **Many-to-Many (M:N)**: Records in Table A can be linked to multiple records in Table B and vice versa. This type of relationship typically requires an additional linking table.

## 4. SQL
RDBMS typically uses SQL (Structured Query Language) for creating, modifying, retrieving, and manipulating data. SQL allows for various operations, such as:
- **SELECT**: Retrieving data from the database.
- **INSERT**: Adding new records to a table.
- **UPDATE**: Updating existing records.
- **DELETE**: Removing records.

Structured Query Language used for interacting with relational databases, is based on relational algebra and tuple relational calculus. SQL comprises many types of statements, which can informally be classified as sublanguages. The most commonly distinguished among them are:

- **Data Query Language (DQL)**

    DQL focuses on retrieving data from databases. It is primarily achieved through the SELECT statement, which allows for selecting data from one or multiple tables.

- **Data Definition Language (DDL)**

    DDL includes statements for defining, altering, and deleting database schemas and the objects within them, such as tables, indexes, and views. Typical DDL statements are CREATE, ALTER, and DROP.

- **Data Control Language (DCL)**

    DCL is used to configure and manage SQL database permissions. The main DCL statements are GRANT, which gives specified privileges, and REVOKE, which removes privileges.

- **Data Manipulation Language (DML)**

    DML allows for inserting, updating, deleting, and modifying data in the database. The most well-known DML statements are INSERT, UPDATE, DELETE.

### Additional SQL Components and Commands
- **WHERE**: Specifies a condition for filtering records.
- **LIKE**: Clause in SQL is used to search for a specified pattern in a column, allowing for flexible matching of strings based on wildcard characters.
- **GROUP BY**: Groups rows that have the same values in specified columns into summary rows.
- **HAVING**: Used to filter groups based on a specified condition, often used with the `GROUP BY` clause.
- **ORDER BY**: Specifies the order in which to return the rows.
- **JOIN**: Combines rows from two or more tables based on a related column between them.
- **UNION**: Combines the result sets of two or more `SELECT` statements.
- **INTERSECT**: returns the intersection of two queries (i.e., records that are present in both queries).
- **EXCEPT**: returns the difference between two queries (i.e., records from the first query that are not present in the second query).
- **DROP**: Deletes an entire table, a view of a table, or other objects in the database.
- **TRUNCATE**: Deletes all rows in a table without logging the individual row deletions.
- **DELETE**: Deletes specified rows from a table.
- **Functions**: Built-in SQL functions to perform calculations on data, manipulate strings, or work with dates.
- **Transactions**: A sequence of SQL operations treated as a single logical unit.
- **Views**: Virtual tables based on the result set of an SQL statement.
- **Index**: Used to speed up the retrieval of rows by using a pointer.
- **Aggregation Functions**: Perform a calculation on a set of values and return a single value, e.g., `SUM`, `AVG`, `COUNT`.
- **Schema**: The structure of a database defined in a formal language supported by the DBMS.
- **Subquery**: A query nested within another SQL query.
- **Character functions**:  tools for manipulating and working with text data (strings).
For example: 
    - trim - removes specified prefixes or suffixes from a string.
    - replace - allows you to replace all occurrences of a specified substring within a string with another substring.
    - char_length - returns the number of characters in a string.
    - substring - ubstring from a string starting at a specified position and for a specified length.
    - instr - returns the position of the first occurrence of a substring in a string.
    - concat - combines two or more strings into one string.
    - upper - converts all letters in a string to uppercase.
    - left - extracts a specified number of characters from the left side of a string.

Of course SQL has dialects, that depends on the type of database.

### SQL Query Examples
Here are some examples of SQL queries that cover basic CRUD operations (Create, Read, Update, Delete), as well as some more advanced operations like JOIN, GROUP BY, and queries using the WHERE clause.

### Creating a Table (CREATE)
Creates a `Users` table with columns for user ID, first name, last name, and age:
```sql
CREATE TABLE Users (
    ID int PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Age int
);
``` 
### Inserting Data (INSERT)
Inserts a record into the Users table:
```sql
INSERT INTO Users (ID, FirstName, LastName, Age)
VALUES (1, 'John', 'Doe', 30);
```
### Reading Data (SELECT)
Selects all columns from the Users table:
```sql
SELECT * FROM Users;
```
Selects only the first name and last name of users who are older than 25:
```sql
SELECT FirstName, LastName FROM Users WHERE Age > 25;
```
### Updating Data (UPDATE)
Updates the age of the user with ID equal to 1:
```sql
UPDATE Users SET Age = 31 WHERE ID = 1;
```
###  Deleting Data (DELETE)
Deletes the user with ID equal to 1:
```sql
DELETE FROM Users WHERE ID = 1;
```
### Joining Tables (JOIN)
Assuming we have another table Orders with columns for order ID, user ID who placed the order, and order date. To join these two tables and select all orders placed by the user with ID equal to 1:
```sql
SELECT Users.ID, FirstName, LastName, OrderDate
FROM Users
JOIN Orders ON Users.ID = Orders.UserID
WHERE Users.ID = 1;
```
### Grouping Data (GROUP BY)
Groups users by age and counts how many users there are in each age group:
```sql
SELECT Age, COUNT(*) AS NumberOfUsers
FROM Users
GROUP BY Age;
```
### Aggregate Functions (e.g., COUNT, MAX, MIN, AVG)
Selects the maximum age among all users:
```sql
SELECT MAX(Age) AS OldestUser FROM Users;
```
### Transactions
A transaction is a sequence of data processing operations that are treated as a single unit. RDBMS provides mechanisms like ACID (Atomicity, Consistency, Isolation, Durability) to ensure data safety and integrity during transactions.

An SQL transaction is a sequence of operations performed as a single unit of work. If all operations within the transaction are successfully completed, the transaction is committed, meaning all changes are permanently saved to the database. However, if any of the operations fail, the transaction is rolled back, meaning none of the operations will be saved, and the database will be restored to its state before the transaction started.
```sql
BEGIN TRANSACTION;

-- Add a user to the Users table
INSERT INTO Users (ID, FirstName, LastName, Age) VALUES (1, 'Anna', 'Kowalska', 28);

-- Add the user's address information to the Addresses table
INSERT INTO Addresses (UserID, Street, City, PostalCode) VALUES (1, 'Lipowa', 'Warsaw', '00-001');

-- If both operations are successful, commit the transaction
COMMIT;

-- In case of an error, rollback the transaction
ROLLBACK;
```
In this example, we start the transaction with the BEGIN TRANSACTION command, then perform two INSERT operations – adding a user to the Users table and their address to the Addresses table. If both operations are executed without errors, the transaction is committed with the COMMIT command, meaning all changes are permanently saved to the database. However, if an error occurs during the transaction execution (for example, a violation of primary or foreign key constraints), the entire transaction is rolled back with the ROLLBACK command, restoring the database state to the point before the transaction started, thus cancelling all changes made during the transaction.

### View
A SQL view is essentially a virtual table that is based on the result-set of an SQL statement. A view contains rows and columns, just like a real table, and the fields in a view are fields from one or more real tables in the database. You can use views to simplify complex queries, aggregate data, join data from multiple tables, or restrict access to certain data.

Here's an example of creating a view in SQL:
```sql
CREATE VIEW ViewEmployeeDetails AS
SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```
In this example, we create a view named ViewEmployeeDetails. This view combines data from two tables: Employees and Departments. For each employee, the view will show the employee ID, first name, last name, and the name of the department they work in. This is achieved by joining the Employees table with the Departments table on the DepartmentID column.

To use this view to retrieve data, you would use a SELECT statement just as you would with a regular table:
```sql
SELECT * FROM ViewEmployeeDetails;
``` 
### Cursor
A cursor in SQL is a tool that allows programmers to sequentially process rows returned by a query. This is particularly useful in situations where operations need to be performed on individual result records, such as for updates, processing, or executing some business logic for each row individually. Cursors allow for iterating over a query's result set, giving the programmer control over each row of data.

Using a cursor typically involves several steps:
- Declaration of the cursor: Specifying the SQL query that will be the data source for the cursor.
- Opening the cursor: Initializing the cursor, making it ready for use.
- Fetch: Sequentially fetching rows from the cursor. Each fetch moves the cursor to the next row in the result set.
- Closing the cursor: Releasing resources associated with the cursor after the work is completed.

Example:
```sql
-- Declaration of variables to store row data
DECLARE @FirstName NVARCHAR(50), @LastName NVARCHAR(50);

-- Cursor declaration
DECLARE cursorEmployees CURSOR FOR 
SELECT FirstName, LastName FROM Employees;

-- Opening the cursor
OPEN cursorEmployees;

-- Fetching the first row
FETCH NEXT FROM cursorEmployees INTO @FirstName, @LastName;

-- Loop through all rows
WHILE @@FETCH_STATUS = 0
BEGIN
    -- Here we can perform operations on the data, for example, displaying it
    PRINT 'Employee: ' + @FirstName + ' ' + @LastName;

    -- Fetching the next row
    FETCH NEXT FROM cursorEmployees INTO @FirstName, @LastName;
END

-- Closing the cursor
CLOSE cursorEmployees;

-- Releasing cursor resources
DEALLOCATE cursorEmployees;
```
In this example:
- We first declare a cursor named cursorEmployees, which selects the first names and last names of employees from the Employees table.
- Then, we open the cursor and use a WHILE loop to iterate through all the rows returned by the cursor. In each iteration of the loop, we fetch the data into the @FirstName and @LastName variables and perform specified operations on them, in this case, simply displaying the data.
- After processing all rows, we close the cursor and release the resources using DEALLOCATE.

### Trigger
A trigger in SQL is a special type of stored procedure that automatically runs or is "triggered" in response to certain events on a specific table or view in a database. Triggers can be used to enforce complex business rules, maintain data integrity, and perform automatic updates within the database. Common triggering events include INSERT, UPDATE, and DELETE operations.

Here’s an example of a trigger in SQL that automatically updates the LastUpdated timestamp column of a Customers table whenever a row in that table is updated:
```sql
CREATE TRIGGER UpdateCustomerLastUpdated
ON Customers
AFTER UPDATE
AS
BEGIN
    UPDATE Customers
    SET LastUpdated = GETDATE()
    WHERE CustomerID IN (SELECT DISTINCT CustomerID FROM Inserted)
END;
```
In this example:
- A trigger named UpdateCustomerLastUpdated is created on the Customers table.
- It is set to fire AFTER an UPDATE operation is performed on the table.
- The trigger's action updates the LastUpdated column of the Customers table to the current date and time (using GETDATE()) for all rows that were affected by the update operation.
- The Inserted logical table, which is used within the trigger, contains copies of the affected rows during INSERT and UPDATE operations. Here, it's used to determine which CustomerIDs were updated, ensuring that only those rows' LastUpdated columns are modified.

### Index 
An index in databases is a data structure that improves the speed of data retrieval operations on a database table. Indexes are created on one or more columns of a table and can significantly increase query performance, allowing the database system to find rows matching query criteria more quickly.

The primary goal of an index is to reduce the number of disk reads required to find data in a large table. It works similarly to an index in a book, where instead of flipping through the entire book page by page to find a topic of interest, you can refer to the index, which quickly directs you to the desired information.

#### How Does an Index Work?
- **Structure**: Indexes are typically implemented as B-trees (most commonly B-trees or variants like B+-trees), although other structures such as AVL trees, red-black trees, or hash tables can also be used.
- **Selection**: When you create an index on a column, the database system creates a data structure that maps the values of the column to the specific locations of rows in the table.
- **Performance**: Queries using an index can find data much faster since the system does not need to search the entire table. The index allows skipping most of the data and directly going to the needed records.

#### Types of Indexes
- **Single Column**: An index created on a single column of a table.
- **Multicolumn**: An index that covers more than one column, useful when queries frequently use several columns simultaneously.
    Unique: An index that requires all values in the column (or set of columns) to be unique. This is often applied to primary keys.

#### Usage and Management
Creating indexes is not without costs. While they increase read query speeds, they can slow down write operations (INSERT, UPDATE, DELETE) because the system must update not only the data in the table but also all corresponding indexes. Therefore, it's important to strategically create indexes, especially on those columns that are frequently used in WHERE clauses, JOIN operations, and aggregation operations.

### Comparisom operators
- **=** : Equality; returns true when two values are identical.
- **!=** or **<>**: Inequality; returns true when two values are not identical.
- **<**: Less than; returns true when the value on the left side is less than the value on the right side.
- **\>**: Greater than; returns true when the value on the left side is greater than the value on the right side.
- **<=**: Less than or equal to; returns true when the value on the left side is less than or equal to the value on the right side.
- **\>=**: Greater than or equal to; returns true when the value on the left side is greater than or equal to the value on the right side.

## 5. ACID Properties
ACID is an acronym that stands for Atomicity, Consistency, Isolation, and Durability. These properties ensure that database transactions are processed reliably and help maintain the integrity of the database:

- **Atomicity**: Guarantees that each transaction is treated as a single unit, which either completes in its entirety or does not complete at all. There's no in-between state.
- **Consistency**: Ensures that a transaction can only bring the database from one valid state to another, maintaining the database's correctness.
- **Isolation**: Provides a way for transactions to be executed in isolation from one another, preventing concurrent transactions from interfering with each other's execution.
- **Durability**: Ensures that once a transaction has been committed, it will remain so, even in the event of power loss, crashes, or errors. This property guarantees that the database keeps track of pending changes in such a way that the changes can be replayed to recover from a crash.

## 6. RDBMS
RDBMS, which stands for Relational Database Management System, is a type of database management system that stores data in structures called tables. These tables are organized into rows and columns, where each row represents a single record, and each column represents a specific data field. One of the key features of an RDBMS is the ability to create relationships between tables, allowing for efficient linking of data across different tables through foreign keys.

RDBMS supports the SQL (Structured Query Language), which allows for the creation, modification, retrieval, and management of data. RDBMS are widely used in business applications, customer data management systems, finance, and anywhere effective management of large volumes of structured data is needed.

Some of the most popular RDBMS include MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server, and SQLite. Each of these systems offers unique features and capabilities, but all are based on the common principles of the relational model, such as data integrity, transactions, normalization, and support for CRUD (Create, Read, Update, Delete) operations.

## 7. Normalization
Normalization is the process of organizing data in a database in a way that minimizes redundancy and dependencies. The goal of normalization is to divide large tables into smaller, related ones, which simplifies data management and provides greater flexibility.

Normalization in relational databases is the process of designing a database's structure to minimize data redundancy and avoid undesirable phenomena such as insertion, update, or deletion anomalies. The aim of normalization is to enhance consistency and efficiency in data processing by dividing large tables into smaller, related ones. Normalization is achieved through applying successive "normal forms" (NF), each intended to eliminate specific design issues. Here are the main types of normalization along with examples for each:

### First Normal Form (1NF)
A table is in 1NF if it meets the following conditions:
- Each cell of the table contains only single values (no composite or list values).
- All the values in a column are of the same data type.
- Each column has a unique name.
- The order in which data is stored does not matter.

Example:
Before 1NF (a table with composite values):

| StudentID | Name       | Courses          |
|-----------|------------|------------------|
| 1         | John Doe   | Math, Science    |
| 2         | Jane Smith | Literature, Math |

After applying 1NF (each value in a separate row, eliminating composite values):

| StudentID | Name       | Course     |
|-----------|------------|------------|
| 1         | John Doe   | Math       |
| 1         | John Doe   | Science    |
| 2         | Jane Smith | Literature |
| 2         | Jane Smith | Math       |

### Second Normal Form (2NF)
To be in 2NF, a table must first meet all the criteria for 1NF, and additionally:
- All non-key attributes must be fully functionally dependent on the primary key.

Example:
Before 2NF (partial dependency on part of the composite key):

| StudentID | CourseID | StudentName | CourseName |
|-----------|----------|-------------|------------|
| 1         | 101      | John Doe    | Math       |
| 2         | 102      | Jane Smith  | Science    |

After applying 2NF (removing partial dependencies by splitting into two tables):

| StudentID | StudentName |
|-----------|-------------|
| 1         | John Doe    |
| 2         | Jane Smith  |

| StudentID | CourseID |
|-----------|----------|
| 1         | 101      |
| 2         | 102      |

| CourseID | CourseName |
|----------|------------|
| 101      | Math       |
| 102      | Science    |

### Third Normal Form (3NF)
A table is in 3NF if it meets all the requirements of 2NF, and:
- There are no transitive functional dependencies between non-key columns. In other words, non-key attributes must be dependent only on the primary key.

Example:
Before 3NF (transitive dependency exists where DepartmentName depends on DepartmentID which depends on EmployeeID):

| EmployeeID | EmployeeName | DepartmentID | DepartmentName |
|------------|--------------|--------------|----------------|
| 1          | John Doe     | D1           | HR             |
| 2          | Jane Smith   | D2           | IT             |

After applying 3NF (removing the transitive dependency by creating a separate table for departments):

| EmployeeID | EmployeeName | DepartmentID |
|------------|--------------|--------------|
| 1          | John Doe     | D1           |
| 2          | Jane Smith   | D2           |

| DepartmentID | DepartmentName |
|--------------|----------------|
| D1           | HR             |
| D2           | IT             |

### Fourth Normal Form (4NF)
To achieve 4NF, a table must meet the criteria of 3NF, and in addition:
- There are no multi-valued dependencies unless they are on a candidate key. This means eliminating situations where there are groups of two or more attributes that are independent of each other.

Example:
Before 4NF (multi-valued dependencies exist between Employee and Project and between Employee and Skill):

| Employee  | Project | Skill  |
|-----------|---------|--------|
| John Doe  | P1      | Java   |
| John Doe  | P2      | Python |

After applying 4NF (removing multi-valued dependencies by splitting into two tables):

| Employee  | Project |
|-----------|---------|
| John Doe  | P1      |
| John Doe  | P2      |

| Employee  | Skill  |
|-----------|--------|
| John Doe  | Java   |
| John Doe  | Python |

### Fifth Normal Form (5NF)
Table is in 5NF if it satisfies the requirements of 4NF and:
- Every join dependency in the table is a consequence of the candidate keys. 5NF addresses the redundancy of data that can occur when a table represents more than one many-to-many relationship.

Example:
Before 5NF (a table representing two many-to-many relationships leading to redundancy):

| Professor | Course | Textbook          |
|-----------|--------|-------------------|
| Dr. Smith | Math   | "Mathematics 101" |
| Dr. Smith | Math   | "Advanced Math"   |
| Dr. Jones | History| "World History"   |

In this table, both the relationships between professors and courses and between courses and textbooks are many-to-many. Representing both in a single table leads to redundancy.

After applying 5NF (splitting into separate tables to remove redundancy):

| Professor | Course  |
|-----------|---------|
| Dr. Smith | Math    |
| Dr. Jones | History |

| Course | Textbook          |
|--------|-------------------|
| Math   | "Mathematics 101" |
| Math   | "Advanced Math"   |
| History| "World History"   |

## 8. Data models
Data models are essential conceptual tools used in organizing, managing, and structuring data in databases and information systems. They provide a systematic approach to data management and are crucial for designing databases and ensuring data integrity and efficiency. Here's an overview of the primary data models used in database systems:

- **Hierarchical Model**

The hierarchical data model organizes data in a tree-like structure, where each record has a single parent but can have multiple children. This model was one of the earliest data models and is reminiscent of a family tree. The hierarchical model is efficient for certain types of read, write, and delete operations, but it can become complex and difficult to manage, especially for databases with many relationships.

- **Network Model**

Expanding on the hierarchical model, the network model allows each record to have multiple parents, creating a more flexible structure that resembles a graph more than a tree. This model can represent more complex relationships and is better suited for environments where relationships between data are dynamic and varied. However, the network model can be complex to design and maintain.

- **Relational Model**

Introduced by Edgar F. Codd in 1970, the relational model uses a table-based format to represent data and relationships between data. Each table (relation) contains rows (records) and columns (attributes). The relational model is the most widely used data model for databases, thanks to its simplicity, flexibility, and robustness. It supports a powerful query language (SQL) and ensures data integrity through rules such as primary and foreign keys.

- **Object-Oriented Model**

The object-oriented model represents data as objects, similar to object-oriented programming. This model integrates well with object-oriented programming languages, making it a good choice for applications developed in these languages. It allows for the representation of more complex data structures, including inheritance and polymorphism, making it suitable for applications requiring complex data interactions.

- **Entity-Relationship Model**

The entity-relationship (ER) model is a conceptual tool used in the design phase of database development. It focuses on identifying the entities present in a system and the relationships between those entities. An ER diagram is used to visually represent entities, their attributes, and their interrelations. This model helps in designing a database at the conceptual level, which can then be translated into a physical database using one of the other data models.

- **Document Model**

The document model is used primarily in NoSQL databases. It organizes data into documents, which can be thought of as independent units or records. These documents are then grouped into collections. The document model is highly flexible, allowing for nested structures and varying fields across documents in the same collection. It's particularly well-suited for applications that deal with large volumes of diverse data that doesn't fit neatly into tables.

- **Key-Value Model**

Also used in NoSQL databases, the key-value model is the simplest form of data storage that stores data as a collection of key-value pairs. This model provides fast retrieval and is ideal for use cases where the data access pattern is simple and does not require complex querying capabilities. It's commonly used for caching, session storage, and in scenarios where the dataset is large but the access pattern is simple.

## 9. Relational database management systems:
- **MySQL**: An open-source RDBMS known for its reliability and ease of use, commonly used in web applications.
- **PostgreSQL**: An advanced, open-source object-relational database system that supports a wide range of data types and is known for its standards compliance and extensibility.
- **Oracle Database**: A comprehensive, enterprise-grade RDBMS known for its robust feature set, scalability, and security features, widely used in large corporations and critical systems.
- **Microsoft SQL Server**: A commercial RDBMS developed by Microsoft, offering a broad range of data analytics, machine learning, and business intelligence features.
- **SQLite**: A lightweight, file-based RDBMS, embedded into the end program, popular for applications and devices where simplicity and minimal setup are advantageous.
- **IBM Db2**: A family of data management products, including database servers, developed by IBM, known for delivering high performance and reliability for enterprise applications.
- **MariaDB**: A community-developed, commercially supported fork of MySQL, intended to remain free and open-source software under the GNU GPL.

## 10. PL/SQL, TSQL
PL/SQL (Procedural Language/SQL) and T-SQL (Transact-SQL) are extensions of SQL designed to add procedural programming features to standard SQL, allowing for more complex operations and programming logic directly within the database.
PL/SQL

- **PL/SQL** is a procedural programming language offered by Oracle Database. It allows for the creation of stored procedures, functions, packages, triggers, and anonymous blocks. PL/SQL is specifically designed for Oracle databases and enables the creation of modular code that can be easily managed and reused. It supports variables, loops, conditional statements, and exception handling, facilitating the development of advanced database applications with more complex business logic.
T-SQL

- **T-SQL**, or Transact-SQL, is an extension of SQL used by Microsoft in SQL Server products. Similar to PL/SQL, T-SQL introduces procedural features such as variables, loops, conditional statements, exception handling, stored procedures, functions, and triggers, and extends SQL with additional constructs like table-valued temporary variables and T-SQL-specific functions and operators. T-SQL is designed to simplify working with data in SQL Server, enabling the creation of more complex queries and data operations.

Both languages significantly extend the capabilities of standard SQL, allowing developers to create more effective and efficient database solutions integrated with business logic. The choice between PL/SQL and T-SQL mainly depends on the database management system being used: Oracle for PL/SQL and SQL Server for T-SQL.

## 11. Constraints
Constraints in databases are rules applied to table columns to enforce data integrity and consistency by restricting the type, range, or format of data that can be stored in a column. These rules ensure that the data entered into the database adheres to the defined business logic and requirements. Here are the main types of constraints:

- **PRIMARY KEY**: Ensures that each value in a column (or a group of columns) is unique and not null, identifying each row in a table uniquely.
- **FOREIGN KEY**: Enforces the relationship between tables by ensuring that the value in one table matches a value in another table, maintaining referential integrity.
- **UNIQUE**: Guarantees that all values in a column are different from one another, ensuring that there are no duplicate values.
- **CHECK**: Allows specifying a condition that each value in a column must satisfy. For example, a CHECK constraint can enforce that a column's value must be greater than zero.
- **NOT NULL**: Ensures that a column cannot have a NULL value, requiring that a value must be entered for the column in every row.
- **DEFAULT**: Sets a default value for a column when no value is specified during the insertion of a row.

## 12. Schema
A schema in databases refers to the structural design of a database that defines how data is organized within the database. It is a collection of database objects such as tables, views, indexes, stored procedures, relationships between tables, and constraints, which together describe the data model and the rules according to which data is stored, processed, and secured.

The database schema also specifies the relationships between different pieces of data, the data types that can be stored in each column, and how data can be accessed and manipulated. Schemas are used not only for designing and implementing databases but also for documenting and managing them.

In practice, a schema can also be seen as a namespace or container that logically groups related objects, facilitating their organization and management. In many database management systems, such as SQL Server, Oracle, or PostgreSQL, multiple schemas can be defined within a single database, allowing for better separation and access control to data in complex systems.

## Learning Resources
- **[Kurs MySQL. Bazy danych, język zapytań SQL](https://www.youtube.com/playlist?list=PLOYHgt8dIdoymv-Wzvs8M-OsKFD31VTVZ)** - basic information about the database and SQL.
- **[SQL Language](https://leetcode.com/explore/learn/card/sql-language/)** - here is some information about SQL, along with exercises to practice.
- **[CS50's Introduction to Databases with SQL](https://www.youtube.com/playlist?list=PLhQjrBD2T382v1MBjNOhPu9SiJ1fsD4C0)** - an introduction to databases using a language called SQL.
