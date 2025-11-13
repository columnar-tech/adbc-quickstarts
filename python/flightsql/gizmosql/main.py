# Copyright 2025 Columnar Technologies Inc.
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
# dependencies = ["adbc-driver-flightsql>=1.8.0", "pyarrow>=20.0.0"]
# ///

import os

from adbc_driver_flightsql import dbapi as gizmosql, DatabaseOptions

with gizmosql.connect(uri="grpc+tls://localhost:31337",
                      db_kwargs={"username": os.getenv("GIZMOSQL_USERNAME", "gizmosql_username"),
                                 "password": os.getenv("GIZMOSQL_PASSWORD", "gizmosql_password"),
                                 DatabaseOptions.TLS_SKIP_VERIFY.value: "true"
                                 # Not needed if you use a trusted CA-signed TLS cert
                                 }
                      ) as con, con.cursor() as cursor:
    cursor.execute("SELECT n_nationkey, n_name FROM nation WHERE n_nationkey = ?",
                   parameters=[24]
                   )
    table = cursor.fetch_arrow_table()

print(table)
