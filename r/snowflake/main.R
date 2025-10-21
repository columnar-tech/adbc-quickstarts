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

drv <- adbc_driver("snowflake")

db <- adbc_database_init(
  drv,

  ### for username/password authentication: ###
  username="USER",
  password="PASS",

  ### for JWT authentication: ####
  #adbc.snowflake.sql.auth_type="auth_jwt",
  #adbc.snowflake.sql.client_option.jwt_private_key="/path/to/rsa_key.p8",

  adbc.snowflake.sql.account="ACCOUNT-IDENT",
  adbc.snowflake.sql.warehouse="MY_WAREHOUSE",
  adbc.snowflake.sql.role="MY_ROLE"
  adbc.snowflake.sql.db="SNOWFLAKE_SAMPLE_DATA",
  adbc.snowflake.sql.schema="TPCH_SF1",
)

con <- adbc_connection_init(db)

con |>
  read_adbc("SELECT * FROM CUSTOMER LIMIT 5") |>
  tibble::as_tibble() # or:
  # arrow::as_arrow_table() # to keep result in Arrow format
  # arrow::as_record_batch_reader() # for larger results
