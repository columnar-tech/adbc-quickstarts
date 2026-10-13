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

# Connecting C++ and Firebolt with ADBC

## Instructions

This example runs Firebolt Core locally in Docker.

> [!TIP]
> If you already have a Firebolt Core instance running, skip the steps to set up Firebolt.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Firebolt

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Firebolt Core instance:

    ```sh
    docker run -d --rm --name firebolt -p 127.0.0.1:3473:3473 ghcr.io/firebolt-db/engine:5.0.0-pre.0.20260927210425.e91cd5bd17f8
    ```

3. Check that the engine can run queries:

    ```sh
    curl -fsS http://localhost:3473 --data 'SELECT 1'
    ```

    If the engine is still starting, wait a few seconds and try again.

### Connect to Firebolt

1. Install the Firebolt ADBC driver:

   ```sh
   dbc install --level user firebolt
   ```

1. Customize the C++ program `main.cpp` as needed,
   - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
     - Format the URI according to the [driver documentation](https://docs.adbc-drivers.org/drivers/firebolt/index.html#connecting), or keep it as is

1. Build and run the C++ program:

   Using Make:
   ```sh
   pixi run make
   ./firebolt_demo
   ```

   Or using CMake:
   ```sh
   pixi run cmake -B build
   pixi run cmake --build build
   ./build/firebolt_demo
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

1. Stop the Docker container running Firebolt:

   ```sh
   docker stop firebolt
   ```
