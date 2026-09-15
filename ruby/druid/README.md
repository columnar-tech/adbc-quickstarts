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

# Connecting Ruby and Apache Druid with ADBC

## Instructions

> [!TIP]
> If you already have a Druid instance running, skip the steps to set up Druid.

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

### Set up Druid

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Start a Druid 37 nano-quickstart instance:

   ```sh
   docker run --detach --rm \
     --name druid \
     --platform linux/amd64 \
     --publish 8888:8888 \
     --volume "$PWD/start-druid.sh:/opt/druid/start-druid.sh:ro" \
     --entrypoint /bin/bash \
     apache/druid:37.0.0 /opt/druid/start-druid.sh
   ```

1. Wait for Druid to accept SQL queries:

   ```sh
   until curl --fail --silent --output /dev/null \
     --header 'Content-Type: application/json' \
     --data '{"query":"SELECT 1"}' \
     http://localhost:8888/druid/v2/sql; do sleep 2; done
   ```

### Connect to Druid

1. Install the Druid ADBC driver:

   ```sh
   dbc install --level user --pre druid
   ```

1. Customize the Ruby script `main.rb` as needed
   - Change the connection arguments in `database.set_option()`
     - Format `uri` according to the [driver documentation](https://docs.adbc-drivers.org/drivers/druid/index.html#connecting), or keep it as is

1. Run the Ruby script:

   ```sh
   bundle exec ruby main.rb
   ```

### Clean up

1. Stop the Docker container running Druid:

   ```sh
   docker stop druid
   ```
