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

# Connecting JavaScript and InfluxDB with ADBC

## Instructions

This example uses [InfluxDB](https://www.influxdata.com/), a time series database that supports Arrow Flight SQL.

> [!TIP]
> If you already have an InfluxDB instance running, skip the steps to set up and clean up InfluxDB.

### Prerequisites

1. [Install Node.js](https://nodejs.org/) (version 22 or later)
   - Alternatively, you can use [Bun](https://bun.sh/) or [Deno](https://deno.com/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up InfluxDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Start an InfluxDB instance:

   ```sh
   docker run -d --rm --name influxdb -p 8181:8181 influxdb:3-core influxdb3
   ```

1. Create an authorization token:

   ```sh
   docker exec -it influxdb influxdb3 create token --admin
   ```

### Connect to InfluxDB

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install flightsql
   ```

1. Install dependencies:

   ```sh
   npm --prefix ../.. install
   ```

1. Customize the script `main.js` as needed:
   - Change the connection arguments in `databaseOptions`
     - `uri` is the URI of your InfluxDB instance. The host and port will depend on your installation.
     - `adbc.flight.sql.authorization_header` is the authorization header used for requests. Replace `YOUR_AUTH_TOKEN` with your InfluxDB authorization token.
     - `adbc.flight.sql.rpc.call_header.database` is the name of your InfluxDB database.
   - If you changed which database you're connecting to, also change the SQL SELECT statement in `conn.query()`

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

Stop the Docker container running InfluxDB:

```sh
docker stop influxdb
```
