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

# Connecting C# and MotherDuck with ADBC

## Instructions

### Prerequisites

1. [Create a MotherDuck account](https://motherduck.com/)

1. [Install the .NET SDK](https://dotnet.microsoft.com/download)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. Create an access token in MotherDuck as described in [Authenticating to MotherDuck](https://motherduck.com/docs/key-tasks/authenticating-and-connecting-to-motherduck/authenticating-to-motherduck/#authentication-using-an-access-token), then set the `MOTHERDUCK_TOKEN` environment variable:

   ```sh
   export MOTHERDUCK_TOKEN="YOUR_MOTHERDUCK_TOKEN"
   ```

### Connect to MotherDuck

1. Install the MotherDuck ADBC driver:

   ```sh
   dbc install --pre motherduck
   ```

1. Customize the C# program `Program.cs` as needed:
   - Set `motherduck.region` to your account's region, which you can find by running `SELECT md_user_info();` in MotherDuck. The example uses `us-east-1`.
   - Replace `my_db` in the `uri` with your database name. See the [driver documentation](https://adbc-drivers.org/drivers/motherduck/#connecting).

1. Run the C# program:

   ```sh
   dotnet run
   ```
