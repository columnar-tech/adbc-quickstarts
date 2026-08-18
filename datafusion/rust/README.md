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

# Connecting Rust and Apache DataFusion with ADBC

## Instructions

### Prerequisites

1. [Install Rust](https://www.rust-lang.org/tools/install)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Connect to DataFusion

1. Install the DataFusion ADBC driver:

   ```sh
   dbc install datafusion
   ```

1. Customize `src/main.rs` as needed
   - Change the SQL SELECT statement in `statement.set_sql_query()`, or keep it set to `SELECT * FROM 'games.parquet'` to query the Parquet file included with this example

1. Run the Rust program:

   ```sh
   cargo run
   ```
