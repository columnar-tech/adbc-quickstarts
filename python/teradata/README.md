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

> [!TIP]
> If you don't already have a Teradata instance running, we recommend signing up for a free [ClearScape Analytics trial](https://www.teradata.com/getting-started/demos/clearscape-analytics).

### Prerequisites

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

2. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

### Connect to Teradata

1. The ADBC driver for Teradata is available from Columnar's private driver registry. Create a [Columnar Cloud](https://cloud.columnar.tech) account and activate a 14-day free trial. Then authenticate to the registry:

    ```sh
    dbc auth login
    ```

2. Install the ADBC driver for Teradata:

    ```sh
    dbc install teradata
    ```

3. Download and install the [Teradata Tools and Utilities (TTU)](https://downloads.teradata.com/). Select "Tools and Utilities" and choose the package for your platform. Install to the default location:
    - Linux: `/opt/teradata`
    - macOS: `/Library/Application Support/teradata`
    - Windows: `C:\Program Files\Teradata\Client`

    On Windows, you can do this with `winget install Teradata.TTUBase`

    On macOS with Homebrew, you can do this with `brew tap Teradata/teradata && brew install ttubasesuite`

4. Set `LD_LIBRARY_PATH` (Linux), `DYLD_LIBRARY_PATH` (macOS), or `PATH` (Windows) to make sure the TTU libraries are discoverable by your application.

5. Customize the Python script `main.py`:
    - Change the connection arguments in `db_kwargs`.
        - `uri` is the URI of your Teradata instance. The format is `host/username,password`.
    - Change the SQL SELECT statement in `cursor.execute()`.

6. Run the Python script:

    ```sh
    uv run main.py
    ```
