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

# Connecting Rust and Arrow Flight SQL with ADBC

## Instructions

This example uses [Dremio](https://www.dremio.com/), but other open source tools and vendor products that support Arrow Flight SQL will also work with this driver.

> [!TIP]
> If you already have a Dremio instance running, skip the steps to set up Dremio.

### Prerequisites

1. [Install Rust](https://www.rust-lang.org/tools/install)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Dremio

1. [Sign up for Dremio Cloud](https://www.dremio.com/) or follow the instructions to [set up Dremio Community](https://docs.dremio.com/current/get-started/docker/).

### Connect to Dremio

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install flightsql
   ```

1. Customize `src/main.rs` as needed
   - Change the connection arguments in `opts`
     - `OptionDatabase::Uri` is the URI of your Dremio instance. The host and port will depend on your installation (the default port is 32010). The protocol scheme should be `grpc` or `grpc+tcp` if your Dremio instance is not using TLS (e.g. if you are using Dremio Community) and should be `grpc+tls` otherwise (e.g. when using Dremio Cloud).
     - `OptionDatabase::Username` and `OptionDatabase::Password` are the username and password of your Dremio account. (If you are using Dremio Community, these were set during the installation instructions.)
     - For Dremio Cloud, don't use username and password; instead create a personal access token (PAT), store it in a string variable `token` in `main()`, and set the options to:

       ```rs
       let opts = [
            (
                OptionDatabase::Uri,
                "grpc+tls://data.dremio.cloud:443".into(), // for US region
                //"grpc+tls://data.eu.dremio.cloud:443".into(), // for Europe region
            ),
            (
                OptionDatabase::Other("adbc.flight.sql.authorization_header".to_string()),
                format!("Bearer {}", token).into(),
            ),
       ];
       ```

   - If you changed `OptionDatabase::Uri` to point to a different Flight SQL server, also change the SQL SELECT statement in `statement.set_sql_query()`

1. Run the Rust program:

   ```sh
   cargo run
   ```
