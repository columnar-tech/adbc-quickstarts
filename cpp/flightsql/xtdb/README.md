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

# Connecting C++ and XTDB with ADBC

## Instructions

This example uses [XTDB](https://xtdb.com/), an immutable SQL database with built-in time travel that supports Arrow Flight SQL.

> [!TIP]
> If you already have an XTDB instance running, skip the steps to set up and clean up XTDB.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up XTDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Start an XTDB instance:

   ```sh
   docker run -d --rm --name xtdb -p 3000:3000 --pull always ghcr.io/xtdb/xtdb
   ```

   The Flight SQL server is enabled by default in XTDB 2.2.0 and later and listens on port 3000.

1. Wait for XTDB to finish starting up (this usually takes about 10 seconds). XTDB is ready when the container logs include the line `Node started`:

   ```sh
   docker logs xtdb
   ```

### Connect to XTDB

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install --level user flightsql
   ```

1. Customize the C++ program `main.cpp` as needed
   - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
     - `uri` is the URI of your XTDB Flight SQL server. The host and port will depend on your installation (the default port is 3000). The protocol scheme should be `grpc` or `grpc+tcp`. XTDB's Flight SQL server does not support TLS or authentication, so no username or password is needed.
   - Change the SQL SELECT statement in `AdbcStatementSetSqlQuery()` if desired

1. Build and run the C++ program:

   Using Make:
   ```sh
   pixi run make
   ./xtdb_demo
   ```

   Or using CMake:
   ```sh
   pixi run cmake -B build
   pixi run cmake --build build
   ./build/xtdb_demo
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

1. Stop the Docker container running XTDB:

   ```sh
   docker stop xtdb
   ```
