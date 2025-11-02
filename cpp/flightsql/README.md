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

# Connecting C++ and Arrow Flight SQL with ADBC

## Instructions

This example uses [Dremio](https://www.dremio.com/), but other open source tools and vendor products that support Arrow Flight SQL will also work with this driver.

> [!TIP]
> If you already have a Dremio instance running, skip the steps to set up Dremio.

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install miniforge](https://github.com/conda-forge/miniforge)

1. Create and activate a new environment with the required C++ libraries:

   ```sh
   mamba create -n adbc-cpp -c conda-forge cmake compilers libadbc-driver-manager arrow-cpp

   # Initialize mamba in your shell if not already done
   eval "$(mamba shell hook --shell zsh)"
   mamba activate adbc-cpp
   ```

   (`cmake` is only needed if you use CMake to build the C++ program below.)

### Set up Dremio

1. [Sign up for Dremio Cloud](https://www.dremio.com/) or follow the instructions to [set up Dremio Community](https://docs.dremio.com/current/get-started/docker/).

### Connect to Dremio

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install --level user flightsql
   ```

1. Customize the C++ program `main.cpp` as needed
   - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
     - `uri` is the URI of your Dremio instance. The host and port will depend on your installation (the default port is 32010). The protocol scheme should be `grpc` or `grpc+tcp` if your Dremio instance is not using TLS (e.g. if you are using Dremio Community) and should be `grpc+tls` otherwise (e.g. when using Dremio Cloud).
     - `username` and `password` are the username and password of your Dremio account. (If you are using Dremio Community, these were set during the installation instructions.)
     - For Dremio Cloud, remove the existing `uri`, `username`, and `password` options, create a personal access token (PAT), and set the URI and authorization header as follows:
       ```cpp
       // For US region:
       CHECK_ADBC(AdbcDatabaseSetOption(&database, "uri",
                                        "grpc+tls://data.dremio.cloud:443", &error));
       // For Europe region:
       //CHECK_ADBC(AdbcDatabaseSetOption(&database, "uri",
       //                                 "grpc+tls://data.eu.dremio.cloud:443", &error));
       CHECK_ADBC(AdbcDatabaseSetOption(
           &database, "adbc.flight.sql.authorization_header",
           "Bearer YOUR_TOKEN_HERE", &error));
       ```
   - If you changed `uri` to point to a different Flight SQL server, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

1. Build and run the C++ program:

   Using Make:
   ```sh
   make
   ./flightsql_demo
   ```

   Or using CMake:
   ```sh
   cmake -B build
   cmake --build build
   ./build/flightsql_demo
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
