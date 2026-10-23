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
  database.set_option("driver", "datafusion")
  database.set_load_flags(ADBC::LoadFlags::DEFAULT)
  database.init

  database.connect do |connection|
    # By default DataFusion reads string columns from Parquet as the Arrow
    # StringView type, which red-arrow cannot yet format. Disable view types so
    # the results use the plain String type. (Queries that produce strings
    # another way, such as a CAST to VARCHAR, may also need
    # datafusion.sql_parser.map_string_types_to_utf8view = false.)
    connection.open_statement do |statement|
      statement.sql_query =
        "SET datafusion.execution.parquet.schema_force_view_types = false"
      statement.execute(need_result: false)
    end

    table, = connection.query("SELECT * FROM 'games.parquet';")
    puts(table)
  end
ensure
  database.release
end
