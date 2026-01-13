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
# requires-python = ">=3.13"
# dependencies = [
#     "adbc-driver-manager>=1.10.0",
#     "pyarrow>=22.0.0",
# ]
# ///

from adbc_driver_manager import dbapi

with (
    dbapi.connect(
        driver="flightsql",
        db_kwargs={
            "uri": "grpc+tcp://localhost:8181",
            "adbc.flight.sql.authorization_header": "Bearer YOUR_AUTH_TOKEN",
            "adbc.flight.sql.rpc.call_header.database": "_internal",
        },
    ) as connection,
    connection.cursor() as cursor,
):
    cursor.execute("SELECT * FROM information_schema.tables")
    table = cursor.fetch_arrow_table()

print(table)
