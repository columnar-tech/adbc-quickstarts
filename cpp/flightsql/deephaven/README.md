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

# Connecting C++ and Deephaven with ADBC

## Instructions

This example queries Deephaven using [Arrow Flight SQL](https://deephaven.io/core/docs/how-to-guides/flight-sql/).

> [!TIP]
> If you already have a Deephaven instance running, skip the steps to set up and clean up Deephaven.

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Deephaven

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Deephaven instance:

    ```sh
    docker run -d --rm --name deephaven -p 127.0.0.1:10000:10000 \
        -e START_OPTS=-Dauthentication.psk=deephaven ghcr.io/deephaven/server:latest
    ```

3. Wait until Docker reports `healthy`.

    ```sh
    docker inspect --format '{{.State.Health.Status}}' deephaven
    ```

### Connect to Deephaven

1. Install the Flight SQL ADBC driver:

    ```sh
    dbc install --level user flightsql
    ```

2. Customize the C++ program `main.cpp` as needed.
    - Change the connection arguments in the `AdbcDatabaseSetOption()` calls. For authentication and session options, see [Deephaven's ADBC examples](https://deephaven.io/core/docs/how-to-guides/flight-sql/#adbc).
        - `uri` is the Flight SQL endpoint of your Deephaven instance. Use `grpc+tls://` for an endpoint with TLS.
        - For pre-shared key authentication, replace the final `deephaven` in `adbc.flight.sql.authorization_header` with your key. Deephaven prints generated keys in the server log. If your instance allows anonymous access, set the header to `Anonymous`.
        - The `x-deephaven-auth-cookie-request` header asks Deephaven for a session cookie. The Flight SQL driver's cookie middleware sends it on subsequent requests.
    - To query a table in Deephaven's global query scope, change the SQL SELECT statement in `AdbcStatementSetSqlQuery()`. Deephaven's Flight SQL interface is read-only and returns a static snapshot, even for ticking tables.

3. Build and run the C++ program:

    Using Make:
    ```sh
    pixi run make
    ./flightsql_demo
    ```

    Or using CMake:
    ```sh
    pixi run cmake -B build
    pixi run cmake --build build
    ./build/flightsql_demo
    ```

### Clean up

1. Stop the Docker container running Deephaven:

    ```sh
    docker stop deephaven
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
