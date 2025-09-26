# Connecting Rust and SQLite with ADBC

## Instructions

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install SQLite](https://www.sqlite.org/download.html)
   - On macOS, if you have Homebrew installed, run `brew install sqlite`

### Connect to SQLite

1. Install the SQLite ADBC driver:

   ```sh
   dbc install sqlite
   ```

1. Customize `src/main.rs` as needed
   - Change the database arguments in `opts`
     - Replace "games.sqlite" to the location of the SQLite database file you want to query, or keep it set to `games.sqlite` to use the database file included with this example
   - If you changed the database file, also change the SQL SELECT statement in `statement.set_sql_query()`

1. Run the Rust program:

   ```sh
   cargo run
   ```
