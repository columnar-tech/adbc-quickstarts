# Connecting Go and Porter with ADBC

This guide shows how to connect Go to [Porter](https://github.com/TFMV/porter), a lightweight streaming SQL engine built on DuckDB with Arrow Flight SQL support.

Porter is intentionally minimal:

> SQL in → Arrow out

---

## 💡 Quick Start (if Porter is already running)

If you already have a Porter instance running, skip setup and go straight to the Go client section.

---

## Prerequisites

* Go installed (1.20+ recommended)
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

## Connect Go to Porter

Edit `main.go` in this example directory.

### Connection settings

* `uri`: Porter endpoint

  * default: `grpc+tcp://localhost:32010`
* `driver`: must be `flightsql`

```go
db, err := drv.NewDatabase(map[string]string{
	"driver": "flightsql",
	"uri":    "grpc+tcp://localhost:32010",
})
```

---

## Run the example

```bash
go mod tidy
go run main.go
```

---

## Expected output

Basic rows:

```
RecordBatch ...
RecordBatch ...
```

Schema inspection example:

```
record:
  schema:
  fields: 2
    - id: type=int64, nullable
    - name: type=utf8, nullable
  rows: 2
  col[0][id]: [1 2]
  col[1][name]: ["porter" "flight"]
```

Streaming queries will output multiple batches until completion.

---

## Stop the server

```bash
CTRL + C
```

---

## Notes

Porter is designed to be simple and hackable:

* No heavy orchestration layer
* No external dependencies beyond Arrow + FlightSQL
* Built for experimentation and embedding

### Local development install

```bash
go install ./cmd/porter
```
