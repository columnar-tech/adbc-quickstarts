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

# Connecting Python and Exasol with ADBC

## Instructions

> [!TIP]
> If you already have an Exasol instance running, skip the steps to run Exasol in a Docker container.

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

### Set up Exasol

1. Start Exasol in a Docker container ([documentation](https://github.com/exasol/docker-db)):

   ```sh
   docker run \
      -p 127.0.0.1:9563:8563 \
      --name exasol \
      --privileged \
      --detach \
      exasol/docker-db:latest-2025.1
   ```

1. Create a table in Exasol and load data into it:

   ```sh
   docker cp games.sql exasol:/tmp/games.sql

   # The Exasol CLI doesn't have an easy flag to trust a self-signed TLS
   # certificate, so try to extract the fingerprint from the error message.
   HOST=$(docker exec exasol /opt/exasol/db-2025.1.9/bin/Console/exaplus -u sys -p exasol -c localhost:8563 2>&1 | tail -n1 | awk '{print $NF}')
   HOST=${HOST%.}

   docker exec exasol /opt/exasol/db-2025.1.9/bin/Console/exaplus \
     -u sys -p exasol -c $HOST -f /tmp/games.sql
   ```

### Connect to Exasol

1. Install the Exasol ADBC driver:

   ```sh
   dbc install exasol
   ```

2. Customize the Python script `main.py` as needed
   - Change the connection arguments in `db_kwargs`
     - Change `uri` as needed, using query parameters to add more connection arguments, or keep it as is to use the data included with this example
   - If you changed which schema you're opening, also change the SQL SELECT statement in `cursor.execute()`

3. Run the Python script:

   ```sh
   uv run main.py
   ```

### Clean up

1. Stop the Docker container running Exasol:

   ```sh
   docker stop exasol
   docker rm exasol
   ```
