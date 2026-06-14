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

# Connecting Ruby and Apache DataFusion with ADBC

## Instructions

### Prerequisites

1. [Install Ruby](https://www.ruby-lang.org/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. Install the native Arrow GLib and ADBC GLib libraries required by `red-adbc`.

   On macOS with Homebrew:

   ```sh
   brew install apache-arrow-glib apache-arrow-adbc-glib
   ```

1. Install Ruby dependencies:

   ```sh
   bundle install
   ```

   If you have multiple Ruby installations, ensure `ruby` and `bundle` resolve
   to the same installation before running this command.

### Connect to DataFusion

1. Install the DataFusion ADBC driver:

   ```sh
   dbc install --level user datafusion
   ```

1. Customize the Ruby script `main.rb` as needed
   - Change the SQL SELECT statement in `connection.query()`, or keep it set to `SELECT * FROM 'games.parquet';` to query the Parquet file included with this example
   - The `SET` statement disables DataFusion's Arrow StringView output for Parquet scans so that the results can be decoded and formatted by `red-arrow`; keep it as is
     - If you change the query to produce string columns another way (for example, casting to `VARCHAR`), you may also need to set `datafusion.sql_parser.map_string_types_to_utf8view = false`

1. Run the Ruby script:

   ```sh
   bundle exec ruby main.rb
   ```
