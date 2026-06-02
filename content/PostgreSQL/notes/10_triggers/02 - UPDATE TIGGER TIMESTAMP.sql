-- Trigger that updates the row modification timestamp.

ALTER TABLE cars ADD COLUMN updated TIMESTAMP; -- Adds the updated column to cars.

-- Function that assigns the current timestamp to NEW.updated.
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
	NEW.updated := NOW();
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Creates the trigger.
CREATE TRIGGER update_car_timestamp
BEFORE UPDATE ON cars -- Runs before each row update.
FOR EACH ROW
EXECUTE PROCEDURE update_timestamp();

-- Updates a row.
UPDATE cars SET top_speed = -40 WHERE id = 4;

-- Example result: updated receives a new timestamp and top_speed is corrected by the trigger.
-- 4	"Plymouth"	"Hemi-Cuda"	4	5.000	"2026-01-30"	"2026-01-30 16:05:17.84059"	55000.00	"Red"	2	"2026-02-10 23:32:43.844824"
