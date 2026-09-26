-- Copyright 2026 Columnar Technologies Inc.
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

CREATE SCHEMA IF NOT EXISTS DEMO;
OPEN SCHEMA DEMO;

CREATE OR REPLACE TABLE GAMES
(
    ID           INT            PRIMARY KEY,
    NAME         VARCHAR(100),
    INVENTOR     VARCHAR(100),
    "YEAR"         SMALLINT,
    MIN_AGE      TINYINT,
    MIN_PLAYERS  TINYINT,
    MAX_PLAYERS  TINYINT,
    LIST_PRICE   DECIMAL(5,2)
);

INSERT INTO GAMES (ID, NAME, INVENTOR, "YEAR", MIN_AGE, MIN_PLAYERS, MAX_PLAYERS, LIST_PRICE) VALUES
(1, 'Monopoly',   'Elizabeth Magie',     1903, 8, 2, 6, 19.99),
(2, 'Scrabble',   'Alfred Mosher Butts', 1938, 8, 2, 4, 17.99),
(3, 'Clue',       'Anthony E. Pratt',    1944, 8, 2, 6, 9.99),
(4, 'Candy Land', 'Eleanor Abbott',      1948, 3, 2, 4, 7.99),
(5, 'Risk',       'Albert Lamorisse',    1957, 10, 2, 5, 29.99);
