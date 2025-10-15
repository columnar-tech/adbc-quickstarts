use adbc_core::options::{AdbcVersion, OptionDatabase};
use adbc_core::{Connection, Database, Driver, LOAD_FLAG_DEFAULT, Statement};
use adbc_driver_manager::ManagedDriver;
use arrow::util::pretty;
use arrow_array::RecordBatch;

fn main() {
    let mut driver = ManagedDriver::load_from_name(
        "trino",
        None,
        AdbcVersion::default(),
        LOAD_FLAG_DEFAULT,
        None,
    )
    .expect("Failed to load driver");

    let opts = [(
        OptionDatabase::Uri,
        "http://user@localhost:8080?catalog=tpch&schema=tiny".into(),
    )];
    let db = driver
        .new_database_with_opts(opts)
        .expect("Failed to create database handle");

    let mut conn = db.new_connection().expect("Failed to create connection");

    let mut statement: adbc_driver_manager::ManagedStatement = conn.new_statement().unwrap();
    statement
        .set_sql_query("
            SELECT nationkey, name, regionkey
            FROM tpch.tiny.nation
            LIMIT 5
        ")
        .unwrap();
    let reader = statement.execute().unwrap();
    let batches: Vec<RecordBatch> = reader.collect::<Result<_, _>>().unwrap();

    pretty::print_batches(&batches).expect("Failed to print batches");
}
