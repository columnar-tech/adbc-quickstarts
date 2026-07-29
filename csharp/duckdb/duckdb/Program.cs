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

using Apache.Arrow;
using Apache.Arrow.Adbc;
using Apache.Arrow.Adbc.DriverManager;
using Apache.Arrow.Ipc;

using AdbcDriver driver = AdbcDriverManager.FindLoadDriver(
    "duckdb",
    loadOptions: AdbcLoadFlags.Default);

using AdbcDatabase db = driver.Open(new Dictionary<string, string>
{
    ["path"] = "games.duckdb",
});

using AdbcConnection conn = db.Connect(null);
using AdbcStatement stmt = conn.CreateStatement();

stmt.SqlQuery = "SELECT * FROM games;";

QueryResult result = stmt.ExecuteQuery();
using IArrowArrayStream stream = result.Stream!;

while (await stream.ReadNextRecordBatchAsync() is { } batch)
{
    using (batch)
    {
        PrintBatch(batch);
    }
}

// Apache Arrow for C# has no built-in printer for record batches, so print the
// column names followed by each row as tab-separated values.
static void PrintBatch(RecordBatch batch)
{
    Console.WriteLine(string.Join("\t", batch.Schema.FieldsList.Select(field => field.Name)));

    for (int row = 0; row < batch.Length; row++)
    {
        var cells = new string[batch.ColumnCount];
        for (int col = 0; col < batch.ColumnCount; col++)
        {
            cells[col] = FormatValue(batch.Column(col), row);
        }
        Console.WriteLine(string.Join("\t", cells));
    }
}

static string FormatValue(IArrowArray array, int index) => array switch
{
    StringArray a => a.GetString(index) ?? "",
    Int8Array a => a.GetValue(index)?.ToString() ?? "",
    Int16Array a => a.GetValue(index)?.ToString() ?? "",
    Int32Array a => a.GetValue(index)?.ToString() ?? "",
    Int64Array a => a.GetValue(index)?.ToString() ?? "",
    FloatArray a => a.GetValue(index)?.ToString() ?? "",
    DoubleArray a => a.GetValue(index)?.ToString() ?? "",
    BooleanArray a => a.GetValue(index)?.ToString() ?? "",
    Decimal128Array a => a.GetString(index) ?? "",
    Decimal256Array a => a.GetString(index) ?? "",
    _ => array.ToString() ?? "",
};
