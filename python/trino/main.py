# /// script
# requires-python = ">=3.9"
# dependencies = ["adbc-driver-manager>=1.8.0", "pyarrow>=20.0.0"]
# ///

from adbc_driver_manager import dbapi

with dbapi.connect(
    driver="trino",
    db_kwargs={
        "uri": "http://user@localhost:8080?catalog=tcph&schema=tiny"
    }
) as con, con.cursor() as cursor:
    cursor.execute("""
      SELECT nationkey, name, regionkey
      FROM tpch.tiny.nation
      LIMIT 5
    """)
    table = cursor.fetch_arrow_table()

print(table)
