-- RETURNS TABLE defines the columns returned by a function.
CREATE OR REPLACE FUNCTION get_speed_stats2()
RETURNS TABLE(min_top_speed NUMERIC, max_top_speed NUMERIC, avg_top_speed NUMERIC) AS $$
BEGIN
	RETURN QUERY
	SELECT MIN(top_speed), MAX(top_speed), AVG(top_speed) FROM cars;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_speed_stats2();
