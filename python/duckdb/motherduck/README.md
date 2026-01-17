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

# Connecting Python and MotherDuck with ADBC

## Instructions

### Prerequisites

1. [Create a MotherDuck account](https://motherduck.com/)

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. (Optional) Create an access token in MotherDuck and save it as the environment variable `motherduck_token` as described at [Authenticating to MotherDuck](https://motherduck.com/docs/key-tasks/authenticating-and-connecting-to-motherduck/authenticating-to-motherduck/#authentication-using-an-access-token). If you skip this step, a browser window will open every time ADBC connects to MotherDuck, allowing you to authenticate via OAuth 2.0.

### Connect to MotherDuck

1. Install the DuckDB ADBC driver:

   ```sh
   dbc install duckdb
   ```

   > [!NOTE]
   > If MotherDuck reports that you're not using a compatible DuckDB version, you can install the specific version it requires by running `dbc install "duckdb=X.Y.Z"`.

1. Customize the Python script `main.py` as needed
   - Change the connection arguments in `db_kwargs`
     - Set `path` to a MotherDuck database path (prefixed with `md:`), or keep it set to `md:sample_data` to use MotherDuck's sample data
   - Change the SQL SELECT statement in `cursor.execute()` to query the tables in your database

1. Run the Python script:

   ```sh
   uv run main.py
   ```
