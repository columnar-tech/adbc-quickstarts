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
