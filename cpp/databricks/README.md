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

# Connecting C++ and Databricks with ADBC

## Instructions

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

4. [Create a Databricks account](https://www.databricks.com/) or be able to log in to an existing one.

### Set up Databricks

1. Log into [Databricks](https://login.databricks.com/) and create or locate an existing SQL warehouse.

2. Open the "Connection details" tab and record the server hostname and HTTP path. Then create and record a personal access token.

### Connect to Databricks

1. Install the Databricks ADBC driver:

    ```sh
    dbc install --level user databricks
    ```

2. Customize the C++ program `main.cpp`:
    - Change the connection arguments in the `AdbcDatabaseSetOption()` calls:
        - `uri` is the URI for your Databricks instance. It uses the following syntax: `databricks://token:<personal-access-token>@<server-hostname>:<port-number>/<http-path>`. See the Databricks documentation describing [how to get these connection details](https://docs.databricks.com/integrations/compute-details).
    - Change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`, or keep it as is.
        - Specify the catalog and schema by fully qualifying the table name as `catalog.schema.table`.

3. Build and run the C++ program:

    Using Make:
    ```sh
    make
    ./databricks_demo
    ```

    Or using CMake:
    ```sh
    cmake -B build
    cmake --build build
    ./build/databricks_demo
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
