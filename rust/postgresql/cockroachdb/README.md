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

# Connecting Rust and CockroachDB with ADBC

## Instructions

> [!TIP]
> If you already have a CockroachDB instance running, skip the steps to set up and clean up CockroachDB.

### Prerequisites

1. [Install Rust](https://www.rust-lang.org/tools/install)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up CockroachDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a CockroachDB instance:

    ```sh
    docker run -d --rm \
        --env COCKROACH_DATABASE=db \
        --env COCKROACH_USER=username \
        --env COCKROACH_PASSWORD=password \
        --name=roach-single \
        -p 26257:26257 \
        -p 8080:8080 \
        cockroachdb/cockroach:v25.4.2 start-single-node
    ```

### Connect to CockroachDB

1. Install the PostgreSQL ADBC driver:

    ```sh
    dbc install postgresql
    ```

1. Customize `src/main.rs` as needed
    - Change the connection arguments in `opts`
        - Format `OptionDatabase::Uri` according to the [connection URI format used by PostgreSQL](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `statement.set_sql_query()`

1. Run the Rust program:

    ```sh
    cargo run
    ```

### Clean up

Stop the Docker container running CockroachDB:

```sh
docker stop roach-single
```
