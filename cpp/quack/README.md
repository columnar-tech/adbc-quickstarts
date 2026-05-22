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

# Connecting C++ and DuckDB Quack Server with ADBC

## Instructions

> [!TIP]
> If you already have a DuckDB Quack server instance running, skip the steps to set up DuckDB.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install DuckDB](https://duckdb.org/install/)

### Set up DuckDB server

1. Start the DuckDB CLI:

    ```sh
    duckdb
    ```

1. Create a table:

    ```sql
    CREATE TABLE penguins AS FROM read_csv('https://blobs.duckdb.org/data/penguins.csv', nullstr = 'NA');
    ```

1. Start a server from the DuckDB session:

    ```sql
    CALL quack_serve('quack:localhost');
    ```

    Note the `auth_token` value that DuckDB prints.

### Connect to DuckDB via Quack protocol

1. Install the Quack ADBC driver:

    ```sh
    dbc install --pre quack
    ```

1. Customize the C++ program `main.cpp` as needed
    - Change the `uri` connection argument in the `AdbcDatabaseSetOption()` call
        - Replace `YOUR_AUTH_TOKEN` with the `auth_token` printed by DuckDB
        - Change the host and port if applicable
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

1. Build and run the C++ program:

    Using Make:
    ```sh
    pixi run make
    ./quack_demo
    ```

    Or using CMake:
    ```sh
    pixi run cmake -B build
    pixi run cmake --build build
    ./build/quack_demo
    ```

### Clean up

1. If you started a DuckDB server, exit the DuckDB CLI:

    ```sql
    .exit
    ```

1. Clean build artifacts:

    Using Make:
    ```sh
    pixi run make clean
    ```

    Using CMake:
    ```sh
    rm -rf build
    ```
