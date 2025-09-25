# /// script
# requires-python = ">=3.9"
# dependencies = ["adbc-driver-manager>=1.8.0", "pyarrow>=20.0.0"]
# ///

from adbc_driver_manager import dbapi

with dbapi.connect(
    driver="flightsql",
    db_kwargs={
        "uri": "grpc+tcp://localhost:32010",
        "username": "admin",
        "password": "password1",
    }
) as con, con.cursor() as cursor:
    cursor.execute("""
      SELECT AVG(tip_amount)
      FROM Samples."samples.dremio.com"."NYC-taxi-trips-iceberg"
    """)
    table = cursor.fetch_arrow_table()

print(table)
