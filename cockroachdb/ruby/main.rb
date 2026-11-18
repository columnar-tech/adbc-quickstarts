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
  database.set_option("driver", "postgresql")
  database.set_option("uri", "postgresql://username:password@localhost:26257/db?sslmode=require")
  database.set_load_flags(ADBC::LoadFlags::DEFAULT)
  database.init

  database.connect do |connection|
    connection.open_statement do |statement|
      # CockroachDB does not support the COPY protocol used by the PostgreSQL ADBC driver.
      statement.set_option("adbc.postgresql.use_copy", "false")
      statement.sql_query = "SELECT version()"
      table, = statement.execute
      puts(table)
    end
  end
ensure
  database.release
end
