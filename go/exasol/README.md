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

# Connecting Go and Exasol with ADBC

## Instructions

> [!TIP]
> If you already have an Exasol instance running, skip the steps to run Exasol in a Docker container.

### Prerequisites

1. [Install Go](https://go.dev/doc/install)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. [Install Docker](https://docs.docker.com/get-started/get-docker/)

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

    Note: this container may not work with Docker for Windows or Docker for macOS. On macOS, we have found that [Colima](https://colima.run/)'s x86_64 emulation may work better. Alternatively, consider [Exasol Personal](https://www.exasol.com/campaigns/exasol-personal/) running in the cloud.

1. Create a table in Exasol and load data into it:

    ```sh
    docker cp games.sql exasol:/tmp/games.sql

    # The Exasol CLI doesn't have an easy flag to trust a self-signed TLS
    # certificate, so try to extract the fingerprint from the error message.
    # Also, wait for Exasol to be available.
    while true; do
      export HOST=$(docker exec exasol /opt/exasol/db-2025.1.9/bin/Console/exaplus -u sys -p exasol -c localhost:8563 2>&1 | tail -n1 | awk '{print $NF}')
      if [[ "${HOST}" == "refused" ]]; then
        echo Waiting for Exasol...
        sleep 2
        continue
      fi
      echo Exasol available at ${HOST}
      break
    done
    export HOST=${HOST%.}

    docker exec exasol /opt/exasol/db-2025.1.9/bin/Console/exaplus \
      -u sys -p exasol -c $HOST -f /tmp/games.sql
    ```

### Connect to Exasol

1. Install the Exasol ADBC driver:

    ```sh
    dbc install exasol
    ```

2. Customize the Go program `main.go` as needed
    - Change the connection arguments in the `NewDatabase()` call
        - Change `uri` as needed, using query parameters to add more connection arguments. Format `uri` according to the the following syntax: `exasol://[user[:password]@]host[:port][?param1=value1&param2=value2]`, or keep it as is.
    - Change the SQL SELECT statement in `stmt.SetSqlQuery()`, or keep it as is.

3. Run the Go program:

    ```sh
    go mod tidy
    go run main.go
    ```

### Clean up

1. Stop the Docker container running Exasol:

    ```sh
    docker stop exasol
    docker rm exasol
    ```
