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

# Connecting C++ and MotherDuck with ADBC

## Instructions

### Prerequisites

1. [Install Pixi](https://pixi.prefix.dev/latest/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Create a MotherDuck account](https://motherduck.com/)

1. Create an access token in MotherDuck as described in [Authenticating to MotherDuck](https://motherduck.com/docs/key-tasks/authenticating-and-connecting-to-motherduck/authenticating-to-motherduck/#authentication-using-an-access-token), then set the `MOTHERDUCK_TOKEN` environment variable, which the MotherDuck ADBC driver reads when connecting:

   ```sh
   export MOTHERDUCK_TOKEN="YOUR_MOTHERDUCK_TOKEN"
   ```

### Connect to MotherDuck

1. Install the MotherDuck ADBC driver:

   ```sh
   dbc install --level user --pre motherduck
   ```

1. Customize the C++ program `main.cpp` as needed
   - Change the connection arguments in the `AdbcDatabaseSetOption()` calls
     - Set `motherduck.region` to your account's region, which you can find by running `SELECT * FROM md_user_info();` in MotherDuck
     - Replace `my_db` in `uri` with the name of your MotherDuck database
     - See the [driver documentation](https://adbc-drivers.org/drivers/motherduck/#connecting) for the full list of available options
   - Change the SQL SELECT statement in `AdbcStatementSetSqlQuery()` to query the tables in your database

1. Build and run the C++ program:

   Using Make:
   ```sh
   pixi run make
   ./motherduck_demo
   ```

   Or using CMake:
   ```sh
   pixi run cmake -B build
   pixi run cmake --build build
   ./build/motherduck_demo
   ```

### Clean up

1. Clean build artifacts:

   Using Make:
   ```sh
   pixi run make clean
   ```

   Using CMake:
   ```sh
   rm -rf build
   ```
