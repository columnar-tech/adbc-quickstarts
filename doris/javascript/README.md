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

# Connecting JavaScript and Apache Doris with ADBC

## Instructions

This example uses [Apache Doris](https://doris.apache.org/), a high-performance, real-time analytical database.

> [!TIP]
> If you already have an Apache Doris instance running, skip the steps to set up Apache Doris.

### Prerequisites

1. [Install Node.js](https://nodejs.org/) (version 22 or later)
   - Alternatively, you can use [Bun](https://bun.sh/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Apache Doris

> [!WARNING]
> This setup process has not been tested on Windows and might not work without modification. Windows users should run it under WSL.

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Download the Apache Doris quick-start script:

   ```sh
   curl -O https://doris.apache.org/files/start-doris.sh
   ```

1. Add Flight SQL ports and configure the backend to advertise `localhost`:

   ```sh
   sed -i.bak -f patch-doris.sed start-doris.sh
   ```

1. Start an Apache Doris cluster:

   ```sh
   chmod 755 start-doris.sh
   ./start-doris.sh
   ```

### Connect to Apache Doris

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install flightsql
   ```

1. Install dependencies:

   ```sh
   npm install
   ```

1. Customize the script `main.js` as needed
   - Change the connection arguments in `databaseOptions`
     - `uri` is the URI of your Apache Doris instance. The host and FE Arrow Flight SQL port will depend on your installation.
     - `username` and `password` are the username and password of your Apache Doris user.
   - Change the SQL SELECT statement in `conn.query()` if desired.

1. Run the script:

   **Node.js:**

   ```sh
   node main.js
   ```

   **Bun:**

   ```sh
   bun run main.js
   ```

### Clean up

Stop the Docker project running Apache Doris:

```sh
docker compose -f docker-compose-doris.yaml down
```
