# Connecting R and Porter with ADBC

This guide shows how to connect R to [Porter](https://github.com/TFMV/porter), a lightweight streaming SQL engine built on DuckDB with Arrow Flight SQL support.

Porter is intentionally minimal:

> SQL in → Arrow out

---

## Quick Start (if Porter is already running)

If you already have a Porter instance running, skip setup and go straight to the R client section.

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

## Connect R to Porter

### Connection settings

* `uri`: Porter endpoint

  * default: `grpc+tcp://localhost:32010`
* `driver`: must be `flightsql`

Porter does not require authentication.

```r
db <- adbc_database_init(
  drv,
  uri = "grpc+tcp://localhost:32010"
)
```

---

## Run the example

```r
Rscript main.R
```

---

## Expected output

```
# A tibble: 1 x 1
  answer
   <int>
1     42
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
