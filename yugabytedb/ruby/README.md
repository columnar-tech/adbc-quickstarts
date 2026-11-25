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

# Connecting Ruby and YugabyteDB with ADBC

## Instructions

> [!TIP]
> If you already have a YugabyteDB instance running, skip the steps to set up and clean up YugabyteDB.

### Prerequisites

1. [Install Ruby](https://www.ruby-lang.org/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

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

### Set up YugabyteDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a YugabyteDB instance:

    ```sh
    docker run -d --rm --name yugabyte \
        -p 9999:9999 -p 9000:9000 -p 15433:15433 -p 5433:5433 -p 9042:9042 \
        yugabytedb/yugabyte:2025.2.0.0-b131 bin/yugabyted start --master_webserver_port=9999 \
        --background=false
    ```

### Connect to YugabyteDB

1. Install the PostgreSQL ADBC driver:

    ```sh
    dbc install --level user postgresql
    ```

2. Customize the Ruby script `main.rb` as needed
    - Change the connection arguments in `database.set_option()`
        - Format `uri` according to the [connection URI format used by PostgreSQL](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `connection.query()`

3. Run the Ruby script:

   ```sh
   bundle exec ruby main.rb
   ```

### Clean up

Stop the Docker container running YugabyteDB:

```sh
docker stop yugabyte
```
