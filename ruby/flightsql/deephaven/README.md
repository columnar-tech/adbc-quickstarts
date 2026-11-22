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

# Connecting Ruby and Deephaven with ADBC

## Instructions

This example queries Deephaven using [Arrow Flight SQL](https://deephaven.io/core/docs/how-to-guides/flight-sql/).

> [!TIP]
> If you already have a Deephaven instance running, skip the steps to set up and clean up Deephaven.

### Prerequisites

1. [Install Ruby](https://www.ruby-lang.org/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. Ensure the native Arrow GLib and ADBC GLib libraries required by `red-adbc`
   are installed and discoverable. If `bundle install` reports missing `arrow`,
   `arrow-glib`, or `adbc-glib`, use the platform-specific commands below.

   <details>
   <summary>macOS with Homebrew</summary>

   ```sh
   brew install apache-arrow-glib apache-arrow-adbc-glib
   ```

   </details>

   <details>
   <summary>Debian/Ubuntu</summary>

   ```sh
   sudo apt install libarrow-glib-dev libadbc-glib-dev
   ```

   </details>

   <details>
   <summary>RHEL-compatible distributions</summary>

   ```sh
   sudo dnf install arrow-glib-devel adbc-glib-devel
   ```

   </details>

   <details>
   <summary>Windows with RubyInstaller/MSYS2 UCRT64</summary>

   ```sh
   pacman -S --needed mingw-w64-ucrt-x86_64-arrow mingw-w64-ucrt-x86_64-arrow-adbc-glib
   ```

   If you use a different MSYS2 environment, adjust the package prefix to match
   it; for example, use `mingw-w64-x86_64-*` from the MINGW64 shell.

   </details>

1. Install Ruby dependencies:

   ```sh
   bundle install
   ```

   If you have multiple Ruby installations, ensure `ruby` and `bundle` resolve
   to the same installation before running this command.

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
    dbc install --level user flightsql
    ```

2. Customize the Ruby script `main.rb` as needed.
    - Change the connection arguments in `database.set_option()`. For authentication and session options, see [Deephaven's ADBC examples](https://deephaven.io/core/docs/how-to-guides/flight-sql/#adbc).
        - `uri` is the Flight SQL endpoint of your Deephaven instance. Use `grpc+tls://` for an endpoint with TLS.
        - For pre-shared key authentication, replace the final `deephaven` in `adbc.flight.sql.authorization_header` with your key. Deephaven prints generated keys in the server log. If your instance allows anonymous access, set the header to `Anonymous`.
        - The `x-deephaven-auth-cookie-request` header asks Deephaven for a session cookie. The Flight SQL driver's cookie middleware sends it on subsequent requests.
    - To query a table in Deephaven's global query scope, change the SQL SELECT statement in `connection.query()`. Deephaven's Flight SQL interface is read-only and returns a static snapshot, even for ticking tables.

3. Run the Ruby script:

    ```sh
    bundle exec ruby main.rb
    ```

### Clean up

Stop the Docker container running Deephaven:

```sh
docker stop deephaven
```
