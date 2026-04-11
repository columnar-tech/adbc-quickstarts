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

# Connecting JavaScript and SingleStore with ADBC

## Instructions

> [!TIP]
> If you already have a SingleStore instance running, skip the steps to set up and clean up SingleStore.

### Prerequisites

1. [Install Node.js](https://nodejs.org/) (version 22 or later)
   - Alternatively, you can use [Bun](https://bun.sh/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up SingleStore

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Start a SingleStore instance:

   ```sh
   docker run \
       -d --rm --name singlestoredb-dev \
       -e ROOT_PASSWORD="YOUR_ROOT_PASSWORD" \
       -p 3306:3306 -p 8080:8080 -p 9000:9000 \
       ghcr.io/singlestore-labs/singlestoredb-dev:latest
   ```

> [!IMPORTANT]
> To run the container on Apple Silicon, add the `--platform linux/amd64` option.

### Connect to SingleStore

1. Install the SingleStore ADBC driver:

   ```sh
   dbc install --pre singlestore
   ```

1. Install dependencies:

   ```sh
   npm install
   ```

1. Customize the script `main.js` as needed
   - Change the connection arguments in `databaseOptions`
     - Format `uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#readme-dsn-data-source-name)
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

### Clean up

Stop the Docker container running SingleStore:

```sh
docker stop singlestoredb-dev
```
