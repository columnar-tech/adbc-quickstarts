<!--
Copyright 2025 Columnar Technologies Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Connecting Python and BigQuery with ADBC

## Instructions

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. [Install Google Cloud CLI](https://cloud.google.com/sdk/docs/install)

1. [Create a Google account](https://accounts.google.com) or be able to log in to an existing one

### Set up BigQuery

1. Log into the [Google Cloud Console](https://console.cloud.google.com/) and create project or locate an existing project and record the project ID for use in a later step

1. Run this command in your terminal to log in with the Google Cloud CLI:

   ```sh
   gcloud auth application-default login
   ```

### Connect to BigQuery

1. Install the BigQuery ADBC driver:

   ```sh
   dbc install bigquery
   ```

1. Customize the Python script `main.py` as needed
   - Change the connection arguments in `db_kwargs`
     - Change the value of the `adbc.bigquery.sql.project_id` argument to match the project ID you recorded in the earlier step
     - Change the value of `adbc.bigquery.sql.dataset_id`, or keep it to use the public Shakespeare dataset
   - If you changed the dataset, also change the SQL SELECT statement in `cursor.execute()`

1. Run the Python script:

   ```sh
   uv run main.py
   ```
