CREATE OR REPLACE FUNCTION get_car_speed_type()
RETURNS TABLE(
	car_id INT, 
	car_brand_model TEXT, 
	car_speed_type TEXT) AS
$$
DECLARE -- Declares local variables.
	car_record cars%ROWTYPE; 
	-- Static row type: cars%ROWTYPE depends on the cars table structure.
	-- It returns a row based on that table structure.
	-- Dynamic row type: RECORD depends on the SELECT query.
	-- car_record RECORD would be dynamic and based strictly on the loop query.
BEGIN -- Starts the function.
	FOR car_record IN SELECT * FROM cars -- Loop query.
	LOOP -- Starts the loop.
		car_id := car_record.id;
		car_brand_model := CONCAT(car_record.brand, ' ', car_record.model);

		IF car_record.top_speed BETWEEN 100 and 180 THEN
			car_speed_type := 'Family car';
		ELSEIF car_record.top_speed BETWEEN 180 and 250 THEN
			car_speed_type := 'Sports car';
		ELSEIF car_record.top_speed > 250 THEN
			car_speed_type := 'Super car';
		ELSE
			car_speed_type := 'Unknown car';
		END IF; -- Ends the conditional block.
		-- RETURN NEXT adds the current row to the function result.
		-- Without RETURN NEXT, this RETURNS TABLE function would not emit rows.
		RETURN NEXT; 
		
	END LOOP; -- Ends the loop.
END; -- Ends the function.
$$ LANGUAGE plpgsql;
		

SELECT * FROM get_car_speed_type();
