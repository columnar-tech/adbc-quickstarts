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

# Connecting R and Firebolt with ADBC

## Instructions

> [!TIP]
> If you already have a Firebolt Core instance running, skip the steps to set up Firebolt.

### Prerequisites

1. [Install R](https://www.r-project.org/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. Install R packages `adbcdrivermanager`, `arrow`, and `tibble`:

   ```r
   install.packages(c("adbcdrivermanager", "arrow", "tibble"))
   ```

### Set up Firebolt

1. [Install Docker](https://docs.docker.com/get-started/get-docker/)

1. Start a Firebolt Core instance:

   ```sh
   docker run -d --rm --name firebolt -p 127.0.0.1:3473:3473 ghcr.io/firebolt-db/engine:5.0.0-pre.0.20260927210425.e91cd5bd17f8
   ```

1. Wait for Firebolt to accept SQL queries:

   ```sh
   until curl --fail --silent --output /dev/null \
     --data 'SELECT 1' \
     http://localhost:3473; do sleep 2; done
   ```

### Connect to Firebolt

1. Install the Firebolt ADBC driver:

   ```sh
   dbc install firebolt
   ```

1. Customize the R script `main.R` as needed
   - Change the connection arguments in `adbc_database_init()`
     - Format `uri` according to the [driver documentation](https://docs.adbc-drivers.org/drivers/firebolt/index.html#connecting), or keep it as is

1. Run the R script:

   ```sh
   Rscript main.R
   ```

### Clean up

1. Stop the Docker container running Firebolt:

   ```sh
   docker stop firebolt
   ```
