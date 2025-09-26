# Connecting Go and Snowflake with ADBC

## Instructions

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Connect to Snowflake

1. Install the Snowflake ADBC driver:

   ```sh
   dbc install snowflake
   ```

1. Customize the Go program `main.go`
   - Change the connection arguments in the `NewDatabase()` call
     - See [Snowflake Driver Client Options](https://arrow.apache.org/adbc/current/driver/snowflake.html#client-options) for the full list of available options
   - If you changed the database and schema, also change the SQL SELECT statement in `stmt.SetSqlQuery()`

1. Run the Go program:

   ```sh
   go mod tidy
   go run main.go
   ```
