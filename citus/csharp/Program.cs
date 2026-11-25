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
    "postgresql",
    loadOptions: AdbcLoadFlags.Default);

using AdbcDatabase db = driver.Open(new Dictionary<string, string>
{
    ["uri"] = "postgresql://postgres:password@localhost:5432/postgres",
});

using AdbcConnection conn = db.Connect(null);
using AdbcStatement stmt = conn.CreateStatement();

stmt.SqlQuery = "SELECT * FROM citus_version()";

QueryResult result = stmt.ExecuteQuery();
using IArrowArrayStream stream = result.Stream!;

while (await stream.ReadNextRecordBatchAsync() is { } batch)
{
    using (batch)
    {
        BatchPrinter.Print(batch);
    }
}
