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

# Connecting C++ and CrateDB with ADBC

## Instructions

> [!TIP]
> If you already have a CrateDB instance running, skip the steps to set up and clean up CrateDB.

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

2. [Install miniforge](https://github.com/conda-forge/miniforge)

3. Create and activate a new environment with the required C++ libraries:

    ```sh
    mamba create -n adbc-cpp -c conda-forge cmake compilers libadbc-driver-manager libarrow

    # Initialize mamba in your shell if not already done
    eval "$(mamba shell hook --shell zsh)"
    mamba activate adbc-cpp
    ```

    (`cmake` is only needed if you use CMake to build the C++ program below.)

### Set up CrateDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a CrateDB instance:

    ```sh
    docker run -d --rm --name cratedb -p 4200:4200 -p 5432:5432 crate -Cdiscovery.type=single-node
    ```

### Connect to CrateDB

1. Install the PostgreSQL ADBC driver:

    ```sh
    dbc install --level user postgresql
    ```

2. Customize the C++ program `main.cpp` as needed
    - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
        - Format `uri` according to the [connection URI format used by PostgreSQL](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

3. Build and run the C++ program:

    Using Make:
    ```sh
    make
    ./cratedb_demo
    ```

    Or using CMake:
    ```sh
    cmake -B build
    cmake --build build
    ./build/cratedb_demo
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

2. Stop the Docker container running CrateDB:

    ```sh
    docker stop cratedb
    ```
