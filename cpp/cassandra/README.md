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

# Connecting C++ and Apache Cassandra with ADBC

## Instructions

> [!TIP]
> If you already have a Cassandra instance running, skip the steps to run Cassandra in a Docker container.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Cassandra

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Start a Cassandra instance:

   ```sh
   docker run -d --rm --name cassandra -p 9042:9042 cassandra:latest
   ```

1. Wait for Cassandra to accept connections. This can take a minute or two:

   ```sh
   docker exec cassandra cqlsh -e "DESCRIBE CLUSTER"
   ```

   If the command fails, wait a few seconds and run it again.

### Connect to Cassandra

1. Install the Cassandra ADBC driver:

   ```sh
   dbc install --level user --pre cassandra
   ```

1. Customize the C++ program `main.cpp` as needed,
   - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
     - Format the URI according to the [driver documentation](https://docs.adbc-drivers.org/drivers/cassandra/index.html#connecting), or keep it as is

1. Build and run the C++ program:

   Using Make:
   ```sh
   pixi run make
   ./cassandra_demo
   ```

   Or using CMake:
   ```sh
   pixi run cmake -B build
   pixi run cmake --build build
   ./build/cassandra_demo
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

1. Stop the Docker container running Cassandra:

   ```sh
   docker stop cassandra
   ```
