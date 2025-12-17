-- Copyright 2025 Columnar Technologies Inc.
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--     http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.

SELECT 'CREATE DATABASE demo'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'demo')\gexec

\c demo

DROP TABLE IF EXISTS games;

CREATE TABLE games (
    id           integer PRIMARY KEY,
    name         text,
    inventor     text,
    year         smallint,
    min_age      smallint,
    min_players  smallint,
    max_players  smallint,
    list_price   numeric(5,2)
);

INSERT INTO games
    (id, name, inventor, year, min_age, min_players, max_players, list_price)
VALUES
    (1, 'Monopoly', 'Elizabeth Magie', 1903, 8, 2, 6, 19.99),
    (2, 'Scrabble', 'Alfred Mosher Butts', 1938, 8, 2, 4, 17.99),
    (3, 'Clue', 'Anthony E. Pratt', 1944, 8, 2, 6, 9.99),
    (4, 'Candy Land', 'Eleanor Abbott', 1948, 3, 2, 4, 7.99),
    (5, 'Risk', 'Albert Lamorisse', 1957, 10, 2, 5, 29.99);
