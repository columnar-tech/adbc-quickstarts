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

# Connecting R and TiDB with ADBC

## Instructions

> [!TIP]
> If you already have a TiDB instance running, skip the steps to set up and clean up TiDB.

### Prerequisites

1. [Install R](https://www.r-project.org/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. Install the R packages `arrow`, `adbcdrivermanager`, and `tibble`:

    ```r
    install.packages(c("arrow", "adbcdrivermanager", "tibble"))
    ```

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

2. Customize the R script `main.R` as needed
    - Change the connection arguments in `adbc_database_init()`
        - Format `uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#section-readme), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `read_adbc()`

3. Run the R script:

    ```sh
    Rscript main.R
    ```

### Clean up

Stop the Docker container running TiDB:

```sh
docker stop tidb-single
```
