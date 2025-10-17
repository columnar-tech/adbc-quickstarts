// Copyright 2025 Columnar Technologies Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

use adbc_core::options::{AdbcVersion, OptionDatabase};
use adbc_core::{Connection, Database, Driver, LOAD_FLAG_DEFAULT, Statement};
use adbc_driver_manager::ManagedDriver;
use arrow::util::pretty;
use arrow_array::RecordBatch;

fn main() {
    let mut driver = ManagedDriver::load_from_name(
        "redshift",
        None,
        AdbcVersion::default(),
        LOAD_FLAG_DEFAULT,
        None,
    )
    .expect("Failed to load driver");

    let opts = [
        (
            OptionDatabase::Uri,
            "postgresql://localhost:5439".into(), // for Redshift Serverless with bastion host
            //"postgresql://localhost:5440".into(), // for Redshift Provisioned with bastion host
            //"postgresql://<cluster hostname>:<cluster port>".into(), // for direct connection
        ),
        (
            OptionDatabase::Other("redshift.cluster_type".to_string()),
            "redshift-serverless".into(), // for Redshift Serverless
            //"redshift-iam".into(), // for Redshift Provisioned with IAM auth
            //"redshift".into(), // for Redshift Provisioned with user/password auth
        ),
        // For Redshift Serverless:
        (
            OptionDatabase::Other("redshift.workgroup_name".to_string()),
            "<WORKGROUP_NAME>".into(),
        ),
        // Uncomment for Redshift Provisioned:
        // (
        //     OptionDatabase::Other("redshift.cluster_identifier".to_string()),
        //     "<CLUSTER IDENTIFIER>".into(),
        // ),
        (
            OptionDatabase::Other("redshift.db_name".to_string()),
            "sample_data_dev".into(),
        ),
    ];

    let db = driver
        .new_database_with_opts(opts)
        .expect("Failed to create database handle");

    let mut conn = db.new_connection().expect("Failed to create connection");

    let mut statement: adbc_driver_manager::ManagedStatement = conn.new_statement().unwrap();
    statement
        .set_sql_query(
            "
        SELECT
            l_partkey,
            SUM(l_quantity) as total_ordered
        FROM tpch.lineitem
        GROUP BY l_partkey
        ORDER BY total_ordered DESC
        LIMIT 5;
    ",
        )
        .unwrap();
    let reader = statement.execute().unwrap();
    let batches: Vec<RecordBatch> = reader.collect::<Result<_, _>>().unwrap();

    pretty::print_batches(&batches).expect("Failed to print batches");
}
