# Connecting R and DuckDB with ADBC

## Instructions

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. Install R package `adbcdrivermanager`:

   ```sh
   install.packages("adbcdrivermanager")
   ```

### Connect to DuckDB

1. Install the DuckDB ADBC driver:

   ```sh
   dbc install duckdb
   ```

1. Customize the R script `main.R` as needed
   - Change the connection arguments in `adbc_database_init()`
     - Set `path` to the location of the DuckDB database file you want to query, or keep it set to `games.duckdb` to use the database file included with this example
   - If you changed the database file, also change the SQL SELECT statement in `read_adbc()`

1. Run the R script:

   ```sh
   Rscript main.R
   ```
