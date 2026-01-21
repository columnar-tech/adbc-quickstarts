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

# Connecting Rust and Apache Doris with ADBC

## Instructions

> [!TIP]
> If you already have an Apache Doris instance running, skip the steps to set up and clean up Apache Doris.

### Prerequisites

1. [Install Rust](https://rustup.rs/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Apache Doris

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Download the Apache Doris quick-start script:

    ```sh
    curl -O https://doris.apache.org/files/start-doris.sh
    ```

3. Add Flight SQL ports to the script:

    ```sh
    sed -i.bak '/9010:9010/a\
          - 8070:8070\
    ' start-doris.sh
    sed -i.bak '/9050:9050/a\
          - 8050:8050\
    ' start-doris.sh
    ```

4. Start an Apache Doris cluster:

    ```sh
    chmod 755 start-doris.sh
    ./start-doris.sh
    ```

5. Configure Flight SQL ports and restart the cluster:

    ```sh
    docker exec doris-fe-1 bash -c "sed -i 's/arrow_flight_sql_port = -1/arrow_flight_sql_port = 8070/' /opt/apache-doris/fe/conf/fe.conf"
    docker exec doris-be-1 bash -c "sed -i 's/arrow_flight_sql_port = -1/arrow_flight_sql_port = 8050/' /opt/apache-doris/be/conf/be.conf"
    docker compose -p doris restart
    ```

### Connect to Apache Doris

1. Install the Flight SQL ADBC driver:

    ```sh
    dbc install flightsql
    ```

2. Customize the Rust program `main.rs` as needed.
    - Change the connection arguments in the `opts` array.
        - `uri` is the URI of your Apache Doris instance. The host and FE Arrow Flight SQL port will depend on your installation.
        - `username` and `password` are the username and password of your Apache Doris user.
    - Change the SQL `SELECT` statement in `statement.set_sql_query()` if desired.

3. Run the Rust program:

    ```sh
    cargo run
    ```

### Clean up

Stop the Docker project running Apache Doris:

```sh
docker compose -p doris stop
```
