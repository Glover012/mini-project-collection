CREATE OR REPLACE FUNCTION multiply_numbers(a INTEGER = 1, b INTEGER = 2) -- Default argument values are defined after =.
RETURNS INTEGER AS $$
DECLARE
-- DECLARE defines local variables used inside the function.
	result INTEGER;
BEGIN
	result := a * b; -- := is the assignment operator
	RETURN result;
END;
$$ LANGUAGE plpgsql;

SELECT multiply_numbers(2,5);
