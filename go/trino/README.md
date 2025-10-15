# Connecting Go and Trino with ADBC

## Instructions

> [!TIP]
> If you already have a Trino instance running, skip the steps to run Trino in a Docker container.

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

### Set up Trino

1. Start Trino in a Docker container:

   ```sh
   docker pull trinodb/trino

   docker run -d --name trino -p 8080:8080 trinodb/trino
   ```

### Connect to Trino

1. Install the Trino ADBC driver:

   ```sh
   dbc install trino
   ```

1. Customize the Go program `main.go` as needed
   - Change the connection arguments in the `NewDatabase()` call
     - Format `uri` according to the [DSN (Data Source Name) format used by the Trino Go client](https://pkg.go.dev/github.com/trinodb/trino-go-client#section-readme), or keep it as is to use the TPC-H data included in the Trino Docker container image
   - If you changed which Trino instance you're connecting to, also change the SQL SELECT statement in `stmt.SetSqlQuery()`

1. Run the Go program:

   ```sh
   go mod tidy
   go run main.go
   ```

### Clean up

1. Stop the Docker container running Trino:

   ```sh
   docker stop trino
   docker rm trino
   ```
