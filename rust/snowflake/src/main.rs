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
        "snowflake",
        None,
        AdbcVersion::default(),
        LOAD_FLAG_DEFAULT,
        None,
    )
    .expect("Failed to load driver");

    let opts = [
        // for username/password authentication:
        (OptionDatabase::Username, "USER".into()),
        (OptionDatabase::Password, "PASS".into()),

        // for JWT authentication:
        /*
        (
            OptionDatabase::Other("adbc.snowflake.sql.auth_type".to_string()),
            "auth_jwt".into(),
        ),
        (
            OptionDatabase::Other("adbc.snowflake.sql.client_option.jwt_private_key".to_string()),
            "/path/to/rsa_key.p8".into(),
        ),
        */

        (
            OptionDatabase::Other("adbc.snowflake.sql.account".to_string()),
            "ACCOUNT_IDENT".into(),
        ),
        (
            OptionDatabase::Other("adbc.snowflake.sql.warehouse".to_string()),
            "MY_WAREHOUSE".into(),
        ),
        (
            OptionDatabase::Other("adbc.snowflake.sql.db".to_string()),
            "SNOWFLAKE_SAMPLE_DATA".into(),
        ),
        (
            OptionDatabase::Other("adbc.snowflake.sql.schema".to_string()),
            "TPCH_SF1".into(),
        ),
    ];
    let db = driver
        .new_database_with_opts(opts)
        .expect("Failed to create database handle");

    let mut conn = db.new_connection().expect("Failed to create connection");

    let mut statement: adbc_driver_manager::ManagedStatement = conn.new_statement().unwrap();
    statement.set_sql_query("SELECT * FROM CUSTOMER LIMIT 5").unwrap();
    let reader = statement.execute().unwrap();
    let batches: Vec<RecordBatch> = reader.map(|b| b.unwrap()).collect();

    pretty::print_batches(&batches).expect("Failed to print batches");
}
