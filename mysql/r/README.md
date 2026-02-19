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

# Connecting R and MySQL with ADBC

## Instructions

> [!TIP]
> If you already have a MySQL instance running, skip the steps to install MySQL, start it, load data, and stop it.

### Prerequisites

1. [Install R](https://www.r-project.org/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

    ```r
    install.packages(c("adbcdrivermanager", "arrow", "tibble"))
    ```

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

2. Customize the R script `main.R` as needed
    - Change the connection arguments in `adbc_database_init()`
        - Format `uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#section-readme), or keep it as is to use the data included with this example
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `read_adbc()`

3. Run the R script:

    ```sh
    Rscript main.R
    ```

### Clean up

Stop the Docker container running MySQL:

```sh
docker stop some-mysql
```
