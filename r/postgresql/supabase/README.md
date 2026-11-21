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

# Connecting R and Supabase with ADBC

## Instructions

### Prerequisites

1. [Install R](https://www.r-project.org/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

    ```r
    install.packages(c("adbcdrivermanager", "arrow", "tibble"))
    ```

4. [Create a Supabase account](https://supabase.com/dashboard) and a Supabase project, and note the database password you set when you create the project

5. Copy the connection string for your project: in your Supabase project dashboard, click Connect at the top of the page, select Direct connection, and copy the connection string. Replace the password placeholder in it with your database password
    - Supabase does not display the database password after you create the project. If you have lost it, reset it in the same dialog
    - If your password contains `@`, `/`, `%`, or a space, percent-encode those characters (for example, replace `@` with `%40`)
    - The direct connection requires IPv6 unless your project has the paid IPv4 add-on. If your network does not support IPv6, select Session pooler instead

### Connect to Supabase

1. Install the PostgreSQL ADBC driver:

    ```sh
    dbc install postgresql
    ```

2. Customize the R script `main.R` as needed
    - Change the connection arguments in `adbc_database_init()`
        - Set `uri` to the connection string you copied, keeping `?sslmode=require` at the end
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `read_adbc()`

3. Run the R script:

    ```sh
    Rscript main.R
    ```
