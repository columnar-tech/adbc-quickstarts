# Connecting Rust and BigQuery with ADBC

## Instructions

### Prerequisites

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install Google Cloud CLI](https://cloud.google.com/sdk/docs/install)

1. [Create a Google account](https://accounts.google.com) or be able to log in to an existing one

### Set up BigQuery

1. Log into the [Google Cloud Console](https://console.cloud.google.com/) and create project or locate an existing project and record the project ID for use in a later step

1. Run this command in your terminal to log in with the Google Cloud CLI:

   ```console
   $ gcloud auth application-default login
   ```

### Connect to BigQuery

1. Install the BigQuery ADBC driver:

   ```sh
   dbc install bigquery
   ```

1. Customize `src/main.rs` as needed
   - Change the database arguments in `opts`
     - Change the value of the `adbc.bigquery.sql.project_id` argument to match the project ID you recorded in the earlier step
     - Change the value of `adbc.bigquery.sql.dataset_id`, or keep it to use the public Shakespeare dataset
   - If you changed the dataset, also change the SQL SELECT statement in `statement.set_sql_query()`

1. Run the Rust program:

   ```sh
   cargo run
   ```
