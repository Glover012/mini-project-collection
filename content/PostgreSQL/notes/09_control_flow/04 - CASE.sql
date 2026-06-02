-- CASE can categorize data based on conditions.
CREATE OR REPLACE FUNCTION get_car_type()
RETURNS TABLE(
	car_id INT, 
	car_brand_model TEXT, 
	car_top_speed NUMERIC,
	car_type TEXT) AS
$$
BEGIN
	RETURN QUERY
	SELECT 
		id, 
		CONCAT(brand, ' ', model),
		top_speed,
	CASE
		WHEN top_speed > 250 THEN 'Sport car'
		WHEN top_speed > 180 THEN 'Fast car'
		WHEN top_speed > 0 THEN 'Regular car'
		ELSE 'Unknown car' -- Default value
	END
	FROM cars;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_car_type();
