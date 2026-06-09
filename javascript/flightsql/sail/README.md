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

# Connecting JavaScript and Sail with ADBC

## Instructions

This example uses [Sail](https://docs.lakesail.com/), a fast query engine that supports Arrow Flight SQL.

> [!TIP]
> If you already have a Sail Flight SQL server running, skip the steps to set up Sail.

### Prerequisites

1. [Install Node.js](https://nodejs.org/) (version 22 or later)
   - Alternatively, you can use [Bun](https://bun.sh/) or [Deno](https://deno.com/)

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Sail

1. Install Sail:

   ```sh
   uv tool install pysail
   ```

1. Start the Sail Flight SQL server:

   ```sh
   sail flight server --ip 127.0.0.1 --port 32010
   ```

### Connect to Sail

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install flightsql
   ```

1. Install dependencies:

   ```sh
   npm --prefix ../.. install
   ```

1. Customize the script `main.js` as needed
   - Change the connection arguments in `databaseOptions`
     - `uri` is the URI of your Sail Flight SQL server. The host and port will depend on your installation (the default port is 32010). The protocol scheme should be `grpc` for plain connections or `grpc+tls` if your server is configured with TLS.
   - Change the SQL SELECT statement in `conn.query()` if desired

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

### Clean up

Stop the Sail Flight SQL server by pressing `Ctrl-C` in the terminal where it is running.
