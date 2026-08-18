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
  database.set_option("driver", "flightsql")
  database.set_option("uri", "grpc+tcp://localhost:32010")
  database.set_option("username", "admin")
  database.set_option("password", "password1")
  database.set_load_flags(ADBC::LoadFlags::DEFAULT)
  database.init

  database.connect do |connection|
    table, = connection.query(<<~SQL)
      SELECT AVG(tip_amount)
      FROM Samples."samples.dremio.com"."NYC-taxi-trips-iceberg"
    SQL
    puts(table)
  end
ensure
  database.release
end
