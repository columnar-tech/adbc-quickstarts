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

# Connecting C# and Dremio with ADBC

## Instructions

This example uses [Dremio](https://www.dremio.com/), a data lakehouse platform that supports Arrow Flight SQL.

> [!TIP]
> If you already have a Dremio instance running, skip the steps to set up Dremio.

### Prerequisites

1. [Install the .NET SDK](https://dotnet.microsoft.com/download)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Dremio

1. [Sign up for Dremio Cloud](https://www.dremio.com/) or follow the instructions to [set up Dremio Community](https://docs.dremio.com/current/get-started/docker/).

### Connect to Dremio

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install flightsql
   ```

1. Customize the C# program `Program.cs` as needed
   - Change the connection arguments passed to `driver.Open()`
     - `uri` is the URI of your Dremio instance. The host and port will depend on your installation (the default port is 32010). The protocol scheme should be `grpc` or `grpc+tcp` if your Dremio instance is not using TLS (e.g. if you are using Dremio Community) and should be `grpc+tls` otherwise (e.g. when using Dremio Cloud).
     - `username` and `password` are the username and password of your Dremio account. (If you are using Dremio Community, these were set during the installation instructions.)
     - For Dremio Cloud, remove `username` and `password`, create a personal access token (PAT), store it in a string variable `token` in the program, and set the connection arguments to:

       ```csharp
       string token = "YOUR_PERSONAL_ACCESS_TOKEN";
       using AdbcDatabase db = driver.Open(new Dictionary<string, string>
       {
           ["uri"] = "grpc+tls://data.dremio.cloud:443", // for US region
           // ["uri"] = "grpc+tls://data.eu.dremio.cloud:443", // for Europe region
           ["adbc.flight.sql.authorization_header"] = "Bearer " + token,
       });
       ```

   - If you changed `uri` to point to a different Flight SQL server, also change the SQL SELECT statement assigned to `stmt.SqlQuery`

1. Run the C# program:

   ```sh
   dotnet run
   ```

   The output will look something like this:

   ```
   EXPR$0: 1.4362464230987455
   ```
