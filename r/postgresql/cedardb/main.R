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

library(adbcdrivermanager)

drv <- adbc_driver("postgresql")

db <- adbc_database_init(
  drv,
  uri="postgresql://postgres:test@localhost:5432/postgres"
)

con <- adbc_connection_init(db)

stmt <- adbc_statement_init(con)
adbc_statement_set_options(
  stmt,
  list(
    "adbc.postgresql.use_copy"="false"
  )
)
adbc_statement_set_sql_query(stmt, "SELECT version()")

adbc_statement_execute_query(stmt) |>
  tibble::as_tibble() # or:
  # arrow::as_arrow_table() # to keep result in Arrow format
  # arrow::as_record_batch_reader() # for larger results
