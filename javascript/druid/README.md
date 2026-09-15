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

# Connecting JavaScript and Apache Druid with ADBC

## Instructions

> [!TIP]
> If you already have a Druid instance running, skip the steps to set up Druid.

### Prerequisites

1. [Install Node.js](https://nodejs.org/) (version 22 or later)
   - Alternatively, you can use [Bun](https://bun.sh/) or [Deno](https://deno.com/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Druid

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Start a Druid 37 nano-quickstart instance:

   ```sh
   docker run --detach --rm \
     --name druid \
     --platform linux/amd64 \
     --publish 8888:8888 \
     --volume "$PWD/start-druid.sh:/opt/druid/start-druid.sh:ro" \
     --entrypoint /bin/bash \
     apache/druid:37.0.0 /opt/druid/start-druid.sh
   ```

1. Wait for Druid to accept SQL queries:

   ```sh
   until curl --fail --silent --output /dev/null \
     --header 'Content-Type: application/json' \
     --data '{"query":"SELECT 1"}' \
     http://localhost:8888/druid/v2/sql; do sleep 2; done
   ```

### Connect to Druid

1. Install the Druid ADBC driver:

   ```sh
   dbc install --pre druid
   ```

1. Install dependencies:

   ```sh
   npm --prefix .. install
   ```

1. Customize the script `main.js` as needed
   - Change the connection arguments in `databaseOptions`
     - Format `uri` according to the [driver documentation](https://docs.adbc-drivers.org/drivers/druid/index.html#connecting), or keep it as is

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

Stop the Docker container running Druid:

```sh
docker stop druid
```
