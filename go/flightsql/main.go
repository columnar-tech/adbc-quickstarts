package main

import (
	"context"
	"fmt"
	"log"

	"github.com/apache/arrow-adbc/go/adbc/drivermgr"
)

func main() {
	var drv drivermgr.Driver

	db, err := drv.NewDatabase(map[string]string{
		"driver":   "flightsql",
		"uri":      "grpc+tcp://localhost:32010",
		"username": "admin",
		"password": "password1",
	})
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	conn, err := db.Open(context.Background())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	stmt, err := conn.NewStatement()
	if err != nil {
		log.Fatal(err)
	}
	defer stmt.Close()

	err = stmt.SetSqlQuery(`
      SELECT AVG(tip_amount)
      FROM Samples."samples.dremio.com"."NYC-taxi-trips-iceberg"
    `)
	if err != nil {
		log.Fatal(err)
	}

	stream, _, err := stmt.ExecuteQuery(context.Background())
	if err != nil {
		log.Fatal(err)
	}
	defer stream.Release()

	// Read all record batches from the stream
	for stream.Next() {
		batch := stream.RecordBatch()
		fmt.Println(batch)
	}

	if err := stream.Err(); err != nil {
		log.Fatal(err)
	}
}
