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

# Connecting C# and MariaDB with ADBC

## Instructions

> [!TIP]
> If you already have a MariaDB instance running, skip the steps to set up and clean up MariaDB.

### Prerequisites

1. [Install the .NET SDK](https://dotnet.microsoft.com/download)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up MariaDB

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

2. Start a MariaDB instance:

    ```sh
    docker run --detach --name some-mariadb -p 3306:3306 --env MARIADB_ROOT_PASSWORD=my-secret-pw mariadb:latest
    ```

### Connect to MariaDB

1. Install the MySQL ADBC driver:

    ```sh
    dbc install mysql
    ```

2. Customize the C# program `Program.cs` as needed
    - Change the connection arguments passed to `driver.Open()`
        - Format `uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#readme-dsn-data-source-name), or keep it as is
    - If you changed which database you're connecting to, also change the SQL SELECT statement assigned to `stmt.SqlQuery`

3. Run the C# program:

    ```sh
    dotnet run
    ```

### Clean up

Stop the Docker container running MariaDB:

```sh
docker stop some-mariadb
```
