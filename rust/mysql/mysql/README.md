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

# Connecting Rust and MySQL with ADBC

## Instructions

> [!TIP]
> If you already have a MySQL instance running, skip the steps to install MySQL, start it, load data, and stop it.

### Prerequisites

1. [Install Rust](https://www.rust-lang.org/tools/install)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install MySQL](https://dev.mysql.com/downloads/installer/)
   - On macOS, if you have Homebrew installed, run `brew install mysql`

### Set up MySQL

1. Start MySQL
   - If you installed it with Homebrew, run `brew services start mysql`

1. Create a table in MySQL and load data into it by running `mysql -u root < games.sql`

### Connect to MySQL

1. Install the MySQL ADBC driver:

   ```sh
   dbc install mysql
   ```

1. Customize `src/main.rs` as needed
   - Change the connection arguments in `opts`
     - Format `OptionDatabase::Uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#section-readme), or keep it as is to use the data included with this example
   - If you changed which database you're connecting to, also change the SQL SELECT statement in `statement.set_sql_query()`

1. Run the Rust program:

   ```sh
   cargo run
   ```

### Clean up

1. Stop MySQL
   - If you installed it with Homebrew, run `brew services stop mysql`
