CREATE OR REPLACE FUNCTION sum_car_prices()
RETURNS NUMERIC AS $$
DECLARE -- Declares local variables.
	car_record RECORD; -- RECORD stores one row returned by a query.
	total_price NUMERIC := 0;
BEGIN
	FOR car_record IN SELECT * FROM cars
	LOOP
		total_price := total_price + car_record.price;
	END LOOP;
	
	RETURN total_price;
END;
$$ LANGUAGE plpgsql;
