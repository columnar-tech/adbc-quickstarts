# Connecting R and Snowflake with ADBC

## Instructions

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. Install R package `adbcdrivermanager`:

   ```sh
   install.packages("adbcdrivermanager")
   ```

### Connect to Snowflake

1. Install the Snowflake ADBC driver:

   ```sh
   dbc install snowflake
   ```

1. Customize the R script `main.R`
   - Change the connection arguments in `adbc_database_init()`
     - See [Snowflake Driver Client Options](https://arrow.apache.org/adbc/current/driver/snowflake.html#client-options) for the full list of available options
   - If you changed the database and schema, also change the SQL SELECT statement in `read_adbc()`

1. Run the R script:

   ```sh
   Rscript main.R
   ```
