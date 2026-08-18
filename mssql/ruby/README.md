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

# Connecting Ruby and Microsoft SQL Server with ADBC

## Instructions

> [!TIP]
> If you already have a SQL Server instance running, skip the steps to run SQL Server in a Docker container.

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

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

### Set up SQL Server

1. Start SQL Server in a Docker container:

   ```sh
   docker run \
      -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Co1umn&r" \
      -p 1433:1433 --name mssql --hostname mssql \
      -d \
      mcr.microsoft.com/mssql/server:2025-latest
   ```

1. Create a table in SQL Server and load data into it:

   ```sh
   docker cp games.sql mssql:/tmp/games.sql

   docker exec -it mssql /opt/mssql-tools18/bin/sqlcmd \
     -S localhost -U sa -P 'Co1umn&r' -C -i /tmp/games.sql
   ```

### Connect to SQL Server

1. Install the SQL Server ADBC driver:

   ```sh
   dbc install --level user mssql
   ```

2. Customize the Ruby script `main.rb` as needed
   - Change the connection arguments in `database.set_option()`
     - Change `uri` as needed, using query parameters to add more connection arguments, or keep it as is to use the data included with this example
   - If you changed which database you're connecting to, also change the SQL SELECT statement in `connection.query()`

> [!TIP]
> To use Microsoft Entra ID for authentication, [install the Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli), log in using the `az login` command, and add `fedauth=` to your connection URI. For example:
>
> ```
> sqlserver://my-database-endpoint.database.windows.net:1433?database=my-database-name&fedauth=ActiveDirectoryDefault
> ```

3. Run the Ruby script:

   ```sh
   bundle exec ruby main.rb
   ```

### Clean up

1. Stop the Docker container running SQL Server:

   ```sh
   docker stop mssql
   docker rm mssql
   ```
