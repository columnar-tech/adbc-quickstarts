library(adbcdrivermanager)

drv <- adbc_driver("bigquery")

db <- adbc_database_init(
  drv,
  adbc.bigquery.sql.project_id="my-gcp-project",
  adbc.bigquery.sql.dataset_id="bigquery-public-data"
)

con <- adbc_connection_init(db)

con |>
  read_adbc("
    SELECT word, corpus FROM `bigquery-public-data.samples.shakespeare`
     WHERE word_count = 1 ORDER BY RAND() LIMIT 5;
  ") |>
  tibble::as_tibble()
