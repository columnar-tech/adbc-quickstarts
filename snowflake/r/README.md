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

# Connecting R and Snowflake with ADBC

## Instructions

### Prerequisites

1. [Install R](https://www.r-project.org/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

   ```r
   install.packages(c("adbcdrivermanager", "arrow", "tibble"))
   ```

### Connect to Snowflake

1. Install the Snowflake ADBC driver:

   ```sh
   dbc install snowflake
   ```

1. Customize the R script `main.R`
   - Change the connection arguments in `adbc_database_init()`
     - See [Snowflake Driver Client Options](https://arrow.apache.org/adbc/current/driver/snowflake.html#client-options) for the full list of available options
   - If you changed the database and schema, also change the SQL SELECT statement in `read_adbc()`

1. Run the R script:

   ```sh
   Rscript main.R
   ```
