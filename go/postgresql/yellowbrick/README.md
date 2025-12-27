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

# Connecting Go and Yellowbrick with ADBC

## Instructions

> [!TIP]
> If you already have a Yellowbrick instance running, skip the steps to set up and clean up Yellowbrick.

### Prerequisites

1. [Install Go](https://go.dev/doc/install)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Yellowbrick

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Yellowbrick Community Edition instance:

    ```sh
    docker run -it --privileged --name yellowbrick -p 443:443 -p 5432:5432 yellowbrickdata/yb-community-edition:latest
    ```

### Connect to Yellowbrick

1. Install the PostgreSQL ADBC driver:

    ```sh
    dbc install postgresql
    ```

1. Customize the Go program `main.go` as needed
    - Change the connection arguments in the `NewDatabase()` call
        - Format `uri` according to the [connection URI format used by PostgreSQL](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS), or keep it as is
    - Change the SQL SELECT statement in `stmt.SetSqlQuery()` if desired

1. Run the Go program:

    ```sh
    go mod tidy
    go run main.go
    ```

### Clean up

Stop the Docker container running Yellowbrick:

```sh
docker stop yellowbrick
```
