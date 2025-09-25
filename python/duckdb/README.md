# Connecting Python and DuckDB with ADBC

## Instructions

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Connect to DuckDB

1. Install the DuckDB ADBC driver:

   ```sh
   dbc install duckdb
   ```

1. Customize the Python script `main.py` as needed
   - Change the connection arguments in `db_kwargs`
     - Set `path` to the location of the DuckDB database file you want to query, or keep it set to `games.duckdb` to use the database file included with this example
   - If you changed the database file, also change the SQL SELECT statement in `cursor.execute()`

1. Run the Python script:

   ```sh
   uv run main.py
   ```
