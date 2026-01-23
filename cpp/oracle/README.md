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

# Connecting C++ and Oracle Database with ADBC

## Instructions

> [!TIP]
> If you already have an Oracle Database instance running, skip the steps to set up and clean up Oracle Database.

### Prerequisites

1. [Install miniforge](https://github.com/conda-forge/miniforge)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. Create and activate a new environment with the required C++ libraries:

    ```sh
    mamba create -n adbc-cpp -c conda-forge cmake compilers libadbc-driver-manager libarrow

    # Initialize mamba in your shell if not already done
    eval "$(mamba shell hook --shell zsh)"
    mamba activate adbc-cpp
    ```

    (`cmake` is only needed if you use CMake to build the C++ program below.)

### Set up Oracle Database

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Oracle Database instance:

    ```sh
    docker run -d --rm --name oracle-db -p 1521:1521 -e ORACLE_PWD=password container-registry.oracle.com/database/free:latest
    ```

### Connect to Oracle Database

1. The ADBC driver for Oracle is available from Columnar's private driver registry. Create a [Columnar Cloud](https://cloud.columnar.tech) account and activate a 14-day free trial. Then authenticate to the registry:

    ```sh
    dbc auth login
    ```

2. Install the ADBC driver for Oracle:

    ```sh
    dbc install --level user oracle
    ```

3. Install the [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html) libraries.

4. Set `LD_LIBRARY_PATH` (Linux), `DYLD_LIBRARY_PATH` (macOS), or `PATH` (Windows) to make sure the Oracle Instant Client libraries are discoverable by your application.

5. Customize the C++ program `main.cpp` as needed
    - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
        - Change `uri` as needed, using query parameters to add more connection arguments. Format `uri` according to the the following syntax: `oracle://[user[:password]@]host[:port][/serviceName][?param1=value1&param2=value2]`, or keep it as is.
    - Change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`, or keep it as is.

6. Build and run the C++ program:

    Using Make:
    ```sh
    make
    ./oracle_demo
    ```

    Or using CMake:
    ```sh
    cmake -B build
    cmake --build build
    ./build/oracle_demo
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

2. Stop the Docker container running Oracle Database:

    ```sh
    docker stop oracle-db
    ```
