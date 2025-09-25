# Connecting Python and MySQL with ADBC

## Instructions

> [!TIP]
> If you already have a MySQL instance running, skip the steps to install MySQL, start it, load data, and stop it.

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install MySQL](https://dev.mysql.com/downloads/installer/)
   - On macOS, if you have Homebrew installed, run `brew install mysql`

### Set up MySQL

1. Start MySQL
   - If you installed it with Homebrew, run `brew services start mysql`

1. Create a table in MySQL and load data into it by running `mysql -u root < games.sql`

### Connect to MySQL

1. Install the MySQL ADBC driver:

   ```sh
   dbc install mysql
   ```

1. Customize the Python script `main.py` as needed
   - Change the connection arguments in `db_kwargs`
     - Format `uri` according to the [DSN (Data Source Name) format used by Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql#section-readme), or keep it as is to use the data included with this example
   - If you changed which database you're connecting to, also change the SQL SELECT statement in `cursor.execute()`

1. Run the Python script:

   ```sh
   uv run main.py
   ```

### Clean up

1. Stop MySQL
   - If you installed it with Homebrew, run `brew services stop mysql`
