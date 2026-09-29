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

import { AdbcDatabase } from '@apache-arrow/adbc-driver-manager';

const db = new AdbcDatabase({
  driver: 'postgresql',
  databaseOptions: {
    uri: 'postgresql://username:password@localhost:26257/db?sslmode=require',
  },
});

let conn, stmt;
try {
  conn = await db.connect();
  stmt = await conn.createStatement();
  // CockroachDB does not support the COPY protocol used by the PostgreSQL ADBC driver
  stmt.setOption('adbc.postgresql.use_copy', 'false');
  await stmt.setSqlQuery('SELECT version()');
  const reader = await stmt.executeQuery();
  for await (const batch of reader) {
    console.log(batch.toArray());
  }
} finally {
  await stmt?.close();
  await conn?.close();
  await db.close();
}
