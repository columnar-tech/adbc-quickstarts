library(adbcdrivermanager)

drv <- adbc_driver("duckdb")

db <- adbc_database_init(
  drv,
  path="games.duckdb"
)

con <- adbc_connection_init(db)

con |>
  read_adbc("SELECT * FROM games") |>
  tibble::as_tibble()
