<!--
Copyright 2025 Columnar Technologies Inc.

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

# Connecting C++ and Snowflake with ADBC

## Instructions

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install miniforge](https://github.com/conda-forge/miniforge)

1. Create and activate a new environment with the required C++ libraries:

   ```sh
   mamba create -n adbc-cpp -c conda-forge cmake compilers libadbc-driver-manager arrow-cpp

   # Initialize mamba in your shell if not already done
   eval "$(mamba shell hook --shell zsh)"
   mamba activate adbc-cpp
   ```

   (`cmake` is only needed if you use CMake to build the C++ program below.)

### Connect to Snowflake

1. Install the Snowflake ADBC driver:

   ```sh
   dbc install --level user snowflake
   ```

1. Customize the C++ program `main.cpp`
   - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
     - See [Snowflake Driver Client Options](https://arrow.apache.org/adbc/current/driver/snowflake.html#client-options) for the full list of available options
   - If you changed the database and schema, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

1. Build and run the C++ program:

   Using Make:
   ```sh
   make
   ./snowflake_demo
   ```

   Or using CMake:
   ```sh
   cmake -B build
   cmake --build build
   ./build/snowflake_demo
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
