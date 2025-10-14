# Connecting R and SQLite with ADBC

## Instructions

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install SQLite](https://www.sqlite.org/download.html)
   - On macOS, if you have Homebrew installed, run `brew install sqlite`

1. Install R packages `adbcdrivermanager` and `arrow`:

   ```r
   install.packages(c("adbcdrivermanager", "arrow"))
   ```

### Connect to SQLite

1. Install the SQLite ADBC driver:

   ```sh
   dbc install sqlite
   ```

1. Customize the R script `main.R` as needed
   - Change the connection arguments in `adbc_database_init()`
     - Set `uri` to the location of the SQLite database file you want to query, or keep it set to `games.sqlite` to use the database file included with this example
   - If you changed the database file, also change the SQL SELECT statement in `read_adbc()`

1. Run the R script:

   ```sh
   Rscript main.R
   ```
