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

IF DB_ID(N'demo') IS NULL
    CREATE DATABASE demo;
GO

USE demo;
GO

IF OBJECT_ID(N'dbo.games', N'U') IS NOT NULL
    DROP TABLE dbo.games;

CREATE TABLE dbo.games
(
    id           INT            PRIMARY KEY,
    name         NVARCHAR(100),
    inventor     NVARCHAR(100),
    [year]       SMALLINT,
    min_age      TINYINT,
    min_players  TINYINT,
    max_players  TINYINT,
    list_price   DECIMAL(5,2)
);

INSERT INTO dbo.games (id, name, inventor, [year], min_age, min_players, max_players, list_price) VALUES
(1, N'Monopoly', N'Elizabeth Magie', 1903, 8, 2, 6, 19.99),
(2, N'Scrabble', N'Alfred Mosher Butts', 1938, 8, 2, 4, 17.99),
(3, N'Clue', N'Anthony E. Pratt', 1944, 8, 2, 6, 9.99),
(4, N'Candy Land', N'Eleanor Abbott', 1948, 3, 2, 4, 7.99),
(5, N'Risk', N'Albert Lamorisse', 1957, 10, 2, 5, 29.99);
