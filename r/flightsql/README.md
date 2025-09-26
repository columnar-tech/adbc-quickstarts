# Connecting R and Arrow Flight SQL with ADBC

## Instructions

This example uses [Dremio](https://www.dremio.com/), but other open source tools and vendor products that support Arrow Flight SQL will also work with this driver.

> [!TIP]
> If you already have a Dremio instance running, skip the steps to set up Dremio.

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. Install R package `adbcdrivermanager`:

   ```sh
   install.packages("adbcdrivermanager")
   ```

### Set up Dremio

1. [Sign up for Dremio Cloud](https://www.dremio.com/) or follow the instructions to [set up Dremio Community](https://docs.dremio.com/current/get-started/docker/).

### Connect to Dremio

1. Install the Flight SQL ADBC driver:

   ```sh
   dbc install flightsql
   ```

1. Customize the R script `main.R` as needed
   - Change the connection arguments in `adbc_database_init()`
     - `uri` is the URI of your Dremio instance. The host and port will depend on your installation (the default port is 32010). The protocol scheme should be `grpc` or `grpc+tcp` if your Dremio instance is not using TLS (e.g. if you are using Dremio Community) and should be `grpc+tls` otherwise (e.g. when using Dremio Cloud).
     - `username` and `password` are the username and password of your Dremio account. (If you are using Dremio Community, these were set during the installation instructions.)
     - For Dremio Cloud, remove `username` and `password`, create a personal access token (PAT), store it in a string variable `token` in the script, and set the database initialization to:

       ```r
       db <- adbc_database_init(
         drv,
         uri="grpc+tls://data.dremio.cloud:443", # for US region
         #uri="grpc+tls://data.eu.dremio.cloud:443", # for Europe region
         adbc.flight.sql.authorization_header=paste("Bearer", token)
       )
       ```
   - If you changed `uri` to point to a different Flight SQL server, also change the SQL SELECT statement in `read_adbc()`

1. Run the R script:

   ```sh
   Rscript main.R
   ```

   The output will look something like this:

   ```
   # A tibble: 1 × 1
     EXPR$0
      <dbl>
   1   1.44
   ```
