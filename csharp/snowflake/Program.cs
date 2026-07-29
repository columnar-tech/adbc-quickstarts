// Copyright 2026 Columnar Technologies Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

using Apache.Arrow.Adbc;
using Apache.Arrow.Adbc.DriverManager;
using Apache.Arrow.Ipc;

using AdbcDriver driver = AdbcDriverManager.FindLoadDriver(
    "snowflake",
    loadOptions: AdbcLoadFlags.Default);

using AdbcDatabase db = driver.Open(new Dictionary<string, string>
{
    ["username"] = "USER",

    // for username/password authentication:
    ["adbc.snowflake.sql.auth_type"] = "auth_snowflake",
    ["password"] = "PASS",

    // for JWT authentication:
    // ["adbc.snowflake.sql.auth_type"] = "auth_jwt",
    // ["adbc.snowflake.sql.client_option.jwt_private_key"] = "/path/to/rsa_key.p8",

    ["adbc.snowflake.sql.account"] = "ACCOUNT-IDENT",
    ["adbc.snowflake.sql.db"] = "SNOWFLAKE_SAMPLE_DATA",
    ["adbc.snowflake.sql.schema"] = "TPCH_SF1",
    ["adbc.snowflake.sql.warehouse"] = "MY_WAREHOUSE",
    ["adbc.snowflake.sql.role"] = "MY_ROLE",
});

using AdbcConnection conn = db.Connect(null);
using AdbcStatement stmt = conn.CreateStatement();

stmt.SqlQuery = "SELECT * FROM CUSTOMER LIMIT 5";

QueryResult result = stmt.ExecuteQuery();
using IArrowArrayStream stream = result.Stream!;

while (await stream.ReadNextRecordBatchAsync() is { } batch)
{
    using (batch)
    {
        BatchPrinter.Print(batch);
    }
}
