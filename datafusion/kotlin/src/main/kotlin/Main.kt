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
    JniDriver.PARAM_DRIVER.set(params, "datafusion")

    RootAllocator().use { allocator ->
        AdbcDriverManager.getInstance().connect(DRIVER_FACTORY, allocator, params).use { db ->
            db.connect().use { conn ->
                conn.createStatement().use { stmt ->
                    stmt.setSqlQuery("SELECT * FROM 'games.parquet';")
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
