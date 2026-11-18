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
	var drv drivermgr.Driver

	db, err := drv.NewDatabase(map[string]string{
		"driver": "postgresql",
		"uri":    "postgresql://crate@localhost:5432/crate",
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

	err = stmt.SetOption("adbc.postgresql.use_copy", "false")
	if err != nil {
		log.Fatal(err)
	}

	err = stmt.SetSqlQuery("SELECT version()")
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
