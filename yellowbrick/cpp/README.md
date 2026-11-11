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

# Connecting C++ and Yellowbrick with ADBC

## Instructions

> [!TIP]
> If you already have a Yellowbrick instance running, skip the steps to set up and clean up Yellowbrick.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Yellowbrick

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

> [!WARNING]
> On Apple Silicon Macs, Yellowbrick Community Edition works with [OrbStack](https://orbstack.dev/) but not with Docker Desktop.

2. Start a Yellowbrick Community Edition instance:

    ```sh
    docker run -d --rm --privileged --name yellowbrick -p 443:443 -p 5432:5432 yellowbrickdata/yb-community-edition:latest
    ```

3. Wait for the service to be ready (it should print `localhost:5432 - accepting connections`):

    ```sh
    docker exec yellowbrick pg_isready -h localhost -p 5432
    ```

### Connect to Yellowbrick

1. Install the PostgreSQL ADBC driver:

    ```sh
    dbc install --level user postgresql
    ```

2. Customize the C++ program `main.cpp` as needed
    - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
        - Format `uri` according to the [connection URI format used by PostgreSQL](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS), or keep it as is
    - Change the SQL SELECT statement in `AdbcStatementSetSqlQuery()` if desired

3. Build and run the C++ program:

    Using Make:
    ```sh
    pixi run make
    ./yellowbrick_demo
    ```

    Or using CMake:
    ```sh
    pixi run cmake -B build
    pixi run cmake --build build
    ./build/yellowbrick_demo
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

2. Stop the Docker container running Yellowbrick:

    ```sh
    docker stop yellowbrick
    ```
