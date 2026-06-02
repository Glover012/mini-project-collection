-- FETCH is an alternative way to limit the number of returned rows.
-- OFFSET skips rows before FETCH returns the requested number of rows.
SELECT * FROM cars ORDER BY id DESC OFFSET 1 FETCH FIRST 3 ROW ONLY;
