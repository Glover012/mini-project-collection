-- CONCAT joins multiple values into a single text value.
CREATE OR REPLACE FUNCTION get_car_complete_name()
RETURNS TABLE( car_id INT, car_brand_model TEXT ) AS $$
BEGIN
	RETURN QUERY SELECT id, CONCAT(brand, ' ', model) FROM cars;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_car_complete_name();
