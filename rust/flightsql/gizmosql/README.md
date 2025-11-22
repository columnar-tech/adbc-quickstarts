<!--
Copyright 2025 Columnar Technologies Inc.

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

# Connecting Rust and GizmoSQL (an Arrow Flight SQL server - powered by DuckDB or SQLite) with ADBC

## Instructions

This example uses [GizmoSQL](https://gizmodata.com/gizmosql), but other open source tools and vendor products that support Arrow Flight SQL will also work with this driver.

> [!TIP]
> If you already have a GizmoSQL instance running, skip the steps to set up GizmoSQL.

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up GizmoSQL server (if you don't already have one)

1. [Install Docker Engine](https://docs.docker.com/engine/install/)

1. Start the GizmoSQL server:
```bash
docker run -d --rm -it --init -p 31337:31337 --name gizmosql -e DATABASE_FILENAME=adbc_quickstart.db -e TLS_ENABLED=0 -e GIZMOSQL_PASSWORD=gizmosql_password -e PRINT_QUERIES=1 -e INIT_SQL_COMMANDS='CALL dbgen(sf=0.01);' --pull always gizmodata/gizmosql:latest-slim
```

### Connect to GizmoSQL

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install flightsql
   ```

1. Customize `src/main.rs` as needed
   - Change the connection arguments in `opts`
     - `OptionDatabase::Uri` is the URI of your GizmoSQL instance. The host and port will depend on your installation (the default port is 31337). The protocol scheme should be `grpc` or `grpc+tcp` if your GizmoSQL instance is not using TLS and should be `grpc+tls` otherwise.
     - `OptionDatabase::Username` and `OptionDatabase::Password` are the username and password of your GizmoSQL admin user (the one specified when starting the instance).

1. Run the Rust program:

   ```sh
   cargo run
   ```
