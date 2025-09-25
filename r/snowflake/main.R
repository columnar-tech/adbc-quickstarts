library(adbcdrivermanager)

drv <- adbc_driver("snowflake")

db <- adbc_database_init(
  drv,

  ### for username/password authentication: ###
  username="USER",
  password="PASS",

  ### for JWT authentication: ####
  #adbc.snowflake.sql.auth_type="auth_jwt",
  #adbc.snowflake.sql.client_option.jwt_private_key="/path/to/rsa_key.p8",

  adbc.snowflake.sql.account="ACCOUNT-IDENT",
  adbc.snowflake.sql.warehouse="MY_WAREHOUSE",
  adbc.snowflake.sql.role="MY_ROLE"
  adbc.snowflake.sql.db="SNOWFLAKE_SAMPLE_DATA",
  adbc.snowflake.sql.schema="TPCH_SF1",
)

con <- adbc_connection_init(db)

con |>
  read_adbc("SELECT * FROM CUSTOMER LIMIT 5") |>
  tibble::as_tibble()
