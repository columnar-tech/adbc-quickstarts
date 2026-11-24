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

# Connecting Scala and Materialize with ADBC

## Instructions

> [!TIP]
> If you already have a Materialize instance running, skip the steps to set up and clean up Materialize.

> [!IMPORTANT]
> This example requires Materialize v26.40 or later.

### Prerequisites

1.  [Install sbt](https://www.scala-sbt.org/download/)

2.  [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Materialize

1.  [Install Docker](https://docs.docker.com/get-started/get-docker/)

2.  Start a [Materialize Emulator](https://materialize.com/docs/get-started/install-materialize-emulator/) instance:

    ```sh
    docker run -d --rm --name materialize -p 127.0.0.1:6875:6875 materialize/materialized:latest
    ```

3.  Wait until this command prints `ready`:

    ```sh
    docker exec materialize curl -s localhost:6878/api/readyz
    ```

### Connect to Materialize

1.  Install the PostgreSQL ADBC driver:

    ```sh
    dbc install postgresql
    ```

1.  Customize the `main` function in `Main.scala`
    -   Change the connection arguments in `params`
        -   Format `uri` according to the [connection URI format used by PostgreSQL](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS), or keep it as is
    -   If you changed which database you're connecting to, also change the SQL SELECT statement in `stmt.setSqlQuery`

1.  Run the Scala program:

    ```sh
    sbt run
    ```

### Clean up

Stop the Docker container running Materialize:

```sh
docker stop materialize
```
