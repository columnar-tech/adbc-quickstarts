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

# Connecting Ruby and InfluxDB with ADBC

## Instructions

This example uses [InfluxDB](https://www.influxdata.com/), a time series database that supports Arrow Flight SQL.

> [!TIP]
> If you already have an InfluxDB instance running, skip the steps to set up and clean up InfluxDB.

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

### Set up InfluxDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start an InfluxDB instance:

    ```sh
    docker run -d --rm --name influxdb -p 8181:8181 influxdb:3-core influxdb3
    ```

3. Create an authorization token:

    ```sh
    docker exec -it influxdb influxdb3 create token --admin
    ```

### Connect to InfluxDB

1. Install the Flight SQL ADBC driver:

    ```sh
    dbc install --level user flightsql
    ```

2. Customize the Ruby script `main.rb` as needed.
    - Change the connection arguments in `database.set_option()`.
        - `uri` is the URI of your InfluxDB instance. The host and port will depend on your installation.
        - `adbc.flight.sql.authorization_header` is the authorization header used for requests. Replace `YOUR_AUTH_TOKEN` with your InfluxDB authorization token.
        - `adbc.flight.sql.rpc.call_header.database` is the name of your InfluxDB database.
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `connection.query()`.

3. Run the Ruby script:

    ```sh
    bundle exec ruby main.rb
    ```

### Clean up

Stop the Docker container running InfluxDB:

```sh
docker stop influxdb
```
