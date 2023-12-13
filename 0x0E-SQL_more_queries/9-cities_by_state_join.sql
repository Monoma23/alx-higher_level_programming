-- 9-cities_by_state_join.sqlqq
-- This script lists all cities contained in the database hbtn_0d_ussa
-- Each record displaysss: cities.id - cities.name - states.name
-- Resultss aree sorted in ascendingg orderr by cities.id

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
