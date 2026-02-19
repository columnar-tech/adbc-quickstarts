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

# Connecting Go and MySQL with ADBC

## Instructions

> [!TIP]
> If you already have a MySQL instance running, skip the steps to install MySQL, start it, load data, and stop it.

### Prerequisites

1. [Install Go](https://go.dev/doc/install)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up MySQL

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a MySQL instance:

    ```sh
    docker run -d --rm --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 mysql
    ```

3. Create a table in MySQL and load data into it:

    ```sh
    cat games.sql | docker exec -i some-mysql mysql --user=root --password=my-secret-pw
    ```

### Connect to MySQL

1. Install the MySQL ADBC driver:

    ```sh
    dbc install mysql
    ```

2. Customize the Go program `main.go` as needed
    - Change the connection arguments in the `NewDatabase()` call
        - Format `uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#section-readme), or keep it as is to use the data included with this example
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `stmt.SetSqlQuery()`

3. Run the Go program:

    ```sh
    go mod tidy
    go run main.go
    ```

### Clean up

Stop the Docker container running MySQL:

```sh
docker stop some-mysql
```
