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

# Connecting Ruby and MotherDuck with ADBC

## Instructions

### Prerequisites

1. [Create a MotherDuck account](https://motherduck.com/)

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

1. (Optional) Create an access token in MotherDuck and save it as the environment variable `motherduck_token` as described at [Authenticating to MotherDuck](https://motherduck.com/docs/key-tasks/authenticating-and-connecting-to-motherduck/authenticating-to-motherduck/#authentication-using-an-access-token). If you skip this step, a browser window will open each time you connect, asking you to log in or confirm access.

### Connect to MotherDuck

1. Install the DuckDB ADBC driver:

   ```sh
   dbc install --level user duckdb
   ```

1. Customize the Ruby script `main.rb` as needed
   - Change the connection arguments in `database.set_option()`
     - Set `path` to the name of a MotherDuck database (prefixed with `md:`), or keep it set to `md:sample_data` to use MotherDuck's sample data
   - Change the SQL SELECT statement in `connection.query()` to query the tables in your database

1. Run the Ruby script:

   ```sh
   bundle exec ruby main.rb
   ```

> [!NOTE]
> If MotherDuck reports that you are not using a compatible DuckDB version, you can install the specific version it requires by running:
> ```sh
> dbc install "duckdb=X.Y.Z"
> ```
