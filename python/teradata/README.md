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

# Connecting Python and Teradata with ADBC

## Instructions

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Connect to Teradata

1. Install the Teradata ADBC driver:

    ```sh
    dbc install teradata
    ```

    Note: This driver is available from Columnar’s private driver registry. Before installing it, create an account at https://cloud.columnar.tech and click to activate a 14-day free trial. Then authenticate to the registry: `dbc auth login`.

2. Download and install the Teradata Tools and Utilities (TTU) from https://downloads.teradata.com/. Select "Tools and Utilities" and choose the package for your platform. Install to the default location:
    - Linux: `/opt/teradata`
    - macOS: `/Library/Application Support/teradata`

3. Set `LD_LIBRARY_PATH` (Linux) or `DYLD_LIBRARY_PATH` (macOS) to make sure the TTU libraries are discoverable by your application.

4. Customize the Python script `main.py`:
    - Change the connection arguments in `db_kwargs`.
        - `uri` is the URI of your Teradata instance. The format is `host/username,password`.
    - Change the SQL SELECT statement in `cursor.execute()`.

5. Run the Python script:

    ```sh
    uv run main.py
    ```
