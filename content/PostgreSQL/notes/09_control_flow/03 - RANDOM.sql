CREATE OR REPLACE FUNCTION get_random_car_driver()
RETURNS TABLE(driver_id INT, driver_name VARCHAR) AS $$
DECLARE
	driver_ids INT[]; -- Array of driver ids.
	random_driver_id INT;
BEGIN
	-- Creates an array from the query result, containing all ids from drivers.
	-- Stores the array in the local driver_ids variable.
	SELECT ARRAY( SELECT id FROM drivers ) INTO driver_ids;

	-- random() returns a value from 0 up to almost 1.
	-- Random driver id index = random float multiplied by array length, plus 1.
	-- array_length(array, dimension) returns the length of the selected array dimension.
	-- floor() rounds the value down, and ::int casts it to integer.
	random_driver_id := floor(random() * array_length(driver_ids, 1) +1)::int;

	RETURN QUERY SELECT id as driver_id, name as driver_name FROM drivers 
	WHERE id = driver_ids[random_driver_id];
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_random_car_driver();
