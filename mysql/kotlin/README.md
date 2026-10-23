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

# Connecting Kotlin and MySQL with ADBC

## Instructions

> [!TIP]
> If you already have a MySQL instance running, skip the steps to install MySQL, start it, load data, and stop it.

### Prerequisites

1.  [Install Gradle](https://docs.gradle.org/current/userguide/installation.html)

1.  [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up MySQL

1.  [Install Docker](https://docs.docker.com/get-started/get-docker/)

1.  Start a MySQL instance:

    ```sh
    docker run -d --rm --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 mysql
    ```

1.  Create a table in MySQL and load data into it:

    ```sh
    cat games.sql | docker exec -i some-mysql mysql --user=root --password=my-secret-pw
    ```

### Connect to MySQL

1.  Install the MySQL ADBC driver:

    ```sh
    dbc install mysql
    ```

1.  Customize the `main` function in `Main.kt`
    -   Change the connection arguments in `params`
        -   Format `uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#readme-dsn-data-source-name), or keep it as is to use the data included with this example
    -   If you changed which database you're connecting to, also change the SQL SELECT statement in `stmt.setSqlQuery`

1.  Run the Kotlin program:

    ```sh
    gradle run
    ```

### Clean up

Stop the Docker container running MySQL:

```sh
docker stop some-mysql
```
