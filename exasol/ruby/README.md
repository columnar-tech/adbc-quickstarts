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

# Connecting Ruby and Exasol with ADBC

## Instructions

> [!TIP]
> If you already have an Exasol instance running, skip the steps to run Exasol in a Docker container.

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

### Set up Exasol

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

> [!WARNING]
> The Exasol Docker image may not work with Docker for Windows or Docker for macOS. On macOS, we have found that [Colima](https://colima.run/)'s x86_64 emulation may work better. Alternatively, consider [Exasol Personal](https://www.exasol.com/campaigns/exasol-personal/) running in the cloud.

2. Start Exasol in a Docker container ([documentation](https://github.com/exasol/docker-db)):

   ```sh
   docker run \
      -p 127.0.0.1:9563:8563 \
      --name exasol \
      --privileged \
      --detach \
      exasol/docker-db:latest-2025.1
   ```

3. Create a table in Exasol and load data into it:

   ```sh
   docker cp games.sql exasol:/tmp/games.sql
   docker cp load-data.sh exasol:/tmp/load-data.sh
   docker exec exasol bash /tmp/load-data.sh
   ```

### Connect to Exasol

1. Install the Exasol ADBC driver:

   ```sh
   dbc install --level user exasol
   ```

2. Customize the Ruby script `main.rb` as needed
   - Change the connection arguments in `database.set_option()`
     - Change `uri` as needed, using query parameters to add more connection arguments, or keep it as is to use the data included with this example
   - If you changed which schema you're opening, also change the SQL SELECT statement in `connection.query()`

3. Run the Ruby script:

   ```sh
   bundle exec ruby main.rb
   ```

### Clean up

1. Stop the Docker container running Exasol:

   ```sh
   docker stop exasol
   docker rm exasol
   ```
