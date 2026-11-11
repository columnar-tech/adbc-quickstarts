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

# Connecting Ruby and Databricks with ADBC

## Instructions

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

3. [Create a Databricks account](https://www.databricks.com/) or be able to log in to an existing one.

### Set up Databricks

1. Log into [Databricks](https://login.databricks.com/) and create or locate an existing SQL warehouse.

2. Open the "Connection details" tab and record the server hostname and HTTP path. See the Databricks documentation describing [how to get these connection details](https://docs.databricks.com/integrations/compute-details).

### Connect to Databricks

1. Install the Databricks ADBC driver:

    ```sh
    dbc install --level user databricks
    ```

2. Customize the Ruby script `main.rb`:
    - Change the connection arguments in `database.set_option()`:
        - `uri` is the URI for your Databricks instance. The script includes several authentication options. See the [Databricks ADBC driver documentation](https://docs.adbc-drivers.org/drivers/databricks/) for details.
    - Change the SQL SELECT statement in `connection.query()`, or keep it as is.
        - Specify the catalog and schema by fully qualifying the table name as `catalog.schema.table`.

3. Run the Ruby script:

    ```sh
    bundle exec ruby main.rb
    ```
