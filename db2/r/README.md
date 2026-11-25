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

# Connecting R and IBM Db2 with ADBC

## Instructions

> [!TIP]
> If you already have a Db2 instance running, skip the steps to install Db2, start it, load data, and stop it.

### Prerequisites

1. [Install R](https://www.r-project.org/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

    ```r
    install.packages(c("adbcdrivermanager", "arrow", "tibble"))
    ```

### Set up IBM Db2

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

> [!IMPORTANT]
> To run the container on Apple Silicon, add the `--platform linux/amd64` option.

2. Start a Db2 instance:

    ```sh
    docker run -d --rm --name db2server \
        --privileged \
        -p 127.0.0.1:50000:50000 \
        -e LICENSE=accept \
        -e DB2INSTANCE=db2inst1 \
        -e DB2INST1_PASSWORD=password \
        -e DBNAME=testdb \
        icr.io/db2_community/db2
    ```

3. Wait until the container logs show `Setup has completed`.

    ```sh
    docker logs db2server 2>&1 | grep 'Setup has completed'
    ```

4. Create a table in Db2 and load data into it:

    ```sh
    cat games.sql | docker exec -i db2server su - db2inst1 -c 'db2 -st'
    ```

### Connect to IBM Db2

1. Install the Db2 ADBC driver:

    ```sh
    dbc install --pre db2
    ```

2. Download the [IBM Data Server Driver for ODBC and CLI](https://public.dhe.ibm.com/ibmdl/export/pub/software/data/db2/drivers/odbc_cli/) for your platform and extract the `clidriver` directory.

3. Make sure the Db2 libraries are discoverable by your application:
    - Linux: Add `clidriver/lib` to `LD_LIBRARY_PATH`
    - macOS: Move the `clidriver` directory into the directory where dbc installed the driver (by default, `~/Library/Application Support/ADBC/Drivers`)
    - Windows: Add `clidriver\bin` to `PATH`

4. Customize the R script `main.R` as needed
    - Change the connection arguments in `adbc_database_init()`
        - Format `uri` according to the [driver documentation](https://docs.adbc-drivers.org/drivers/db2/index.html#connecting), or keep it as is to use the data included with this example
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `read_adbc()`

5. Run the R script:

    ```sh
    Rscript main.R
    ```

### Clean up

Stop the Docker container running Db2:

```sh
docker stop db2server
```
