-- OUT parameters can return values from a function.
CREATE OR REPLACE FUNCTION get_speed_stats(
OUT min_top_speed NUMERIC, OUT max_top_speed NUMERIC, OUT avg_top_speed NUMERIC) AS $$
BEGIN
	SELECT INTO min_top_speed, max_top_speed, avg_top_speed
	MIN(top_speed), MAX(top_speed), AVG(top_speed) FROM cars;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_speed_stats();
