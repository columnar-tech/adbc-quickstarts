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

# Connecting Ruby and DuckDB Quack Server with ADBC

## Instructions

> [!TIP]
> If you already have a DuckDB Quack server instance running, skip the steps to set up DuckDB.

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

1. [Install DuckDB](https://duckdb.org/install/)

### Set up DuckDB server

1. Start the DuckDB CLI:

    ```sh
    duckdb
    ```

1. Create a table:

    ```sql
    CREATE TABLE penguins AS FROM read_csv('https://blobs.duckdb.org/data/penguins.csv', nullstr = 'NA');
    ```

1. Start a server from the DuckDB session:

    ```sql
    CALL quack_serve('quack:localhost');
    ```

    Note the `auth_token` value that DuckDB prints.

### Connect to DuckDB via Quack protocol

1. Install the Quack ADBC driver:

    ```sh
    dbc install --level user --pre quack
    ```

1. Customize the Ruby script `main.rb` as needed
    - Change the `uri` connection argument
        - Replace `YOUR_AUTH_TOKEN` with the `auth_token` printed by DuckDB
        - Change the host and port if applicable
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `connection.query()`

1. Run the Ruby script:

    ```sh
    bundle exec ruby main.rb
    ```

### Clean up

If you started a DuckDB server, exit the DuckDB CLI:

```sql
.exit
```
