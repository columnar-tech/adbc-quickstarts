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

# Connecting Node.js and SQLite with ADBC

## Instructions

### Prerequisites

1. [Install Node.js 22+](https://nodejs.org/en/download)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install SQLite](https://www.sqlite.org/download.html)
   - On macOS, if you have Homebrew installed, run `brew install sqlite`

### Connect to SQLite

1. Install the SQLite ADBC driver:

   ```sh
   dbc install sqlite
   ```

1. Install the `adbc-driver-manager` package.

   > **Note:** Until this package is published to npm, build and install it from source:
   >
   > ```sh
   > git clone --branch gh-3734 https://github.com/kentkwu/arrow-adbc.git
   > pushd arrow-adbc/javascript
   > npm install
   > npm run build
   > popd
   > npm install arrow-adbc/javascript apache-arrow
   > ```
   >
   > Once published, this will simply be:
   >
   > ```sh
   > npm install
   > ```

1. Customize the script `main.js` as needed
   - Change `uri` in the `databaseOptions` to the location of the SQLite database file you want to query, or keep it set to `games.sqlite` to use the database file included with this example
   - If you changed the database file, also change the SQL SELECT statement in `conn.query()`

1. Run the script:

   ```sh
   node main.js
   ```
