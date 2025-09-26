# Copyright 2025 Columnar Technologies Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

library(adbcdrivermanager)

drv <- adbc_driver("bigquery")

db <- adbc_database_init(
  drv,
  adbc.bigquery.sql.project_id="my-gcp-project",
  adbc.bigquery.sql.dataset_id="bigquery-public-data"
)

con <- adbc_connection_init(db)

con |>
  read_adbc("
    SELECT word, corpus FROM `bigquery-public-data.samples.shakespeare`
     WHERE word_count = 1 ORDER BY RAND() LIMIT 5;
  ") |>
  tibble::as_tibble()
