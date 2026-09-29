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

require "adbc"

database = ADBC::Database.new

begin
  database.set_option("driver", "snowflake")
  database.set_option("username", "USER")
  # for username/password authentication:
  database.set_option("adbc.snowflake.sql.auth_type", "auth_snowflake")
  database.set_option("password", "PASS")
  # for JWT authentication:
  # database.set_option("adbc.snowflake.sql.auth_type", "auth_jwt")
  # database.set_option("adbc.snowflake.sql.client_option.jwt_private_key", "/path/to/rsa_key.p8")
  database.set_option("adbc.snowflake.sql.account", "ACCOUNT-IDENT")
  database.set_option("adbc.snowflake.sql.db", "SNOWFLAKE_SAMPLE_DATA")
  database.set_option("adbc.snowflake.sql.schema", "TPCH_SF1")
  database.set_option("adbc.snowflake.sql.warehouse", "MY_WAREHOUSE")
  database.set_option("adbc.snowflake.sql.role", "MY_ROLE")
  database.set_load_flags(ADBC::LoadFlags::DEFAULT)
  database.init

  database.connect do |connection|
    table, = connection.query("SELECT * FROM CUSTOMER LIMIT 5")
    puts(table)
  end
ensure
  database.release
end
