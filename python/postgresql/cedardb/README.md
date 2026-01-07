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

# Connecting Python and CedarDB with ADBC

## Instructions

> [!TIP]
> If you already have a CedarDB instance running, skip the steps to set up and clean up CedarDB.

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up CedarDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a CedarDB instance:

    ```sh
    docker run -d --rm --name cedardb -p 5432:5432 -e CEDAR_PASSWORD=test cedardb/cedardb
    ```

### Connect to CedarDB

1. Install the PostgreSQL ADBC driver:

    ```sh
    dbc install postgresql
    ```

2. Customize the Python script `main.py` as needed
    - Change the connection arguments in `db_kwargs`
        - Format `uri` according to the [connection URI format used by PostgreSQL](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `cursor.execute()`

3. Run the Python script:

   ```sh
   uv run main.py
   ```

### Clean up

Stop the Docker container running CedarDB:

```sh
docker stop cedardb
```
