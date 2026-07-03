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

# Connecting Ruby and Sail with ADBC

## Instructions

This example uses [Sail](https://docs.lakesail.com/), a fast query engine that supports Arrow Flight SQL.

> [!TIP]
> If you already have a Sail Flight SQL server running, skip the steps to set up Sail.

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

### Set up Sail

1. Install Sail:

   ```sh
   uv tool install pysail
   ```

1. Start the Sail Flight SQL server:

   ```sh
   sail flight server --ip 127.0.0.1 --port 32010
   ```

   Alternatively, you can start the server programmatically using the Sail Python API. Install `pysail` into your environment:

   ```sh
   uv pip install pysail
   ```

   Then start the server:

   ```python
   from pysail.flight import FlightSqlServer

   server = FlightSqlServer(ip="127.0.0.1", port=32010)
   server.start(background=False)
   ```

### Connect to Sail

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install --level user flightsql
   ```

1. Customize the Ruby script `main.rb` as needed
   - Change the connection arguments in `database.set_option()`
     - `uri` is the URI of your Sail Flight SQL server. The host and port will depend on your installation (the default port is 32010). The protocol scheme should be `grpc` for plain connections or `grpc+tls` if your server is configured with TLS.
   - Change the SQL SELECT statement in `connection.query()` if desired

1. Run the Ruby script:

   ```sh
   bundle exec ruby main.rb
   ```

   The output will look something like this:

   ```
   	 result
   	(int64)
   0	      2
   ```

### Clean up

Stop the Sail Flight SQL server by pressing `Ctrl-C` in the terminal where it is running.
