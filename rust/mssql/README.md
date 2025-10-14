# Connecting Rust and Microsoft SQL Server with ADBC

## Instructions

> [!TIP]
> If you already have a SQL Server instance running, skip the steps to run SQL Server in a Docker container.

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

### Set up SQL Server

1. Start SQL Server in a Docker container:

   ```sh
   docker pull mcr.microsoft.com/mssql/server:2025-latest

   docker run \
      -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Co1umn&r" \
      -p 1433:1433 --name mssql --hostname mssql \
      -d \
      mcr.microsoft.com/mssql/server:2025-latest
   ```

1. Create a table in SQL Server and load data into it:

   ```sh
   docker cp games.sql mssql:/tmp/games.sql

   docker exec -it mssql /opt/mssql-tools18/bin/sqlcmd \
     -S localhost -U sa -P 'Co1umn&r' -C -i /tmp/games.sql
   ```

### Connect to SQL Server

1. Install the SQL Server ADBC driver:

   ```sh
   dbc install mssql
   ```

1. Customize `src/main.rs` as needed
   - Change the connection arguments in `opts`
     - Change `OptionDatabase::Uri` as needed, using query parameters to add more connection arguments, or keep it as is to use the data included with this example
   - If you changed which database you're connecting to, also change the SQL SELECT statement in `statement.set_sql_query()`

1. Run the Rust program:

   ```sh
   cargo run
   ```

### Clean up

1. Stop the Docker container running SQL Server:

   ```sh
   docker stop mssql
   docker rm mssql
   ```
