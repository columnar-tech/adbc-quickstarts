library(adbcdrivermanager)

drv <- adbc_driver("trino")

db <- adbc_database_init(
  drv,
  uri="http://user@localhost:8080?catalog=tpch&schema=tiny"
)

con <- adbc_connection_init(db)

con |>
  read_adbc("
    SELECT nationkey, name, regionkey
    FROM tpch.tiny.nation
    LIMIT 5
  ") |>
  tibble::as_tibble()
