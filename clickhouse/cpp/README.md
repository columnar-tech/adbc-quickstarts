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

# Connecting C++ and ClickHouse with ADBC

## Instructions

> [!TIP]
> If you already have a ClickHouse instance running, skip the steps to set up and clean up ClickHouse.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up ClickHouse

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a ClickHouse instance:

    ```sh
    docker run -d --rm --name some-clickhouse-server -p 8123:8123 -e CLICKHOUSE_USER=user -e CLICKHOUSE_PASSWORD=pass clickhouse/clickhouse-server
    ```

### Connect to ClickHouse

1. Install the ClickHouse ADBC driver:

    ```sh
    dbc install --level user clickhouse --pre
    ```

2. Customize the C++ program `main.cpp`
    - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
        - Format `uri` according to the [ClickHouse HTTP interface](https://clickhouse.com/docs/interfaces/http), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

3. Build and run the C++ program:

    Using Make:
    ```sh
    pixi run make
    ./clickhouse_demo
    ```

    Or using CMake:
    ```sh
    pixi run cmake -B build
    pixi run cmake --build build
    ./build/clickhouse_demo
    ```

### Clean up

1. Stop the Docker container running ClickHouse:

    ```sh
    docker stop some-clickhouse-server
    ```

2. Clean build artifacts:

    Using Make:
    ```sh
    pixi run make clean
    ```

    Using CMake:
    ```sh
    rm -rf build
    ```
