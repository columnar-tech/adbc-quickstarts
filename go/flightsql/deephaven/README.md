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

# Connecting Go and Deephaven with ADBC

## Instructions

This example queries Deephaven using [Arrow Flight SQL](https://deephaven.io/core/docs/how-to-guides/flight-sql/).

Deephaven's Flight SQL interface is read-only. Each `SELECT` query returns a static snapshot, even for ticking tables. For authentication and session options, see [Deephaven's ADBC examples](https://deephaven.io/core/docs/how-to-guides/flight-sql/#adbc).

> [!TIP]
> If you already have a Deephaven instance running, skip the steps to set up and clean up Deephaven.

### Prerequisites

1. [Install Go](https://go.dev/doc/install)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Deephaven

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Deephaven instance:

    ```sh
    docker run -d --rm --name deephaven -p 127.0.0.1:10000:10000 \
        -e START_OPTS=-Dauthentication.psk=deephaven ghcr.io/deephaven/server:latest
    ```

3. Wait until Docker reports `healthy`.

    ```sh
    docker inspect --format '{{.State.Health.Status}}' deephaven
    ```

### Connect to Deephaven

1. Install the Flight SQL ADBC driver:

    ```sh
    dbc install flightsql
    ```

2. Customize the Go program `main.go` as needed.
    - Change the connection arguments in the `NewDatabase()` call.
        - `uri` is the Flight SQL endpoint of your Deephaven instance. Use `grpc+tls://` for an endpoint with TLS.
        - For pre-shared key authentication, replace the final `deephaven` in `adbc.flight.sql.authorization_header` with your key. Deephaven prints generated keys in the server log. If your instance allows anonymous access, set the header to `Anonymous`.
        - The `x-deephaven-auth-cookie-request` header asks Deephaven for a session cookie. The Flight SQL driver's cookie middleware sends it on subsequent requests.
    - To query a table in Deephaven's global query scope, change the SQL SELECT statement in `stmt.SetSqlQuery()`.

3. Run the Go program:

    ```sh
    go mod tidy
    go run main.go
    ```

### Clean up

Stop the Docker container running Deephaven:

```sh
docker stop deephaven
```
