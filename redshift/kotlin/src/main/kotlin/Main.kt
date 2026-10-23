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

import org.apache.arrow.adbc.driver.jni.JniDriver
import org.apache.arrow.adbc.drivermanager.AdbcDriverManager
import org.apache.arrow.memory.RootAllocator

private const val DRIVER_FACTORY = "org.apache.arrow.adbc.driver.jni.JniDriverFactory"

fun main() {
    val params = mutableMapOf<String, Any>()
    JniDriver.PARAM_DRIVER.set(params, "redshift")
    params["uri"] = "postgresql://localhost:5439" // for Redshift Serverless with bastion host
    // params["uri"] = "postgresql://localhost:5440" // for Redshift Provisioned with bastion host
    // params["uri"] = "postgresql://<cluster hostname>:<cluster port>" // for direct connection

    params["redshift.cluster_type"] = "redshift-serverless" // for Redshift Serverless
    // params["redshift.cluster_type"] = "redshift-iam" // for Redshift Provisioned with IAM auth
    // params["redshift.cluster_type"] = "redshift" // for Redshift Provisioned with user/password auth

    params["redshift.workgroup_name"] = "<WORKGROUP_NAME>" // for Redshift Serverless
    // params["redshift.cluster_identifier"] = "<CLUSTER IDENTIFIER>" // for Redshift Provisioned

    params["redshift.db_name"] = "sample_data_dev"

    RootAllocator().use { allocator ->
        AdbcDriverManager.getInstance().connect(DRIVER_FACTORY, allocator, params).use { db ->
            db.connect().use { conn ->
                conn.createStatement().use { stmt ->
                    stmt.setSqlQuery(
                        """
                        SELECT
                          l_partkey,
                          SUM(l_quantity) as total_ordered
                        FROM tpch.lineitem
                        GROUP BY l_partkey
                        ORDER BY total_ordered DESC
                        LIMIT 5;
                        """.trimIndent(),
                    )
                    stmt.executeQuery().use { result ->
                        val reader = result.reader
                        while (reader.loadNextBatch()) {
                            println(reader.vectorSchemaRoot.contentToTSVString())
                        }
                    }
                }
            }
        }
    }
}
