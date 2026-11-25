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

# Connecting C++ and PolarDB for PostgreSQL with ADBC

## Instructions

> [!TIP]
> If you already have a PolarDB for PostgreSQL instance running, skip the steps to set up and clean up PolarDB for PostgreSQL.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up PolarDB for PostgreSQL

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a PolarDB for PostgreSQL instance:

    ```sh
    docker run -d --rm --name polardb -p 127.0.0.1:5432:5432 \
        -e POLARDB_USER=username -e POLARDB_PASSWORD=password \
        polardb/polardb_pg_local_instance:15
    ```

3. The primary and replica restart during setup. Wait for two `server started` lines after the `server stopped` lines.

    ```sh
    docker logs polardb 2>&1 | grep -E '^server (started|stopped)$'
    ```

### Connect to PolarDB for PostgreSQL

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
    pixi run make
    ./polardb_pg_demo
    ```

    Or using CMake:
    ```sh
    pixi run cmake -B build
    pixi run cmake --build build
    ./build/polardb_pg_demo
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

2. Stop the Docker container running PolarDB for PostgreSQL:

    ```sh
    docker stop polardb
    ```
