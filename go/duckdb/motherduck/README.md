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

# Connecting Go and MotherDuck with ADBC

## Instructions

### Prerequisites

1. [Create a MotherDuck account](https://motherduck.com/)

1. [Install Go](https://go.dev/doc/install)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. (Optional) Create an access token in MotherDuck and save it as the environment variable `motherduck_token` as described at [Authenticating to MotherDuck](https://motherduck.com/docs/key-tasks/authenticating-and-connecting-to-motherduck/authenticating-to-motherduck/#authentication-using-an-access-token). If you skip this step, a browser window will open each time you connect, asking you to log in or confirm access.

### Connect to MotherDuck

1. Install the DuckDB ADBC driver:

   ```sh
   dbc install duckdb
   ```

1. Customize the Go program `main.go` as needed
   - Change the connection arguments in the `NewDatabase()` call
     - Set `path` to the name of a MotherDuck database (prefixed with `md:`), or keep it set to `md:sample_data` to use MotherDuck's sample data
   - Change the SQL SELECT statement in `stmt.SetSqlQuery()` to query the tables in your database

1. Run the Go program:

   ```sh
   go mod tidy
   go run main.go
   ```

> [!NOTE]
> If MotherDuck reports that you are not using a compatible DuckDB version, you can install the specific version it requires by running:
> ```sh
> dbc install "duckdb=X.Y.Z"
> ```
