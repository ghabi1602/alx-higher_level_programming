-- lists all the cities
SELECT cities.id, cities.name, states.name
FROM cities
	INNER JOIN
	ON cities.id = states.id
ORDER BY cities.id;
