CREATE OR REPLACE FUNCTION get_cars_by_driver(driver_name VARCHAR)
RETURNS TABLE (id INTEGER, brand VARCHAR, model VARCHAR) AS $$
BEGIN
	RETURN QUERY
	SELECT c.id, c.brand, c.model -- Uses alias c and then defines it in the FROM clause.
	FROM cars c
	JOIN drivers d ON c.driver_id = d.id -- Joins another table using aliases and matching keys.
	WHERE d.name = driver_name;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_cars_by_driver('Tom'); -- Returns all cars assigned to Tom.
