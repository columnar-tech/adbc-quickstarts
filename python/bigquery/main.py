# /// script
# requires-python = ">=3.9"
# dependencies = ["adbc-driver-manager>=1.8.0", "pyarrow>=20.0.0"]
# ///

from adbc_driver_manager import dbapi

with dbapi.connect(
    driver="bigquery",
    db_kwargs={
        "adbc.bigquery.sql.project_id": "my-gcp-project",
        "adbc.bigquery.sql.dataset_id": "bigquery-public-data"
    }
) as con, con.cursor() as cursor:
    cursor.execute("""
      SELECT word, corpus FROM bigquery-public-data.samples.shakespeare
      WHERE word_count = 1 ORDER BY RAND() LIMIT 5;
    """)
    table = cursor.fetch_arrow_table()

print(table)
