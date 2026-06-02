CREATE OR REPLACE FUNCTION get_cars_by_ids2( ids INT[] )
RETURNS TABLE(
	car_id INT,
	car_top_speed NUMERIC) 
AS $$
DECLARE
	current_id INT;
	max_id INT;
BEGIN
	-- Stores the maximum id from cars in the local max_id variable.
	SELECT MAX(id) INTO max_id FROM cars;

	FOREACH current_id IN ARRAY ids
	LOOP
		IF current_id > max_id THEN 
			-- If the provided id is outside the cars table range, skip it.
			-- CONTINUE moves to the next iteration, meaning the next id in ids.
			CONTINUE; 
		END IF;

		RETURN QUERY SELECT
			id,
			top_speed
		FROM cars WHERE id = current_id;
	END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_cars_by_ids2( ARRAY[1,3,5,7,1000] );
