-- A trigger is a procedure that runs automatically when a database event occurs.
-- Examples include inserting or updating a row.

-- Function executed by the trigger.
CREATE OR REPLACE FUNCTION check_top_speed()
RETURNS TRIGGER
AS $$
BEGIN
	-- NEW represents the new row or the row being updated.
	IF NEW.top_speed < 0 THEN
		NEW.top_speed := 5;
	END IF;

	RETURN NEW; -- Returns the row so it can be inserted or updated.
END;
$$ LANGUAGE plpgsql;

-- Creates the trigger and defines when it runs.
CREATE TRIGGER check_speed -- Trigger name.
BEFORE INSERT OR UPDATE ON CARS -- Runs before an insert or update.
FOR EACH ROW -- Runs once for each affected row.
EXECUTE PROCEDURE check_top_speed(); -- Calls the trigger function.

INSERT INTO cars( brand, model, top_speed)
VALUES ( 'Audi', 'R8', '-320' );

-- Example result: top_speed is set to 5 by the trigger.
-- 16	"Audi"	"R8"	4	"5.000"

UPDATE cars SET top_speed = -20 WHERE id = 1;

-- Example result: top_speed is set to 5.
-- 1	"Dodge"	"Viper"	6	5.000
