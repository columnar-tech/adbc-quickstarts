# Copyright 2026 Columnar Technologies Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# /// script
# requires-python = ">=3.9"
# dependencies = ["adbc-driver-manager>=1.8.0", "pyarrow>=20.0.0"]
# ///

from adbc_driver_manager import dbapi

with (
    dbapi.connect(
        driver="duckdb", db_kwargs={"path": "md:sample_data"}
    ) as con,
    con.cursor() as cursor,
):
    cursor.execute("SELECT title FROM kaggle.movies LIMIT 10;")
    table = cursor.fetch_arrow_table()

print(table)
