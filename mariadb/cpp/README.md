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

# Connecting C++ and MariaDB with ADBC

## Instructions

> [!TIP]
> If you already have a MariaDB instance running, skip the steps to install MariaDB, start it, load data, and stop it.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up MariaDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a MariaDB instance:

    ```sh
    docker run -d --rm --name some-mariadb -e MARIADB_ROOT_PASSWORD=my-secret-pw -p 3306:3306 mariadb
    ```

3. Create a table in MariaDB and load data into it:

    ```sh
    cat games.sql | docker exec -i some-mariadb mariadb --user=root --password=my-secret-pw
    ```

### Connect to MariaDB

1. Install the MariaDB ADBC driver:

    ```sh
    dbc install --level user mariadb
    ```

2. Customize the C++ program `main.cpp` as needed
    - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
        - Format `uri` according to the [driver documentation](https://docs.adbc-drivers.org/drivers/mariadb/index.html#connecting), or keep it as is to use the data included with this example
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

3. Build and run the C++ program:

    Using Make:
    ```sh
    pixi run make
    ./mariadb_demo
    ```

    Or using CMake:
    ```sh
    pixi run cmake -B build
    pixi run cmake --build build
    ./build/mariadb_demo
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

2. Stop the Docker container running MariaDB:

    ```sh
    docker stop some-mariadb
    ```
