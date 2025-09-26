# Connecting Rust and Snowflake with ADBC

## Instructions

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Connect to Snowflake

1. Install the Snowflake ADBC driver:

   ```sh
   dbc install snowflake
   ```

1. Customize `src/main.rs` as needed
   - Change the connection arguments in `opts`
     - See [Snowflake Driver Client Options](https://arrow.apache.org/adbc/current/driver/snowflake.html#client-options) for the full list of available options
   - If you changed the database and schema, also change the SQL SELECT statement in `statement.set_sql_query()`

1. Run the Rust program:

   ```sh
   cargo run
   ```
