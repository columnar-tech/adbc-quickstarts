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

import java.util.HashMap

import org.apache.arrow.adbc.driver.jni.JniDriver
import org.apache.arrow.adbc.drivermanager.AdbcDriverManager
import org.apache.arrow.memory.RootAllocator

import scala.util.Using

private val DriverFactory = "org.apache.arrow.adbc.driver.jni.JniDriverFactory"

@main def main(): Unit =
  val params = new HashMap[String, Object]()
  JniDriver.PARAM_DRIVER.set(params, "snowflake")
  params.put("username", "USER")

  // for username/password authentication:
  params.put("adbc.snowflake.sql.auth_type", "auth_snowflake")
  params.put("password", "PASS")

  // for JWT authentication:
  // params.put("adbc.snowflake.sql.auth_type", "auth_jwt")
  // params.put("adbc.snowflake.sql.client_option.jwt_private_key", "/path/to/rsa_key.p8")

  params.put("adbc.snowflake.sql.account", "ACCOUNT-IDENT")
  params.put("adbc.snowflake.sql.db", "SNOWFLAKE_SAMPLE_DATA")
  params.put("adbc.snowflake.sql.schema", "TPCH_SF1")
  params.put("adbc.snowflake.sql.warehouse", "MY_WAREHOUSE")
  params.put("adbc.snowflake.sql.role", "MY_ROLE")

  Using.resource(new RootAllocator()) { allocator =>
    Using.resource(AdbcDriverManager.getInstance().connect(DriverFactory, allocator, params)) { db =>
      Using.resource(db.connect()) { conn =>
        Using.resource(conn.createStatement()) { stmt =>
          stmt.setSqlQuery("SELECT C_CUSTKEY, C_NAME, C_ADDRESS FROM CUSTOMER LIMIT 5")
          Using.resource(stmt.executeQuery()) { result =>
            val reader = result.getReader()
            while reader.loadNextBatch() do
              println(reader.getVectorSchemaRoot().contentToTSVString())
          }
        }
      }
    }
  }
