-- listss numbesr of records wsith the same score in the table second_tsable
-- list sorted by numbers of records descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
