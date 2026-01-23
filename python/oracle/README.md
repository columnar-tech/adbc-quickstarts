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

# Connecting Python and Oracle Database with ADBC

## Instructions

> [!TIP]
> If you already have an Oracle Database instance running, skip the steps to set up and clean up Oracle Database.

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Oracle Database

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Oracle Database instance:

    ```sh
    docker run -d --rm --name oracle-db -p 1521:1521 -e ORACLE_PWD=password container-registry.oracle.com/database/free:latest
    ```

### Connect to Oracle Database

1. The ADBC driver for Oracle is available from Columnar's private driver registry. Create a [Columnar Cloud](https://cloud.columnar.tech) account and activate a 14-day free trial. Then authenticate to the registry:

    ```sh
    dbc auth login
    ```

2. Install the ADBC driver for Oracle:

    ```sh
    dbc install oracle
    ```

3. Install the [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html) libraries.

4. Set `LD_LIBRARY_PATH` (Linux), `DYLD_LIBRARY_PATH` (macOS), or `PATH` (Windows) to make sure the Oracle Instant Client libraries are discoverable by your application.

5. Customize the Python script `main.py` as needed:
    - Change the connection arguments in `db_kwargs`.
        - Format `uri` according to the the following syntax: `oracle://[user[:password]@]host[:port][/serviceName][?param1=value1&param2=value2]`, or keep it as is.
    - Change the SQL SELECT statement in `cursor.execute()`, or keep it as is.

6. Run the Python script:

   ```sh
   uv run main.py
   ```

### Clean up

Stop the Docker container running Oracle Database:

```sh
docker stop oracle-db
```
