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

# Connecting JavaScript and Apache DataFusion with ADBC

## Instructions

### Prerequisites

1. [Install Node.js](https://nodejs.org/) (version 22 or later)
   - Alternatively, you can use [Bun](https://bun.sh/) or [Deno](https://deno.com/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Connect to DataFusion

1. Install the DataFusion ADBC driver:

   ```sh
   dbc install datafusion
   ```

1. Install dependencies:

   ```sh
   npm install
   ```

1. Customize the script `main.js` as needed
   - Change the SQL SELECT statement in `conn.query()`, or keep it set to `SELECT * FROM 'games.parquet';` to query the Parquet file included with this example
   - The `conn.execute()` call disables DataFusion's Arrow StringView output for Parquet scans so that the results can be decoded by the `apache-arrow` JavaScript library; keep it as is
     - If you change the query to produce string columns another way (for example, casting to `VARCHAR`), you may also need to set `datafusion.sql_parser.map_string_types_to_utf8view = false`

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
