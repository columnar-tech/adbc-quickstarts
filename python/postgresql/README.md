<!--
Copyright 2025 Columnar Technologies Inc.

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

# Connecting Python and PostgreSQL with ADBC

## Instructions

> [!TIP]
> If you already have a PostgreSQL instance running, skip the steps to install PostgreSQL, start it, load data, and stop it.

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install PostgreSQL](https://www.postgresql.org/download/)
   - On macOS, if you have Homebrew installed, run `brew install postgresql@17`

1. Follow [these instructions](https://github.com/apache/arrow-adbc/blob/main/CONTRIBUTING.md#python) to build the Python driver manager locally. (Until version 22 of the ADBC libraries are released, you must build the Python driver manager locally to test it with a URI as the only provided option.) After completing those steps, also build a wheel:

   ```sh
   pip install build
   python -m build
   ```

   Note the path to the `.whl` file under `dist/`. You will need it in a later step.

### Set up PostgreSQL

1. Start PostgreSQL
   - If you installed it with Homebrew, run `brew services start postgresql@17`
1. Create a table in PostgreSQL and load data into it by running `psql -d postgres -f games.sql`

### Connect to PostgreSQL

1. Install the PostgreSQL ADBC driver:

   ```sh
   dbc install postgresql
   ```

1. Customize the Python script `main.py` as needed
   - Change the connection arguments in `db_kwargs`
     - Format `uri` according to the [connection URI format used by PostgreSQL](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS), or keep it as is to use the data included with this example
   - If you changed which database you're connecting to, also change the SQL SELECT statement in `cursor.execute()`

1. Use uv to run the Python script, using `--with` to specify the path to the `.whl` file created above. For example:

   ```sh
   uv run --with /path/to/arrow-adbc/python/adbc_driver_manager/dist/adbc_driver_manager-1.10.0.dev0-cp314-cp314-macosx_11_0_arm64.whl main.py
   ```

### Clean up

1. Stop PostgreSQL
   - If you installed it with Homebrew, run `brew services stop postgresql@17`
