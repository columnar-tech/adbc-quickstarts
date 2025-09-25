# Connecting Python and Snowflake with ADBC

## Instructions

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Connect to Snowflake

1. Install the Snowflake ADBC driver:

   ```sh
   dbc install snowflake
   ```

1. Customize the Python script `main.py`
   - Change the connection arguments in `db_kwargs`
     - See [Snowflake Driver Client Options](https://arrow.apache.org/adbc/current/driver/snowflake.html#client-options) for the full list of available options
   - If you changed the database and schema, also change the SQL SELECT statement in `cursor.execute()`

1. Run the Python script:

   ```sh
   uv run main.py
   ```
