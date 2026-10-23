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
  database.set_option("driver", "redshift")
  database.set_option("uri", "postgresql://localhost:5439") # for Redshift Serverless with bastion host
  # database.set_option("uri", "postgresql://localhost:5440") # for Redshift Provisioned with bastion host
  # database.set_option("uri", "postgresql://<cluster hostname>:<cluster port>") # for direct connection
  database.set_option("redshift.cluster_type", "redshift-serverless") # for Redshift Serverless
  # database.set_option("redshift.cluster_type", "redshift-iam") # for Redshift Provisioned with IAM auth
  # database.set_option("redshift.cluster_type", "redshift") # for Redshift Provisioned with user/password auth
  database.set_option("redshift.workgroup_name", "<WORKGROUP_NAME>") # for Redshift Serverless
  # database.set_option("redshift.cluster_identifier", "<CLUSTER IDENTIFIER>") # for Redshift Provisioned
  database.set_option("redshift.db_name", "sample_data_dev")
  database.set_load_flags(ADBC::LoadFlags::DEFAULT)
  database.init

  database.connect do |connection|
    table, = connection.query(<<~SQL)
      SELECT
        l_partkey,
        SUM(l_quantity) as total_ordered
      FROM tpch.lineitem
      GROUP BY l_partkey
      ORDER BY total_ordered DESC
      LIMIT 5;
    SQL
    puts(table)
  end
ensure
  database.release
end
