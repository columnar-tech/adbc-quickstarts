library(adbcdrivermanager)

drv <- adbc_driver("mssql")

db <- adbc_database_init(
  drv,
  uri="sqlserver://sa:Co1umn@r@localhost:1433?database=demo"
)

con <- adbc_connection_init(db)

con |>
  read_adbc("SELECT * FROM games") |>
  tibble::as_tibble()
