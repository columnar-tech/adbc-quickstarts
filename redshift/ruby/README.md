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

# Connecting Ruby and Amazon Redshift with ADBC

## Instructions

### Prerequisites

1. [Install Ruby](https://www.ruby-lang.org/)

1. [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)

1. Ensure the native Arrow GLib and ADBC GLib libraries required by `red-adbc`
   are installed and discoverable. If `bundle install` reports missing `arrow`,
   `arrow-glib`, or `adbc-glib`, use the platform-specific commands below.

   <details>
   <summary>macOS with Homebrew</summary>

   ```sh
   brew install apache-arrow-glib apache-arrow-adbc-glib
   ```

   </details>

   <details>
   <summary>Debian/Ubuntu</summary>

   ```sh
   sudo apt install libarrow-glib-dev libadbc-glib-dev
   ```

   </details>

   <details>
   <summary>RHEL-compatible distributions</summary>

   ```sh
   sudo dnf install arrow-glib-devel adbc-glib-devel
   ```

   </details>

   <details>
   <summary>Windows with RubyInstaller/MSYS2 UCRT64</summary>

   ```sh
   pacman -S --needed mingw-w64-ucrt-x86_64-arrow mingw-w64-ucrt-x86_64-arrow-adbc-glib
   ```

   If you use a different MSYS2 environment, adjust the package prefix to match
   it; for example, use `mingw-w64-x86_64-*` from the MINGW64 shell.

   </details>

1. Install Ruby dependencies:

   ```sh
   bundle install
   ```

   If you have multiple Ruby installations, ensure `ruby` and `bundle` resolve
   to the same installation before running this command.

1. [Install the AWS CLI](https://aws.amazon.com/cli/)

1. [Create an AWS account](https://aws.amazon.com/) or be able to log in to an existing one

### Set Up Redshift

1. Log into the [AWS Console](https://console.aws.amazon.com/). Record the region name (in the upper-right corner). (If your AWS account uses single sign-on (SSO), the URL to log in to the console may be different, e.g. it may instead be https://(example).awsapps.com/start/.)
1. Create a Redshift cluster or locate an existing one. (For example, Amazon provides a [tutorial to create a new serverless cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console.html).) Record the hostname, port number, database name, workgroup name (for serverless clusters), and cluster identifier (for provisioned clusters).
1. Ensure that the VPC security group that Redshift is running in has an inbound rule that accepts connections from your IP address on the Redshift port.
1. If using a provisioned cluster, make sure the cluster is started and not paused. From the AWS Console, choose the cluster, then "Actions", then "Resume".
1. This example uses the `sample_data_dev` database which is built-in and contains example datasets. If you wish to use the example as-is, then also create the `sample_data_dev` database from the console:

   1. From the AWS console, find your cluster.
   1. Choose "Query Data".
   1. Choose your database in the panel on the left to connect to it.
   1. Expand the database in the panel on the left and expand "native databases", then expand `sample_data_dev`.
   1. Click the folder icon on the `tpch` schema listed, which will have a tooltip labeled "Open sample notebooks". This will ask if you want to create the sample TPC-H data.
   1. Confirm that you want to create the database, then wait for Redshift to populate the data.

1. Configure the AWS CLI:

   ```sh
   aws sso configure         # If you have never logged in before
   export AWS_PROFILE=<...>  # This comes from `sso configure`.
                             # Or use `aws configure list-profiles`
   export AWS_REGION=<...>
   ```

1. Run this command in your terminal to log in with the AWS CLI:

   ```sh
   aws sso login             # This will open the browser
   ```

1. If your cluster is not [publicly accessable](https://repost.aws/knowledge-center/redshift-cluster-private-public), and you are not running from within AWS (e.g. on an EC2 machine with access to Redshift), you will need to create a jump box and an SSH tunnel to access the cluster. See the AWS documentation on [bastion hosts](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect.html).

### Connect to Redshift

1. Install the Redshift ADBC driver:

   ```sh
   dbc install --level user redshift
   ```

1. Customize the Ruby script `main.rb`
   - Change the connection arguments in `database.set_option()`
     - Change the value of `uri` to match the hostname and port you recorded in the earlier step, or your SSH tunnel if necessary
     - Change the value of `redshift.cluster_type` to match your Redshift cluster type
     - Change the value of `redshift.workgroup_name` or `redshift.cluster_identifier` to match the workgroup name or cluster identifier you recorded in the earlier step
     - Change the value of `redshift.db_name` to match the database name you recorded in the earlier step (or leave it as `sample_data_dev` to use the built-in sample database)
   - If you changed the database name, also change the SQL SELECT statement in `connection.query()`

1. Run the Ruby script:

   ```sh
   bundle exec ruby main.rb
   ```
