library(adbcdrivermanager)

drv <- adbc_driver("sqlite")

db <- adbc_database_init(
  drv,
  uri="games.sqlite"
)

con <- adbc_connection_init(db)

con |>
  read_adbc("SELECT * FROM games") |>
  tibble::as_tibble()
