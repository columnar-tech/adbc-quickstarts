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

# Connecting R and Apache Spark with ADBC

## Instructions

> [!TIP]
> If you already have a Spark instance running, skip the steps to set up and clean up Spark.

### Prerequisites

1. [Install R](https://www.r-project.org/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

    ```r
    install.packages(c("adbcdrivermanager", "arrow", "tibble"))
    ```

### Set up Spark

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Spark instance:

    ```sh
    docker run -d --rm --name spark-connect -p 15002:15002 apache/spark:4.1.2 bash -c "/opt/spark/sbin/start-connect-server.sh && tail -f /dev/null"
    ```

### Connect to Spark

1. Install the Spark ADBC driver:

    ```sh
    dbc install spark --pre
    ```

2. Customize the R script `main.R`
    - Change the connection arguments in `adbc_database_init()`
        - Format `uri` according to the [driver documentation](https://docs.adbc-drivers.org/drivers/spark/index.html#connecting), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `read_adbc()`

3. Run the R script:

    ```sh
    Rscript main.R
    ```

### Clean up

Stop the Docker container running Spark:

```sh
docker stop spark-connect
```
