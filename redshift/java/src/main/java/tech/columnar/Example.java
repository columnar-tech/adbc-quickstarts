/*
 * Copyright 2026 Columnar Technologies Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package tech.columnar;

import java.util.HashMap;
import java.util.Map;
import org.apache.arrow.adbc.core.AdbcConnection;
import org.apache.arrow.adbc.core.AdbcDatabase;
import org.apache.arrow.adbc.core.AdbcStatement;
import org.apache.arrow.adbc.driver.jni.JniDriver;
import org.apache.arrow.adbc.drivermanager.AdbcDriverManager;
import org.apache.arrow.memory.BufferAllocator;
import org.apache.arrow.memory.RootAllocator;
import org.apache.arrow.vector.ipc.ArrowReader;

public class Example {
  private static final String DRIVER_FACTORY = "org.apache.arrow.adbc.driver.jni.JniDriverFactory";

  public static void main(String[] args) throws Exception {
    Map<String, Object> params = new HashMap<>();
    JniDriver.PARAM_DRIVER.set(params, "redshift");
    params.put("uri", "postgresql://localhost:5439"); // for Redshift Serverless with bastion host
    // params.put("uri", "postgresql://localhost:5440"); // for Redshift Provisioned with bastion
    // host
    // params.put("uri", "postgresql://<cluster hostname>:<cluster port>"); // for direct connection

    params.put("redshift.cluster_type", "redshift-serverless"); // for Redshift Serverless
    // params.put("redshift.cluster_type", "redshift-iam"); // for Redshift Provisioned with IAM
    // auth
    // params.put("redshift.cluster_type", "redshift"); // for Redshift Provisioned with
    // user/password auth

    params.put("redshift.workgroup_name", "<WORKGROUP_NAME>"); // for Redshift Serverless
    // params.put("redshift.cluster_identifier", "<CLUSTER IDENTIFIER>"); // for Redshift
    // Provisioned

    params.put("redshift.db_name", "sample_data_dev");

    try (BufferAllocator allocator = new RootAllocator();
        AdbcDatabase db =
            AdbcDriverManager.getInstance().connect(DRIVER_FACTORY, allocator, params);
        AdbcConnection conn = db.connect();
        AdbcStatement stmt = conn.createStatement()) {
      stmt.setSqlQuery(
          """
            SELECT
              l_partkey,
              SUM(l_quantity) as total_ordered
            FROM tpch.lineitem
            GROUP BY l_partkey
            ORDER BY total_ordered DESC
            LIMIT 5;
          """);
      try (AdbcStatement.QueryResult result = stmt.executeQuery()) {
        ArrowReader reader = result.getReader();
        while (reader.loadNextBatch()) {
          System.out.println(reader.getVectorSchemaRoot().contentToTSVString());
        }
      }
    }
  }
}
