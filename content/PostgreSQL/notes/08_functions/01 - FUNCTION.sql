-- CREATE OR REPLACE FUNCTION creates a function or replaces it if it already exists.
CREATE OR REPLACE FUNCTION add_numbers(a INTEGER, b INTEGER) -- a and b are function parameters.
-- The $$ markers define the beginning and end of the function body.
RETURNS INTEGER AS $$ 
BEGIN -- Starts the function body.
	RETURN a + b;
END;
$$ LANGUAGE plpgsql; -- Ends the function definition and sets the PL/pgSQL language.

SELECT add_numbers(2,5);

/* 
If error 25P02 appears, run ROLLBACK.
It clears the failed transaction that blocks the next statements.
*/
