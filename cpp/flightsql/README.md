<!--
Copyright 2025 Columnar Technologies Inc.

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

# Connecting C++ and Arrow Flight SQL with ADBC

This directory contains examples showing how to use ADBC to connect C++ applications to systems that support [Arrow Flight SQL](https://arrow.apache.org/docs/format/FlightSql.html).

## Source systems covered

Any open source tool or vendor product that implements Arrow Flight SQL should work with the ADBC driver for Flight SQL. The examples included here focus on two specific systems:
- Dremio
- GizmoSQL

Other systems that support Arrow Flight SQL include Apache Doris, Deephaven, Spice, and StarRocks. Examples for these are not yet included here. PRs are welcome if you'd like to contribute.

 ## Instructions

Each subdirectory contains its own README with specific instructions.
