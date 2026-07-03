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

# Connecting Ruby and Teradata with ADBC

## Instructions

> [!TIP]
> If you don't already have a Teradata instance running, we recommend signing up for a free [ClearScape Analytics trial](https://www.teradata.com/getting-started/demos/clearscape-analytics).

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

### Connect to Teradata

1. The ADBC driver for Teradata is available from Columnar's private driver registry. Create a [Columnar Console](https://console.columnar.tech) account and activate a 14-day free trial. Then authenticate to the registry:

    ```sh
    dbc auth login
    ```

2. Install the ADBC driver for Teradata:

    ```sh
    dbc install --level user teradata
    ```

3. Download and install the [Teradata Tools and Utilities (TTU)](https://downloads.teradata.com/). Select "Tools and Utilities" and choose the package for your platform. Install to the default location:
    - Linux: `/opt/teradata`
    - macOS: `/Library/Application Support/teradata`
    - Windows: `C:\Program Files\Teradata\Client`

    On Windows, you can do this with `winget install Teradata.TTUBase`

    On macOS with Homebrew, you can do this with `brew tap Teradata/teradata && brew install ttubasesuite`

4. Set `LD_LIBRARY_PATH` (Linux), `DYLD_LIBRARY_PATH` (macOS), or `PATH` (Windows) to make sure the TTU libraries are discoverable by your application.

5. Customize the Ruby script `main.rb`:
    - Change the connection arguments in `database.set_option()`.
        - `uri` is the URI of your Teradata instance. The format is `teradata://user:password@host[:port]`.
    - Change the SQL SELECT statement in `connection.query()`.

6. Run the Ruby script:

    ```sh
    bundle exec ruby main.rb
    ```
