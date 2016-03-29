DROP DATABASE IF EXISTS score_it;

\c score_it

CREATE DATABASE score_it;

CREATE TABLE players
    -- Holds all of the registered players.
    (
        player_id serial PRIMARY KEY,
        user_name text,
        email text,
        address text,
        name text,
        UNIQUE (email, user_name)
    );

CREATE TABLE games
    -- Holds all of the games played and information about them.
    (
        game_id serial PRIMARY KEY,
        game_name text,
        game_type text,
        max_players integer,
        min_players integer,
        difficulty text
     );

CREATE TABLE game_ownership
    -- Holds a record of who owns what games.
    (
        game_id serial REFERENCES games(game_id),
        player_id serial REFERENCES players(player_id)
    );

CREATE TABLE game_nights
    -- Holds all of the game nights, who played, and who hosted
    (
        game_night_id serial PRIMARY KEY,
        play_date timestamp DEFAULT current_timestamp,
        host serial REFERENCES players(player_id)
    );

CREATE TABLE played_games
    -- Records the games played at each game night and the players.
    (
        game_night_id serial REFERENCES game_nights(game_night_id),
        game_id serial REFERENCES games(game_id),
        player_id serial REFERENCES game_nights(player_id)
    );


-- CREATE VIEW current_tournament AS
--     SELECT max(tournament_id) FROM tournaments;
--     -- Creates a view for the current (latest) tournament_id

-- CREATE VIEW last_registered_player AS
--     SELECT max(player_id) FROM players;

-- CREATE VIEW player_standings AS
--     SELECT players.player_id, players.name, tournament_data.wins, tournament_data.matches
--     FROM players JOIN tournament_data
--     ON (players.player_id = tournament_data.player_id);








