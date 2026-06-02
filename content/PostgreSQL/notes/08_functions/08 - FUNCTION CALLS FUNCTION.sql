-- Calls one function from another function and returns the computed result.
CREATE OR REPLACE FUNCTION substract_numers( a INT, b INT )
RETURNS INT
AS $$
BEGIN
	RETURN a - b;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION compute_num( a INT, b INT)
RETURNS TABLE ( result INT )
AS $$
DECLARE
	num INT;
BEGIN
	num := substract_numers( a, b ) + 10;
	num := num * 2;
	RETURN QUERY SELECT num;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM compute_num( 5,3 );
