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

# Connecting Kotlin and IBM Db2 with ADBC

## Instructions

> [!TIP]
> If you already have a Db2 instance running, skip the steps to install Db2, start it, load data, and stop it.

### Prerequisites

1.  [Install Gradle](https://docs.gradle.org/current/userguide/installation.html)

1.  [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up IBM Db2

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)
2. Start a Db2 instance:

    ```sh
    docker run --rm --name some-db2 \
        --privileged \
        -p 127.0.0.1:50000:50000 \
        -e LICENSE=accept \
        -e DB2INSTANCE=db2inst1 \
        -e DB2INST1_PASSWORD=password \
        -e DBNAME=testdb \
        icr.io/db2_community/db2
    ```

3. Create a table in Db2 and load data into it:

    ```sh
    cat games.sql | docker exec -i some-db2 su - db2inst1 -c 'db2 -st'
    ```

### Connect to IBM Db2

1. Install the Db2 ADBC driver:

    ```sh
    dbc install --pre db2
    ```

2. Download the [IBM Data Server Driver for ODBC and CLI](https://www.ibm.com/support/pages/getting-started-ibm-data-server-drivers) for your platform and extract the `clidriver` directory.
3. Set `LD_LIBRARY_PATH` (Linux), `DYLD_LIBRARY_PATH` (macOS), or `PATH` (Windows) to make sure the Db2 libraries are discoverable by your application.

    | Platform | Environment variable | Directory to add |
    | --- | --- | --- |
    | Linux | `LD_LIBRARY_PATH` | `clidriver/lib` |
    | macOS | `DYLD_LIBRARY_PATH` | `clidriver/lib` |
    | Windows | `PATH` | `clidriver\bin` |

4. Customize the `main` function in `Main.kt`
    - Change the connection arguments in `params`
        - Format `uri` according to the [driver documentation](https://docs.adbc-drivers.org/drivers/db2/index.html#connecting), or keep it as is to use the data included with this example
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `stmt.setSqlQuery`

5. Run the Kotlin program:

    ```sh
    gradle run
    ```

### Clean up

Stop the Docker container running Db2:

```sh
docker stop some-db2
```
