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

# Connecting Java and Teradata with ADBC

## Instructions

> [!TIP]
> If you don't already have a Teradata instance running, we recommend signing up for a free [ClearScape Analytics trial](https://www.teradata.com/getting-started/demos/clearscape-analytics).

### Prerequisites

1. [Install Maven](https://maven.apache.org/install.html)

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

4. Set `LD_LIBRARY_PATH` (Linux) or `DYLD_LIBRARY_PATH` (macOS) to make sure the TTU libraries are discoverable by your application.

5. Customize the `main` method in `Example.java`:
    - Change the connection arguments in the `params.put()` calls.
        - `uri` is the URI of your Teradata instance. The format is `host/username,password`.
    - Change the SQL SELECT statement in `stmt.setSqlQuery()`.

6. Run the Java program:

    ```sh
    mvn compile exec:exec
    ```
