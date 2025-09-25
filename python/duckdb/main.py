# /// script
# requires-python = ">=3.9"
# dependencies = ["adbc-driver-manager>=1.8.0", "pyarrow>=20.0.0"]
# ///

from adbc_driver_manager import dbapi

with dbapi.connect(
    driver="duckdb",
    db_kwargs={
        "path": "games.duckdb"
    }
) as con, con.cursor() as cursor:
    cursor.execute("SELECT * FROM games;")
    table = cursor.fetch_arrow_table()

print(table)
