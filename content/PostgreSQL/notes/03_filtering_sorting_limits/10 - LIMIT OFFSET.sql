-- OFFSET skips a specified number of rows before returning results.
-- Combined with LIMIT, it can be used to page through grouped query results.
SELECT * FROM cars ORDER BY id ASC LIMIT 2 OFFSET 0;
