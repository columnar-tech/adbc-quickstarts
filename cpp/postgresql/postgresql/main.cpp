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

// For EXIT_SUCCESS
#include <cstdlib>
// For strerror
#include <cstring>
#include <iostream>

#include <arrow-adbc/adbc.h>
#include <arrow-adbc/adbc_driver_manager.h>
#include <arrow/c/bridge.h>
#include <arrow/record_batch.h>

// Error-checking helper for ADBC calls.
// Assumes that there is an AdbcError named `error` in scope.
#define CHECK_ADBC(EXPR)                                                       \
  if (AdbcStatusCode status = (EXPR); status != ADBC_STATUS_OK) {              \
    if (error.message != nullptr) {                                            \
      std::cerr << error.message << std::endl;                                 \
    }                                                                          \
    return EXIT_FAILURE;                                                       \
  }

// Error-checking helper for ArrowArrayStream.
#define CHECK_STREAM(STREAM, EXPR)                                             \
  if (int status = (EXPR); status != 0) {                                      \
    std::cerr << "(" << std::strerror(status) << "): ";                        \
    const char *message = (STREAM).get_last_error(&(STREAM));                  \
    if (message != nullptr) {                                                  \
      std::cerr << message << std::endl;                                       \
    } else {                                                                   \
      std::cerr << "(no error message)" << std::endl;                          \
    }                                                                          \
    return EXIT_FAILURE;                                                       \
  }

int main() {
  AdbcError error = {};

  AdbcDatabase database = {};
  CHECK_ADBC(AdbcDatabaseNew(&database, &error));

  CHECK_ADBC(AdbcDatabaseSetOption(&database, "driver", "postgresql", &error));
  CHECK_ADBC(AdbcDatabaseSetOption(&database, "uri",
                                   "postgresql://postgres:mysecretpassword@localhost:5432/demo", &error));
  CHECK_ADBC(AdbcDriverManagerDatabaseSetLoadFlags(
      &database, ADBC_LOAD_FLAG_DEFAULT, &error));
  CHECK_ADBC(AdbcDatabaseInit(&database, &error));

  AdbcConnection connection = {};
  CHECK_ADBC(AdbcConnectionNew(&connection, &error));
  CHECK_ADBC(AdbcConnectionInit(&connection, &database, &error));

  AdbcStatement statement = {};
  CHECK_ADBC(AdbcStatementNew(&connection, &statement, &error));

  struct ArrowArrayStream stream = {};
  int64_t rows_affected = -1;

  CHECK_ADBC(
      AdbcStatementSetSqlQuery(&statement, "SELECT * FROM games;", &error));
  CHECK_ADBC(
      AdbcStatementExecuteQuery(&statement, &stream, &rows_affected, &error));

  // Import stream as record batch reader
  auto maybe_reader = arrow::ImportRecordBatchReader(&stream);
  if (!maybe_reader.ok()) {
    std::cerr << "Failed to import record batch reader: "
              << maybe_reader.status().message() << std::endl;
    return 1;
  }

  auto reader = maybe_reader.ValueOrDie();

  while (true) {
    auto maybe_batch = reader->Next();
    if (!maybe_batch.ok()) {
      std::cerr << "Error reading batch: " << maybe_batch.status().message()
                << std::endl;
      return 1;
    }

    auto batch = maybe_batch.ValueOrDie();
    if (!batch) {
      break;
    }

    std::cout << batch->ToString() << std::endl;
  }

  CHECK_ADBC(AdbcStatementRelease(&statement, &error));
  CHECK_ADBC(AdbcConnectionRelease(&connection, &error));
  CHECK_ADBC(AdbcDatabaseRelease(&database, &error));

  return EXIT_SUCCESS;
}
