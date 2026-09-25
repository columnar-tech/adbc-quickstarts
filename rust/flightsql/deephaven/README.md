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

# Connecting Rust and Deephaven with ADBC

## Instructions

> [!TIP]
> If you already have a Deephaven instance running, skip the steps to set up and clean up Deephaven.

### Prerequisites

1. [Install Rust](https://www.rust-lang.org/tools/install)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Deephaven

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Deephaven instance:

    ```sh
    docker run -d --rm --name deephaven -p 10000:10000 -e START_OPTS="-Dauthentication.psk=YOUR_PASSWORD_HERE" ghcr.io/deephaven/server:latest
    ```

### Connect to Deephaven

1. Install the Flight SQL ADBC driver:

    ```sh
    dbc install flightsql
    ```

2. Customize `src/main.rs` as needed
    - Change the connection arguments in `opts`
        - `OptionDatabase::Uri` is the URI of your Deephaven instance. The host and port will depend on your installation.
        - `OptionDatabase::Other("adbc.flight.sql.authorization_header")` is the authorization header used for requests. Replace `YOUR_PASSWORD_HERE` with your Deephaven pre-shared key.
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `statement.set_sql_query()`

3. Run the Rust program:

    ```sh
    cargo run
    ```

### Clean up

Stop the Docker container running Deephaven:

```sh
docker stop deephaven
```
