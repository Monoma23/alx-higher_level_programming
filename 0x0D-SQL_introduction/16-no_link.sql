-- displaying all records of the second_table of the database
-- result should display the score  and the name, in descending scoree
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
