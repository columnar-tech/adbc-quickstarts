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

# Connecting C++ and Apache Spark with ADBC

## Instructions

> [!TIP]
> If you already have a Spark instance running, skip the steps to set up and clean up Spark.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Spark

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Spark instance:

    ```sh
    docker run -d --rm --name spark-connect -p 15002:15002 apache/spark:4.1.2 bash -c "/opt/spark/sbin/start-connect-server.sh && tail -f /dev/null"
    ```

### Connect to Spark

1. Install the Spark ADBC driver:

    ```sh
    dbc install --level user spark --pre
    ```

2. Customize the C++ program `main.cpp`
    - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
        - Format `uri` according to the [driver documentation](https://docs.adbc-drivers.org/drivers/spark/index.html#connecting), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

3. Build and run the C++ program:

    Using Make:
    ```sh
    pixi run make
    ./spark_demo
    ```

    Or using CMake:
    ```sh
    pixi run cmake -B build
    pixi run cmake --build build
    ./build/spark_demo
    ```

### Clean up

1. Stop the Docker container running Spark:

    ```sh
    docker stop spark-connect
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
