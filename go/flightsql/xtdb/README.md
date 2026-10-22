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

# Connecting Go and XTDB with ADBC

## Instructions

This example uses [XTDB](https://xtdb.com/), an immutable SQL database with built-in time travel that supports Arrow Flight SQL.

> [!TIP]
> If you already have an XTDB instance running, skip the steps to set up and clean up XTDB.

### Prerequisites

1. [Install Go](https://go.dev/doc/install)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up XTDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Start an XTDB instance:

   ```sh
   docker run -d --rm --name xtdb -p 3000:3000 --pull always ghcr.io/xtdb/xtdb
   ```

   The Flight SQL server is enabled by default in XTDB 2.2.0 and later and listens on port 3000.

1. Wait for XTDB to finish starting up (this usually takes about 10 seconds). XTDB is ready when the container logs include the line `Node started`:

   ```sh
   docker logs xtdb
   ```

### Connect to XTDB

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install flightsql
   ```

1. Customize the Go program `main.go` as needed
   - Change the connection arguments in the `NewDatabase()` call
     - `uri` is the URI of your XTDB Flight SQL server. The host and port will depend on your installation (the default port is 3000). The protocol scheme should be `grpc` or `grpc+tcp`. XTDB's Flight SQL server does not support TLS or authentication, so no username or password is needed.
   - Change the SQL SELECT statement in `stmt.SetSqlQuery()` if desired

1. Run the Go program:

   ```sh
   go mod tidy
   go run main.go
   ```

   The output will look something like this:

   ```
   record:
     schema:
     fields: 1
       - version: type=utf8
     rows: 1
     col[0][version]: ["PostgreSQL 16 (XTDB 2.2.0)"]
   ```

### Clean up

Stop the Docker container running XTDB:

```sh
docker stop xtdb
```
