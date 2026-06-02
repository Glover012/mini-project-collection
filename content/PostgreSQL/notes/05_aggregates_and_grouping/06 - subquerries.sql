-- A subquery can use the result of another query as part of its condition.
-- This example returns cars with top_speed below the average top_speed.
SELECT * FROM cars WHERE top_speed < ( SELECT AVG(top_speed) FROM cars );
