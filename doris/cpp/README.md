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

# Connecting C++ and Apache Doris with ADBC

## Instructions

This example uses [Apache Doris](https://doris.apache.org/), a high-performance, real-time analytical database.

> [!TIP]
> If you already have an Apache Doris instance running, skip the steps to set up Apache Doris.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Apache Doris

> [!WARNING]
> This setup process has not been tested on Windows and might not work without modification. Windows users should run it under WSL.

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Download the Apache Doris quick-start script:

    ```sh
    curl -O https://doris.apache.org/files/start-doris.sh
    ```

3. Add Flight SQL ports and configure the backend to advertise `localhost`:

    ```sh
    sed -i.bak -f patch-doris.sed start-doris.sh
    ```

4. Start an Apache Doris cluster:

    ```sh
    chmod 755 start-doris.sh
    ./start-doris.sh
    ```

### Connect to Apache Doris

1. Install the Flight SQL ADBC driver:

    ```sh
    dbc install --level user flightsql
    ```

2. Customize the C++ program `main.cpp` as needed.
    - Change the connection arguments in the `AdbcDatabaseSetOption()` calls.
        - `uri` is the URI of your Apache Doris instance. The host and FE Arrow Flight SQL port will depend on your installation.
        - `username` and `password` are the username and password of your Apache Doris user.
    - Change the SQL `SELECT` statement in `AdbcStatementSetSqlQuery()` if desired.

3. Build and run the C++ program:

    Using Make:
    ```sh
    pixi run make
    ./doris_demo
    ```

    Or using CMake:
    ```sh
    pixi run cmake -B build
    pixi run cmake --build build
    ./build/doris_demo
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

2. Stop the Docker project running Apache Doris:

    ```sh
    docker compose -f docker-compose-doris.yaml down
    ```
