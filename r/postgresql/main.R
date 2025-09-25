library(adbcdrivermanager)

drv <- adbc_driver("postgresql")

db <- adbc_database_init(
  drv,
  uri="postgresql://localhost:5432/demo"
)

con <- adbc_connection_init(db)

con |>
  read_adbc("SELECT * FROM games") |>
  tibble::as_tibble()
