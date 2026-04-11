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

# Connecting JavaScript and Exasol with ADBC

## Instructions

> [!TIP]
> If you already have an Exasol instance running, skip the steps to run Exasol in a Docker container.

### Prerequisites

1. [Install Node.js](https://nodejs.org/) (version 22 or later)
   - Alternatively, you can use [Bun](https://bun.sh/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Exasol

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

> [!WARNING]
> The Exasol Docker image may not work with Docker for Windows or Docker for macOS. On macOS, we have found that [Colima](https://colima.run/)'s x86_64 emulation may work better. Alternatively, consider [Exasol Personal](https://www.exasol.com/campaigns/exasol-personal/) running in the cloud.

2. Start Exasol in a Docker container ([documentation](https://github.com/exasol/docker-db)):

   ```sh
   docker run \
      -p 127.0.0.1:9563:8563 \
      --name exasol \
      --privileged \
      --detach \
      exasol/docker-db:latest-2025.1
   ```

3. Create a table in Exasol and load data into it:

   ```sh
   docker cp games.sql exasol:/tmp/games.sql
   docker cp load-data.sh exasol:/tmp/load-data.sh
   docker exec exasol bash /tmp/load-data.sh
   ```

### Connect to Exasol

1. Install the Exasol ADBC driver:

   ```sh
   dbc install exasol
   ```

1. Install dependencies:

   ```sh
   npm --prefix .. install
   ```

1. Customize the script `main.js` as needed
   - Change the connection arguments in `databaseOptions`
     - Change `uri` as needed, using query parameters to add more connection arguments, or keep it as is to use the data included with this example
   - If you changed which schema you're opening, also change the SQL SELECT statement in `conn.query()`

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

1. Stop the Docker container running Exasol:

   ```sh
   docker stop exasol
   docker rm exasol
   ```
