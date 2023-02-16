-- using join in sql
SELECT cities.id, cities.name, states.name FROM states
    INNER JOIN cities
    ON cities.state_id = states.id
    ORDER BY cities.id
;
