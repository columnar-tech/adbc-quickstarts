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

# Connecting R and SingleStore with ADBC

## Instructions

> [!TIP]
> If you already have a SingleStore instance running, skip the steps to set up and clean up SingleStore.

### Prerequisites

1. [Install R](https://www.r-project.org/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

    ```r
    install.packages(c("adbcdrivermanager", "arrow", "tibble"))
    ```

### Set up SingleStore

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a SingleStore instance:

    ```sh
    docker run \
        -d --rm --name singlestoredb-dev \
        -e ROOT_PASSWORD="YOUR_ROOT_PASSWORD" \
        -p 3306:3306 -p 8080:8080 -p 9000:9000 \
        ghcr.io/singlestore-labs/singlestoredb-dev:latest
    ```

    To run the image on Apple Silicon, add the `--platform linux/amd64` option.

### Connect to SingleStore

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

Stop the Docker container running SingleStore:

```sh
docker stop singlestoredb-dev
```
