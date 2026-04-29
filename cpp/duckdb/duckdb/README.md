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

# Connecting C++ and DuckDB with ADBC

## Instructions

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Connect to DuckDB

1. Install the DuckDB ADBC driver:

   ```sh
   dbc install --level user duckdb
   ```

1. Customize the C++ program `main.cpp` as needed
   - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
     - Set `uri` to the location of the DuckDB database file you want to query, or keep it set to `games.duckdb` to use the database file included with this example
   - If you changed the database file, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

1. Build and run the C++ program:

   Using Make:
   ```sh
   pixi run make
   ./duckdb_demo
   ```

   Or using CMake:
   ```sh
   pixi run cmake -B build
   pixi run cmake --build build
   ./build/duckdb_demo
   ```

### Clean up

1. Clean build artifacts:

   Using Make:
   ```sh
   pixi run make clean
   ```

   Using CMake:
   ```sh
   rm -rf build
   ```
