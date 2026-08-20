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

# Connecting JavaScript and Presto with ADBC

## Instructions

> [!TIP]
> If you already have a Presto instance running, skip the steps to run Presto in a Docker container.

### Prerequisites

1. [Install Node.js](https://nodejs.org/) (version 22 or later)
   - Alternatively, you can use [Bun](https://bun.sh/) or [Deno](https://deno.com/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Presto

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Start a Presto instance:

   ```sh
   docker run -d --rm --name presto -p 8080:8080 prestodb/presto:latest
   ```

### Connect to Presto

1. Install the Presto ADBC driver:

   ```sh
   dbc install --pre presto
   ```

1. Install dependencies:

   ```sh
   npm --prefix .. install
   ```

1. Customize the script `main.js` as needed
   - Change the connection arguments in `databaseOptions`
     - Format `uri` according to the [driver documentation](https://docs.adbc-drivers.org/drivers/presto/index.html#connecting), or keep it as is to use the TPC-H data included in the Presto Docker container image

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

Stop the Docker container running Presto:

```sh
docker stop presto
```
