# Connecting Go and Arrow Flight SQL with ADBC

## Instructions

This example uses [Dremio](https://www.dremio.com/), but other open source tools and vendor products that support Arrow Flight SQL will also work with this driver.

> [!TIP]
> If you already have a Dremio instance running, skip the steps to set up Dremio.

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Set up Dremio

1. [Sign up for Dremio Cloud](https://www.dremio.com/) or follow the instructions to [set up Dremio Community](https://docs.dremio.com/current/get-started/docker/).

### Connect to Dremio

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install flightsql
   ```

1. Customize the Go program `main.go` as needed
   - Change the connection arguments in the `NewDatabase()` call
     - `uri` is the URI of your Dremio instance. The host and port will depend on your installation (the default port is 32010). The protocol scheme should be `grpc` or `grpc+tcp` if your Dremio instance is not using TLS (e.g. if you are using Dremio Community) and should be `grpc+tls` otherwise (e.g. when using Dremio Cloud).
     - `username` and `password` are the username and password of your Dremio account.
     (If you are using Dremio Community, these were set during the installation instructions.)
     - For Dremio Cloud, remove `username` and `password`, create a personal access token (PAT), store it in a string variable `token` in the program, and set the database configuration to:

       ```go
       db, err := drv.NewDatabase(map[string]string{
           "driver": "flightsql",
           "uri":    "grpc+tls://data.dremio.cloud:443", // for US region
           //"uri":  "grpc+tls://data.eu.dremio.cloud:443", // for Europe region
           "adbc.flight.sql.authorization_header": "Bearer " + token,
       })
       ```

   - If you changed `uri` to point to a different Flight SQL server, also change the SQL SELECT statement in `stmt.SetSqlQuery()`

1. Run the Go program:

   ```sh
   go mod tidy
   go run main.go
   ```

   The output will look something like this:

   ```
   record:
      schema:
      fields: 1
         - EXPR$0: type=float64, nullable
            metadata: ["ARROW:FLIGHT:SQL:IS_AUTO_INCREMENT": "0", "ARROW:FLIGHT:SQL:IS_CASE_SENSITIVE": "0", "ARROW:FLIGHT:SQL:SCHEMA_NAME": "", "ARROW:FLIGHT:SQL:TABLE_NAME": "", "ARROW:FLIGHT:SQL:IS_SEARCHABLE": "1", "ARROW:FLIGHT:SQL:IS_READ_ONLY": "1", "ARROW:FLIGHT:SQL:TYPE_NAME": "DOUBLE"]
      rows: 1
      col[0][EXPR$0]: [1.4362464230987455]
   ```
