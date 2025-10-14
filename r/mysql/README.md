# Connecting R and MySQL with ADBC

## Instructions

> [!TIP]
> If you already have a MySQL instance running, skip the steps to install MySQL, start it, load data, and stop it.

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install MySQL](https://dev.mysql.com/downloads/installer/)
   - On macOS, if you have Homebrew installed, run `brew install mysql`

1. Install R packages `adbcdrivermanager` and `arrow`:

   ```r
   install.packages(c("adbcdrivermanager", "arrow"))
   ```

### Set up MySQL

1. Start MySQL
   - If you installed it with Homebrew, run `brew services start mysql`

1. Create a table in MySQL and load data into it by running `mysql -u root < games.sql`

### Connect to MySQL

1. Install the MySQL ADBC driver:

   ```sh
   dbc install mysql
   ```

1. Customize the R script `main.R` as needed
   - Change the connection arguments in `adbc_database_init()`
     - Format `uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#section-readme), or keep it as is to use the data included with this example
   - If you changed which database you're connecting to, also change the SQL SELECT statement in `read_adbc()`

1. Run the R script:

   ```sh
   Rscript main.R
   ```

### Clean up

1. Stop MySQL
   - If you installed it with Homebrew, run `brew services stop mysql`
