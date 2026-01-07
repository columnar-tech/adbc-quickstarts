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

# Connecting Go and TiDB with ADBC

## Instructions

> [!TIP]
> If you already have a TiDB instance running, skip the steps to set up and clean up TiDB.

### Prerequisites

1. [Install Go](https://go.dev/doc/install)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up TiDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a TiDB instance:

    ```sh
    docker run -d --rm --name tidb-single -p 4000:4000 pingcap/tidb
    ```

### Connect to TiDB

1. Install the MySQL ADBC driver:

    ```sh
    dbc install mysql
    ```

2. Customize the Go program `main.go` as needed
    - Change the connection arguments in `drv.NewDatabase()`
        - Format `uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#section-readme), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `stmt.SetSqlQuery()`

3. Run the Go program:

    ```sh
    go mod tidy
    go run main.go
    ```

### Clean up

Stop the Docker container running TiDB:

```sh
docker stop tidb-single
```
