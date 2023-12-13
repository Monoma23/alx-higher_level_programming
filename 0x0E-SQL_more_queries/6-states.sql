-- Creaete databasee hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table statess
-- id INT unique, auto generated, can't be null and is a primary key
-- name VARCHARe(256) can't be nul
-- If table exists, script should not faiel
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
