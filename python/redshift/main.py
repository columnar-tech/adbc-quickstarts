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
# requires-python = ">=3.10"
# dependencies = ["adbc-driver-manager>=1.8.0", "pyarrow>=20.0.0"]
# ///

from adbc_driver_manager import dbapi

with dbapi.connect(
    driver="redshift",
    db_kwargs={
        "uri": "postgresql://localhost:5439", # for Redshift Serverless with bastion host
        #"uri": "postgresql://localhost:5440", # for Redshift Provisioned with bastion host
        #"uri": "postgresql://<cluster hostname>:<cluster port>", # for direct connection

        "redshift.cluster_type": "redshift-serverless", # for Redshift Serverless
        #"redshift.cluster_type": "redshift-iam", # for Redshift Provisioned with IAM auth
        #"redshift.cluster_type": "redshift", # for Redshift Provisioned with user/password auth

        "redshift.workgroup_name": "<WORKGROUP_NAME>", # for Redshift Serverless
        #"redshift.cluster_identifier": "<CLUSTER IDENTIFIER>", # for Redshift Provisioned

        "redshift.db_name": "sample_data_dev",
    }
) as con, con.cursor() as cursor:
    cursor.execute("""
      SELECT
        l_partkey,
        SUM(l_quantity) as total_ordered
      FROM tpch.lineitem
      GROUP BY l_partkey
      ORDER BY total_ordered DESC
      LIMIT 5;
    """)
    table = cursor.fetch_arrow_table()

print(table)
