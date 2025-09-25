# /// script
# requires-python = ">=3.9"
# dependencies = ["adbc-driver-manager>=1.8.0", "pyarrow>=20.0.0"]
# ///

from adbc_driver_manager import dbapi

with dbapi.connect(
    driver="snowflake",
    db_kwargs={
        "username": "USER",

        ### for username/password authentication: ###
        "adbc.snowflake.sql.auth_type": "auth_snowflake",
        "password": "PASS",

        ### for JWT authentication: ###
        #"adbc.snowflake.sql.auth_type": "auth_jwt",
        #"adbc.snowflake.sql.client_option.jwt_private_key": "/path/to/rsa_key.p8",

        "adbc.snowflake.sql.account": "ACCOUNT-IDENT",
        "adbc.snowflake.sql.db": "SNOWFLAKE_SAMPLE_DATA",
        "adbc.snowflake.sql.schema": "TPCH_SF1",
        "adbc.snowflake.sql.warehouse": "MY_WAREHOUSE",
        "adbc.snowflake.sql.role": "MY_ROLE"
    }
) as con, con.cursor() as cursor:
    cursor.execute("SELECT * FROM CUSTOMER LIMIT 5")
    table = cursor.fetch_arrow_table()

print(table)
