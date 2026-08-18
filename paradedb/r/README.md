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

# Connecting R and ParadeDB with ADBC

## Instructions

> [!TIP]
> If you already have a ParadeDB instance running, skip the steps to set up and clean up ParadeDB.

### Prerequisites

1. [Install R](https://www.r-project.org/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

    ```r
    install.packages(c("adbcdrivermanager", "arrow", "tibble"))
    ```

### Set up ParadeDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a ParadeDB instance:

    ```sh
    docker run -d --rm --name paradedb -e POSTGRES_PASSWORD=password -p 5432:5432 paradedb/paradedb
    ```

### Connect to ParadeDB

1. Install the PostgreSQL ADBC driver:

    ```sh
    dbc install postgresql
    ```

1. Customize the R script `main.R` as needed
    - Change the connection arguments in `adbc_database_init()`
        - Format `uri` according to the [connection URI format used by PostgreSQL](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `read_adbc()`

2. Run the R script:

    ```sh
    Rscript main.R
    ```

### Clean up

Stop the Docker container running ParadeDB:

```sh
docker stop paradedb
```
