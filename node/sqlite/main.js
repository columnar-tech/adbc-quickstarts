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

'use strict'

const { AdbcDatabase } = require('adbc-driver-manager')

async function main() {
  const db = new AdbcDatabase({
    driver: 'sqlite',
    databaseOptions: { uri: 'games.sqlite' },
  })

  const conn = await db.connect()

  try {
    const reader = await conn.query('SELECT * FROM games;')

    for await (const batch of reader) {
      for (const row of batch) {
        console.log(row.toJSON())
      }
    }
  } finally {
    await conn.close()
    await db.close()
  }
}

main().catch((err) => {
  console.error(err)
  process.exit(1)
})
