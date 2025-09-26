// Copyright 2025 Columnar Technologies Inc.
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
		"driver": "snowflake",
		"username": "USER",

		// for username/password authentication:
		"adbc.snowflake.sql.auth_type": "auth_snowflake",
		"password": "PASS",

		// for JWT authentication:
		// "adbc.snowflake.sql.auth_type": "auth_jwt",
		// "adbc.snowflake.sql.client_option.jwt_private_key": "/path/to/rsa_key.p8",

		"adbc.snowflake.sql.account": "ACCOUNT-IDENT",
		"adbc.snowflake.sql.db": "SNOWFLAKE_SAMPLE_DATA",
		"adbc.snowflake.sql.schema": "TPCH_SF1",
		"adbc.snowflake.sql.warehouse": "MY_WAREHOUSE",
		"adbc.snowflake.sql.role": "MY_ROLE",
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

	err = stmt.SetSqlQuery("SELECT * FROM CUSTOMER LIMIT 5")
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
