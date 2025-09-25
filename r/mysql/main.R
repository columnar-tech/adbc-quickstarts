library(adbcdrivermanager)

drv <- adbc_driver("mysql")

db <- adbc_database_init(
  drv,
  uri="root@tcp(localhost:3306)/demo"
)

con <- adbc_connection_init(db)

con |>
  read_adbc("SELECT * FROM games") |>
  tibble::as_tibble()
