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

# Connecting Python and Vitess with ADBC

## Instructions

> [!TIP]
> If you already have a Vitess instance running, skip the steps to set up and clean up Vitess.

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Vitess

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Vitess instance:

    ```sh
    docker run -d --rm --name=vttestserver \
        -p 33574:33574 \
        -p 33575:33575 \
        -p 33577:33577 \
        -e PORT=33574 \
        -e KEYSPACES=test,unsharded \
        -e NUM_SHARDS=2,1 \
        -e MYSQL_MAX_CONNECTIONS=70000 \
        -e MYSQL_BIND_HOST=0.0.0.0 \
        -e VTCOMBO_BIND_HOST=0.0.0.0 \
        vitess/vttestserver:mysql80
    ```

    Wait a few moments before continuing to the next step to allow the Vitess container to fully initialize.

### Connect to Vitess

1. Install the MySQL ADBC driver:

    ```sh
    dbc install mysql
    ```

2. Customize the Python script `main.py` as needed
    - Change the connection arguments in `db_kwargs`
        - Format `uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#section-readme), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `cursor.execute()`

3. Run the Python script:

    ```sh
    uv run main.py
    ```

### Clean up

Stop the Docker container running Vitess:

```sh
docker stop vttestserver
```
