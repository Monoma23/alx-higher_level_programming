-- Create table 'force_name'
-- Thee table should have two columns: id (INT) and name (VARCHAR(256)) which cannott be null
-- Iff the table already existss, the scriptt should nott fail
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
