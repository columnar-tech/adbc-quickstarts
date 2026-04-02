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

# Connecting C++ and SingleStore with ADBC

## Instructions

> [!TIP]
> If you already have a SingleStore instance running, skip the steps to set up and clean up SingleStore.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up SingleStore

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a SingleStore instance:

    ```sh
    docker run \
        -d --rm --name singlestoredb-dev \
        -e ROOT_PASSWORD="YOUR_ROOT_PASSWORD" \
        -p 3306:3306 -p 8080:8080 -p 9000:9000 \
        ghcr.io/singlestore-labs/singlestoredb-dev:latest
    ```

    To run the image on Apple Silicon, add the `--platform linux/amd64` option.

### Connect to SingleStore

1. Install the SingleStore ADBC driver:

    ```sh
    dbc install --level user --pre singlestore
    ```

2. Customize the C++ program `main.cpp`
    - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
        - Format the URI according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#section-readme)
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

3. Build and run the C++ program:

    Using Make:
    ```sh
    pixi run make
    ./singlestore_demo
    ```

    Or using CMake:
    ```sh
    pixi run cmake -B build
    pixi run cmake --build build
    ./build/singlestore_demo
    ```

### Clean up

1. Stop the Docker container running SingleStore:

    ```sh
    docker stop singlestoredb-dev
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
