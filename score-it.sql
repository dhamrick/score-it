CREATE DATABASE score_it

CREATE TABLE players
    -- Creates a table called players to hold the player's name and
    -- whether or not they are currently active.
    (
        player_id serial PRIMARY KEY,
        name text,
        email text,
        active text DEFAULT 'yes',
        UNIQUE (email)
    );



