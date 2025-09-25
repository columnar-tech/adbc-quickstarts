library(adbcdrivermanager)

drv <- adbc_driver("flightsql")

db <- adbc_database_init(
  drv,
  uri="grpc+tcp://localhost:32010",
  username="admin",
  password="password1"
)

con <- adbc_connection_init(db)

con |>
  read_adbc("
    SELECT AVG(tip_amount)
    FROM Samples.\"samples.dremio.com\".\"NYC-taxi-trips-iceberg\"
  ") |>
  tibble::as_tibble()
