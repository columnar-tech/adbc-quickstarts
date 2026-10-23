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

using System.Collections;
using Apache.Arrow;

// Apache Arrow for C# has no built-in printer for record batches, so this helper
// prints one column per line. It is not part of the ADBC machinery the example
// demonstrates; it just makes the query results readable.
static class BatchPrinter
{
    public static void Print(RecordBatch batch)
    {
        for (int i = 0; i < batch.ColumnCount; i++)
        {
            Console.WriteLine($"{batch.Schema.FieldsList[i].Name}: {Render(batch.Column(i))}");
        }
    }

    // Render a column's values as a comma-separated string. Most Arrow arrays
    // enumerate as their values, but a few types need special handling: decimal
    // arrays enumerate as raw bytes, and dictionary-encoded arrays (returned for
    // low-cardinality columns) don't enumerate at all, so decode them by index.
    // Nested types (list, struct, map) aren't enumerable either; this helper
    // just names them rather than recursing into their values.
    static string Render(IArrowArray column) => column switch
    {
        Decimal128Array decimals => string.Join(", ",
            Enumerable.Range(0, decimals.Length).Select(decimals.GetString)),
        Decimal256Array decimals => string.Join(", ",
            Enumerable.Range(0, decimals.Length).Select(decimals.GetString)),
        DictionaryArray dictionary => string.Join(", ",
            dictionary.EnumeratePhysicalIndices().Select(i => i < 0 ? "" : DictValues(dictionary)[i])),
        IEnumerable values => string.Join(", ", values.Cast<object?>()),
        _ => $"<{column.Data.DataType.TypeId}>",
    };

    // Materialize a dictionary array's distinct values as strings.
    static string?[] DictValues(DictionaryArray dictionary) =>
        ((IEnumerable)dictionary.Dictionary).Cast<object?>().Select(value => value?.ToString()).ToArray();
}
