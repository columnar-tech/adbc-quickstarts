<!--
Copyright 2026 Columnar Technologies Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Connecting C++ and Microsoft SQL Server with ADBC

## Instructions

> [!TIP]
> If you already have a SQL Server instance running, skip the steps to run SQL Server in a Docker container.

### Prerequisites

1. [Install miniforge](https://github.com/conda-forge/miniforge)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Create and activate a new environment with the required C++ libraries:

   ```sh
   mamba create -n adbc-cpp -c conda-forge cmake compilers libadbc-driver-manager libarrow

   # Initialize mamba in your shell if not already done
   eval "$(mamba shell hook --shell zsh)"
   mamba activate adbc-cpp
   ```

   (`cmake` is only needed if you use CMake to build the C++ program below.)

### Set up SQL Server

1. Start SQL Server in a Docker container:

   ```sh
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
   dbc install --level user mssql
   ```

1. Customize the C++ program `main.cpp` as needed
   - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
     - Change `uri` as needed, using query parameters to add more connection arguments, or keep it as is to use the data included with this example

   > [!TIP]
   > To use Microsoft Entra ID for authentication, [install the Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli), log in using the `az login` command, and add `fedauth=` to your connection URI. For example:
   >
   > ```
   > sqlserver://my-database-endpoint.database.windows.net:1433?database=my-database-name&fedauth=ActiveDirectoryDefault
   > ```

   - If you changed which database you're connecting to, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

1. Build and run the C++ program:

   Using Make:
   ```sh
   make
   ./mssql_demo
   ```

   Or using CMake:
   ```sh
   cmake -B build
   cmake --build build
   ./build/mssql_demo
   ```

### Clean up

1. Clean build artifacts:

   Using Make:
   ```sh
   make clean
   ```

   Using CMake:
   ```sh
   rm -rf build
   ```

1. Stop the Docker container running SQL Server:

   ```sh
   docker stop mssql
   docker rm mssql
   ```
