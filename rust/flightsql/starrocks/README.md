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

# Connecting Rust and StarRocks with ADBC

## Instructions

This example uses [StarRocks](https://www.starrocks.io/), an open query engine for sub-second, ad-hoc analytics both on and off the data lakehouse.

> [!TIP]
> If you already have a StarRocks instance running, skip the steps to set up StarRocks.

### Prerequisites

1. [Install Rust](https://www.rust-lang.org/tools/install)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up StarRocks

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a StarRocks instance:

    ```sh
    docker run -p 9030:9030 -p 8030:8030 -p 8040:8040 -p 9408:9408 -p 9419:9419 -itd \
    --name quickstart starrocks/allin1-ubuntu
    ```

3. Configure StarRocks for Arrow Flight SQL using one of the following options:

    #### Option A: Quick setup (automated)

    Run these commands from your terminal:

    ```sh
    docker exec quickstart sed -i 's/JAVA_OPTS="-Dlog4j2/JAVA_OPTS="--add-opens=java.base\/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED -Dlog4j2/' /data/deploy/starrocks/fe/conf/fe.conf
    docker exec quickstart bash -c 'echo "arrow_flight_port = 9408" >> /data/deploy/starrocks/fe/conf/fe.conf'
    docker exec quickstart bash -c 'echo "arrow_flight_port = 9419" >> /data/deploy/starrocks/be/conf/be.conf'
    docker restart quickstart
    ```

    #### Option B: Manual setup

    If you prefer to understand and apply the changes yourself:

    1. Open a shell inside the container:
        ```sh
        docker exec -it quickstart bash
        ```

    2. Edit the FE (frontend) configuration:
        ```sh
        vi /data/deploy/starrocks/fe/conf/fe.conf
        ```

        - Find the `JAVA_OPTS` line and add the Arrow memory module at the beginning:
            ```
            JAVA_OPTS="--add-opens=java.base/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED ..."
            ```

        - Add this line at the end of the file:
            ```
            arrow_flight_port = 9408
            ```

    3. Edit the BE (backend) configuration:
        ```sh
        vi /data/deploy/starrocks/be/conf/be.conf
        ```

        - Add this line at the end of the file:
            ```
            arrow_flight_port = 9419
            ```

    4. Exit the container and restart it:
        ```sh
        exit
        docker restart quickstart
        ```

4. Verify the container is ready. Wait for the container to become healthy:

    ```sh
    docker ps --filter "name=quickstart"
    ```

    You should see `(healthy)` in the status before proceeding.

### Connect to StarRocks

1. Install the Flight SQL ADBC driver:

    ```sh
    dbc install flightsql
    ```

2. Customize `src/main.rs` as needed.
    - Change the connection arguments in `opts`.
        - `OptionDatabase::Uri` is the URI of your StarRocks instance. The host and FE Arrow Flight port will depend on your installation.
        - `OptionDatabase::Username` and `OptionDatabase::Password` are the username and password of your StarRocks user.
    - Change the SQL `SELECT` statement in `statement.set_sql_query()` if desired.

3. Run the Rust program:

   ```sh
   cargo run
   `````

### Clean up

Stop the Docker container running StarRocks:

```sh
docker stop quickstart
```
