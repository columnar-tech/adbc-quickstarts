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

# Connecting R and StarRocks with ADBC

## Instructions

This example uses [StarRocks](https://www.starrocks.io/), an open query engine for sub-second, ad-hoc analytics both on and off the data lakehouse.

> [!TIP]
> If you already have a StarRocks instance running, skip the steps to set up StarRocks.

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

2. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

    ```r
    install.packages(c("adbcdrivermanager", "arrow"))
    install.packages("tibble")
    ```

### Set up StarRocks

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a StarRocks instance:

    ```sh
    docker run -p 9030:9030 -p 8030:8030 -p 8040:8040 -p 9408:9408 -p 9419:9419 -itd \
    --name quickstart starrocks/allin1-ubuntu
    ```

3. Configure StarRocks for Arrow Flight SQL:
    1. Specify the FE configuration item `JAVA_OPTS` in `fe.conf`:
        ```sh
        JAVA_OPTS="--add-opens=java.base/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED ..."
        ```
    2. In both FE configuration file `fe.conf` and BE configuration file `be.conf`, set `arrow_flight_port` to an available port:
        ```
        // fe.conf
        arrow_flight_port = 9408

        // be.conf
        arrow_flight_port = 9419
        ```
    3. Restart the FE and BE services:
        ```sh
        docker restart quickstart
        ```

### Connect to StarRocks

1. Install the Flight SQL ADBC driver:

    ```sh
    dbc install flightsql
    ```

2. Customize the R script `main.R` as needed.
    - Change the connection arguments in `adbc_database_init()`
        - `uri` is the URI of your StarRocks instance. The host and FE Arrow Flight port will depend on your installation.
        - `username` and `password` are the username and password of your StarRocks user.
    - Change the SQL `SELECT` statement in `read_adbc()` if desired.

3. Run the R script:
    ```sh
    Rscript main.R
    ```

### Clean up

Stop the Docker container running StarRocks:

```sh
docker stop quickstart
```
