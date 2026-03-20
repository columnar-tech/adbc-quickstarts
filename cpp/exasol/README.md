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

# Connecting C++ and Exasol with ADBC

## Instructions

> [!TIP]
> If you already have an Exasol instance running, skip the steps to run Exasol in a Docker container.

### Prerequisites

1. [Install miniforge](https://github.com/conda-forge/miniforge)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. Create and activate a new environment with the required C++ libraries:

   ```sh
   mamba create -n adbc-cpp -c conda-forge cmake compilers libadbc-driver-manager libarrow

   # Initialize mamba in your shell if not already done
   eval "$(mamba shell hook --shell zsh)"
   mamba activate adbc-cpp
   ```

   (`cmake` is only needed if you use CMake to build the C++ program below.)

### Set up Exasol

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

   > [!WARNING]
   > The Exasol Docker image may not work with Docker for Windows or Docker for macOS. On macOS, we have found that [Colima](https://colima.run/)'s x86_64 emulation may work better. Alternatively, consider [Exasol Personal](https://www.exasol.com/campaigns/exasol-personal/) running in the cloud.

1. Start Exasol in a Docker container ([documentation](https://github.com/exasol/docker-db)):

   ```sh
   docker run \
      -p 127.0.0.1:9563:8563 \
      --name exasol \
      --privileged \
      --detach \
      exasol/docker-db:latest-2025.1
   ```

1. Create a table in Exasol and load data into it:

   ```sh
   docker cp games.sql exasol:/tmp/games.sql
   docker cp load-data.sh exasol:/tmp/load-data.sh
   docker exec exasol bash /tmp/load-data.sh
   ```

### Connect to Exasol

1. Install the Exasol ADBC driver:

   ```sh
   dbc install --level user exasol
   ```

2. Customize the C++ program `main.cpp` as needed
   - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
     - Change `uri` as needed, using query parameters to add more connection arguments, or keep it as is to use the data included with this example
   - If you changed which schema you're opening, also change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`

3. Build and run the C++ program:

   Using Make:
   ```sh
   make
   ./exasol_demo
   ```

   Or using CMake:
   ```sh
   cmake -B build
   cmake --build build
   ./build/exasol_demo
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

1. Stop the Docker container running Exasol:

   ```sh
   docker stop exasol
   docker rm exasol
   ```
