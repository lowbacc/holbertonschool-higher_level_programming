-- Use a subquery to get the id of the state with the name 'California' and then select all the cities of that state ordered by id in ascending order.
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
ORDER BY id ASC;