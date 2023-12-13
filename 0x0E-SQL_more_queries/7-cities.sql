-- Create databasee hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table statess
-- id INT uniquee, auto generatedd, can't be null and is a primary keyy
-- name VARCHARR(256) can't be null
-- If table exists, script should not failff
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
