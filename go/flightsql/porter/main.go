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

package main

import (
	"context"
	"fmt"
	"log"

	"github.com/apache/arrow-adbc/go/adbc/drivermgr"
)

func main() {
	ctx := context.Background()

	var drv drivermgr.Driver

	// ─────────────────────────────────────────────
	// 1. Open ADBC database
	// ─────────────────────────────────────────────
	db, err := drv.NewDatabase(map[string]string{
		"driver": "flightsql",
		"uri":    "grpc+tcp://localhost:32010",
	})
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// ─────────────────────────────────────────────
	// 2. Open connection
	// ─────────────────────────────────────────────
	conn, err := db.Open(ctx)
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	// ─────────────────────────────────────────────
	// 3. Create statement
	// ─────────────────────────────────────────────
	stmt, err := conn.NewStatement()
	if err != nil {
		log.Fatal(err)
	}
	defer stmt.Close()

	if err := stmt.SetSqlQuery(`SELECT 42 AS answer`); err != nil {
		log.Fatal(err)
	}

	// ─────────────────────────────────────────────
	// 4. Execute
	// ─────────────────────────────────────────────
	stream, _, err := stmt.ExecuteQuery(ctx)
	if err != nil {
		log.Fatal(err)
	}
	defer stream.Release()

	// ─────────────────────────────────────────────
	// 5. Consume Arrow record batches
	// ─────────────────────────────────────────────
	for stream.Next() {
		batch := stream.RecordBatch()
		fmt.Println(batch)
	}

	if err := stream.Err(); err != nil {
		log.Fatal(err)
	}
}
