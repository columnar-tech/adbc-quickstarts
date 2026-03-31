# Connecting Rust and Porter with ADBC

This guide shows how to connect Rust to [Porter](https://github.com/TFMV/porter), a lightweight streaming SQL engine built on DuckDB with Arrow Flight SQL support.

Porter is intentionally minimal:

> SQL in → Arrow out

---

## Quick Start (if Porter is already running)

If you already have a Porter instance running, skip setup and go straight to the Rust client section.

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

## Connect Rust to Porter

### Connection settings

* `uri`: Porter endpoint

  * default: `grpc+tcp://localhost:32010`
* `driver`: must be `flightsql`

Porter does not require authentication.

```rust
let opts = [(OptionDatabase::Uri, "grpc+tcp://localhost:32010".into())];
let db = driver
    .new_database_with_opts(opts)
    .expect("Failed to create database handle");
```

---

## Run the example

```bash
cargo run
```

---

## Expected output

```
+------------+
| answer     |
+------------+
| 42         |
+------------+
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
