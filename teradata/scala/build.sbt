// Copyright 2026 Columnar Technologies Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

name := "adbc-quickstart-teradata"
version := "1.0-SNAPSHOT"
scalaVersion := "3.3.7"

val arrowVersion = "18.3.0"
val adbcVersion = "0.21.0"

libraryDependencies ++= Seq(
  "org.apache.arrow" % "arrow-c-data" % arrowVersion,
  "org.apache.arrow" % "arrow-memory-core" % arrowVersion,
  "org.apache.arrow" % "arrow-memory-netty" % arrowVersion,
  "org.apache.arrow" % "arrow-vector" % arrowVersion,
  "org.apache.arrow.adbc" % "adbc-core" % adbcVersion,
  "org.apache.arrow.adbc" % "adbc-driver-manager" % adbcVersion,
  "org.apache.arrow.adbc" % "adbc-driver-jni" % adbcVersion,
  "org.slf4j" % "slf4j-nop" % "2.0.16"
)

Compile / mainClass := Some("main")

// Arrow needs access to java.nio internals, plus a few flags that only exist on
// newer JDKs to silence warnings about native access and sun.misc.Unsafe.
val jdkVersion = System.getProperty("java.specification.version").toInt

run / fork := true
run / connectInput := true
run / javaOptions ++= Seq("--add-opens=java.base/java.nio=ALL-UNNAMED") ++
  (if (jdkVersion >= 22) Seq("--enable-native-access=ALL-UNNAMED") else Nil) ++
  (if (jdkVersion >= 23) Seq("--sun-misc-unsafe-memory-access=allow") else Nil)
