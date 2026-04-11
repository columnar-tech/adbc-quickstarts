<!--
Copyright 2026 Columnar Technologies Inc.

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

# Connecting R and Databricks with ADBC

## Instructions

### Prerequisites

1. [Install R](https://www.r-project.org/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

3. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

    ```r
    install.packages(c("adbcdrivermanager", "arrow", "tibble"))
    ```

4. [Create a Databricks account](https://www.databricks.com/) or be able to log in to an existing one.

### Set up Databricks

1. Log into [Databricks](https://login.databricks.com/) and create or locate an existing SQL warehouse.

2. Open the "Connection details" tab and record the server hostname and HTTP path. See the Databricks documentation describing [how to get these connection details](https://docs.databricks.com/integrations/compute-details).

### Connect to Databricks

1. Install the Databricks ADBC driver:

    ```sh
    dbc install databricks
    ```

2. Customize the R script `main.R`:
    - Change the connection arguments in `adbc_database_init()`:
        - `uri` is the URI for your Databricks instance. The script includes several authentication options. See the [Databricks ADBC driver documentation](https://docs.adbc-drivers.org/drivers/databricks/) for details.
    - Change the SQL SELECT statement in `read_adbc()`, or keep it as is.
        - Specify the catalog and schema by fully qualifying the table name as `catalog.schema.table`.

3. Run the R script:

    ```sh
    Rscript main.R
    ```
