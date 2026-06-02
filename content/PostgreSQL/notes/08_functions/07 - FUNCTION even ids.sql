-- Loops through cars and returns only rows with even ids.
CREATE OR REPLACE FUNCTION get_even_id_cars()
RETURNS TABLE(
	car_id INT,
	car_brand_model TEXT,
	car_top_speed NUMERIC) AS
$$
DECLARE
	car_record RECORD;
	total_records NUMERIC := 0;
BEGIN
	FOR car_record IN SELECT * FROM cars
	LOOP
		IF MOD(car_record.id, 2) = 0 THEN
			car_id := car_record.id;
			car_brand_model := CONCAT( car_record.brand, ' ', car_record.model );
			car_top_speed := car_record.top_speed;
			RETURN NEXT;
		END IF;
		
	END LOOP;
END;
$$ LANGUAGE plpgsql;
