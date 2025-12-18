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

# Connecting R and PostgreSQL with ADBC

## Instructions

> [!TIP]
> If you already have a PostgreSQL instance running, skip the steps to install PostgreSQL, start it, load data, and stop it.

### Prerequisites

1. [Install R](https://www.r-project.org/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install PostgreSQL](https://www.postgresql.org/download/)
   - On macOS, if you have Homebrew installed, run `brew install postgresql@17`

1. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

   ```r
   install.packages(c("adbcdrivermanager", "arrow", "tibble"))
   ```

### Set up PostgreSQL

1. Start PostgreSQL
   - If you installed it with Homebrew, run `brew services start postgresql@17`
1. Create a table in PostgreSQL and load data into it by running `psql -d postgres -f games.sql`

### Connect to PostgreSQL

1. Install the PostgreSQL ADBC driver:

   ```sh
   dbc install postgresql
   ```

1. Customize the R script `main.R` as needed
   - Change the connection arguments in `adbc_database_init()`
     - Format `uri` according to the [connection URI format used by PostgreSQL](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS), or keep it as is to use the data included with this example
   - If you changed which database you're connecting to, also change the SQL SELECT statement in `read_adbc()`

1. Run the R script:

   ```sh
   Rscript main.R
   ```

### Clean up

1. Stop PostgreSQL
   - If you installed it with Homebrew, run `brew services stop postgresql@17`
