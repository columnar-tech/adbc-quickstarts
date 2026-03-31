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

# Connecting Java and Porter with ADBC

This guide shows how to connect Java to [Porter](https://github.com/TFMV/porter), a lightweight streaming SQL engine built on DuckDB with Arrow Flight SQL support.

Porter is intentionally minimal:

> SQL in → Arrow out

---

## Quick Start (if Porter is already running)

If you already have a Porter instance running, skip setup and go straight to the Java client section.

---

## Prerequisites

* [Install dbc](https://docs.columnar.tech/dbc/getting_started/installation/)
* A running Porter server (optional if you are testing locally)

---

## Install Porter (Go install)

### Recommended (install binary)

```bash
go install github.com/TFMV/porter/cmd/porter@latest
```

Run it:

```bash
porter
```

---

### Alternative (run from source)

```bash
git clone https://github.com/TFMV/porter.git
cd porter
go mod tidy
```

Run server:

```bash
go run ./cmd/server
```

Default endpoint:

```
localhost:32010
```

---

## Install ADBC FlightSQL Driver

```bash
dbc install flightsql
```

---

## Connect Java to Porter

### Connection settings

* `uri`: Porter endpoint

  * default: `grpc+tcp://localhost:32010`
* `driver`: must be `flightsql`

Porter does not require authentication.

```java
Map<String, Object> params = new HashMap<>();
JniDriver.PARAM_DRIVER.set(params, "flightsql");
params.put("uri", "grpc+tcp://localhost:32010");
```

---

## Run the example

```bash
mvn compile exec:exec
```

---

## Expected output

```
answer
42
```

---

## Stop the server

```bash
CTRL + C
```

---

## Notes

Porter is designed to be simple and hackable:

* No heavy orchestration layer
* No external dependencies beyond Arrow + Flight SQL
* Built for experimentation and embedding
