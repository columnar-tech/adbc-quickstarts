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

# Connecting Go and GizmoSQL with ADBC


## Instructions

This example uses [GizmoSQL](https://gizmodata.com/gizmosql), a lightweight, high-performance SQL server powered by DuckDB or SQLite that supports Arrow Flight SQL.

> [!TIP]
> If you already have a GizmoSQL instance running, skip the steps to set up GizmoSQL.

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up GizmoSQL server (if you don't already have one)

1. [Install Docker Engine](https://docs.docker.com/engine/install/)

1. Start the GizmoSQL server:

   ```sh
   docker run -d --rm -it --init -p 31337:31337 --name gizmosql -e DATABASE_FILENAME=adbc_quickstart.db -e TLS_ENABLED=0 -e GIZMOSQL_PASSWORD=gizmosql_password -e PRINT_QUERIES=1 -e INIT_SQL_COMMANDS='CALL dbgen(sf=0.01);' --pull always gizmodata/gizmosql:latest-slim
    ```

### Connect to GizmoSQL

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install flightsql
   ```

1. Customize the Go program `main.go` as needed
   - Change the connection arguments in the `NewDatabase()` call
     - `uri` is the URI of your GizmoSQL instance. The host and port will depend on your installation (the default port is 31337). The protocol scheme should be `grpc` or `grpc+tcp` if your GizmoSQL instance is not using TLS and should be `grpc+tls` otherwise.
     - `username` and `password` are the username and password of your GizmoSQL admin user (the one specified when starting the instance).
     - You can optionally use JWT token authentication with GizmoSQL server (see more [here](https://github.com/gizmodata/generate-gizmosql-token)) - with username: `token` and a password value of the JWT token contents. 

1. Run the Go program:

   ```sh
   go mod tidy
   go run main.go
   ```

   The output will look something like this:

   ```
   record:
     schema:
     fields: 3
       - r_regionkey: type=int32, nullable
       - r_name: type=utf8, nullable
       - r_comment: type=utf8, nullable
     rows: 5
     col[0][r_regionkey]: [0 1 2 3 4]
     col[1][r_name]: ["AFRICA" "AMERICA" "ASIA" "EUROPE" "MIDDLE EAST"]
     col[2][r_comment]: ["ar packages. regular excuses among the ironic requests cajole fluffily blithely final requests. furiously express p" "s are. furiously even pinto bea" "c, special dependencies around " "e dolphins are furiously about the carefully " " foxes boost furiously along the carefully dogged tithes. slyly regular orbits according to the special epit"]
   ```

### Clean up

1. Stop and remove the Docker container running GizmoSQL:

   ```sh
   docker stop gizmosql
   ```
