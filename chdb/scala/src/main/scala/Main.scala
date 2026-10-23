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
  JniDriver.PARAM_DRIVER.set(params, "chdb")

  Using.resource(new RootAllocator()) { allocator =>
    Using.resource(AdbcDriverManager.getInstance().connect(DriverFactory, allocator, params)) { db =>
      Using.resource(db.connect()) { conn =>
        Using.resource(conn.createStatement()) { stmt =>
          stmt.setSqlQuery("SELECT * FROM 'games.parquet';")
          Using.resource(stmt.executeQuery()) { result =>
            val reader = result.getReader()
            while reader.loadNextBatch() do
              println(reader.getVectorSchemaRoot().contentToTSVString())
          }
        }
      }
    }
  }
