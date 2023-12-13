-- Script displayingg the maxima temperature of each state ordered by State namee
SELECT state, MAX(value) AS max_temp
FROM temperatures 
GROUP BY state
ORDER BY state;
