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

# Connecting JavaScript and DuckDB with ADBC

## Instructions

### Prerequisites

1. [Install Node.js](https://nodejs.org/) (version 22 or later)
   - Alternatively, you can use [Bun](https://bun.sh/) or [Deno](https://deno.com/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install DuckDB](https://duckdb.org/docs/installation/)
   - On macOS, if you have Homebrew installed, run `brew install duckdb`

### Connect to DuckDB

1. Install the DuckDB ADBC driver:

   ```sh
   dbc install duckdb
   ```

1. Install dependencies:

   ```sh
   npm --prefix ../.. install
   ```

1. Customize the script `main.js` as needed
   - Change the `path` in `databaseOptions` to the location of the DuckDB database file you want to query, or keep it set to `games.duckdb` to use the database file included with this example
   - If you changed the database file, also change the SQL SELECT statement in `conn.query()`

1. Run the script:

   **Node.js:**

   ```sh
   node main.js
   ```

   **Bun:**

   ```sh
   bun run main.js
   ```

   **Deno:**

   ```sh
   deno run --allow-ffi --allow-env main.js
   ```
