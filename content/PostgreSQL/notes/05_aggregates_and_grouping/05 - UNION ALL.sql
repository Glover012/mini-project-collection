-- UNION ALL combines results from multiple SELECT statements and keeps duplicates.
SELECT SUM(top_speed) AS "Total speed" FROM cars
UNION ALL
SELECT MAX(top_speed) AS "Maximum speed" FROM cars
UNION ALL
SELECT AVG(top_speed) AS "Average speed" FROM cars
UNION ALL
SELECT MIN(top_speed) AS "Minimum speed" FROM cars;

-- UNION removes duplicate rows from the combined result.
SELECT brand FROM cars
UNION
SELECT brand FROM cars;
