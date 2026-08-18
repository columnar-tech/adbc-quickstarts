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

# Connecting Ruby and Oracle Database with ADBC

## Instructions

> [!TIP]
> If you already have an Oracle Database instance running, skip the steps to set up and clean up Oracle Database.

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

### Set up Oracle Database

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a Oracle Database instance:

    ```sh
    docker run -d --rm --name oracle-db -p 1521:1521 -e ORACLE_PWD=password container-registry.oracle.com/database/free:latest
    ```

3. Wait about a minute for the database to initialize.

### Connect to Oracle Database

1. The ADBC driver for Oracle is available from Columnar's private driver registry. Create a [Columnar Console](https://console.columnar.tech) account and activate a 14-day free trial. Then authenticate to the registry:

    ```sh
    dbc auth login
    ```

2. Install the ADBC driver for Oracle:

    ```sh
    dbc install --level user oracle
    ```

3. Install the [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html) libraries.

4. Set `LD_LIBRARY_PATH` (Linux), `DYLD_LIBRARY_PATH` (macOS), or `PATH` (Windows) to make sure the Oracle Instant Client libraries are discoverable by your application.

5. Customize the Ruby script `main.rb` as needed:
    - Change the connection arguments in `database.set_option()`.
        - Format `uri` according to the the following syntax: `oracle://[user[:password]@]host[:port][/serviceName][?param1=value1&param2=value2]`, or keep it as is.
    - Change the SQL SELECT statement in `connection.query()`, or keep it as is.

6. Run the Ruby script:

   ```sh
   bundle exec ruby main.rb
   ```

### Clean up

Stop the Docker container running Oracle Database:

```sh
docker stop oracle-db
```
