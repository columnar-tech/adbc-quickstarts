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
