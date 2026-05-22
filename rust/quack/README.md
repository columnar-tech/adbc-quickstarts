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

# Connecting Rust and DuckDB Quack Server with ADBC

## Instructions

> [!TIP]
> If you already have a DuckDB Quack server instance running, skip the steps to set up DuckDB.

### Prerequisites

1. [Install Rust](https://www.rust-lang.org/tools/install)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install DuckDB](https://duckdb.org/install/)

### Set up DuckDB server

1. Start the DuckDB CLI:

    ```sh
    duckdb
    ```

1. Create a table:

    ```sql
    CREATE TABLE penguins AS FROM read_csv('https://blobs.duckdb.org/data/penguins.csv', nullstr = 'NA');
    ```

1. Start a server from the DuckDB session:

    ```sql
    CALL quack_serve('quack:localhost');
    ```

### Connect to DuckDB via Quack protocol

1. Install the Quack ADBC driver:

    ```sh
    dbc install --pre quack
    ```

1. Customize `src/main.rs` as needed
    - Change the `uri` connection argument in `opts`
        - Replace `YOUR_AUTH_TOKEN` with the auth token for your DuckDB server
        - Change the host and port if applicable
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `statement.set_sql_query()`

1. Run the Rust program:

    ```sh
    cargo run
    ```

### Clean up

If you started a DuckDB server, exit the DuckDB CLI:

```sql
.exit
```
