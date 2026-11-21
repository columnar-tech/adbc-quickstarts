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

# Connecting Go and Supabase with ADBC

## Instructions

### Prerequisites

1. [Install Go](https://go.dev/doc/install)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. [Create a Supabase account](https://supabase.com/dashboard) and a Supabase project, and note the database password you set when you create the project

4. Copy the connection string for your project: in your Supabase project dashboard, click Connect at the top of the page, select Direct connection, and copy the connection string. Replace the password placeholder in it with your database password
    - Supabase does not display the database password after you create the project. If you have lost it, reset it in the same dialog
    - If your password contains `@`, `/`, `%`, or a space, percent-encode those characters (for example, replace `@` with `%40`)
    - The direct connection requires IPv6 unless your project has the paid IPv4 add-on. If your network does not support IPv6, select Session pooler instead

### Connect to Supabase

1. Install the PostgreSQL ADBC driver:

    ```sh
    dbc install postgresql
    ```

1. Customize the Go program `main.go` as needed
    - Change the connection arguments in the `NewDatabase()` call
        - Set `uri` to the connection string you copied, keeping `?sslmode=require` at the end
    - If you changed which database you're connecting to, also change the SQL SELECT statement in `stmt.SetSqlQuery()`

1. Run the Go program:

    ```sh
    go mod tidy
    go run main.go
    ```
