# Apache NiFi Implementation

## Project Overview

This project demonstrates the use of Apache NiFi to automate data flows between MySQL, MongoDB, and Redis. The setup includes integration of a MySQL database, MongoDB for NoSQL operations, and Redis for key-value storage. Additionally, the necessary MySQL driver JAR is included for connecting NiFi to MySQL.

## Setup Components

### Databases:

1. MySQL:

- Used for relational data storage.
- Example use case: Storing employee records.

2. MongoDB:

- Used for document-based NoSQL storage.
- Example use case: Flexible schema storage for JSON data.

3. Redis:

- Used as a key-value store.
- Example use case: Caching and fast access to specific data.

### NiFi Integration:

- Automates data ingestion, transformation, and delivery across the databases.
- Uses processors to perform ETL tasks and cache data in Redis for quick access.

### MySQL Connector:

- Includes the MySQL JDBC driver (JAR file) to enable NiFi to connect with MySQL.
