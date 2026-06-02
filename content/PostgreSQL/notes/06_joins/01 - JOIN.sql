-- Creates a new table.
CREATE TABLE IF NOT EXISTS drivers(
	id SERIAL PRIMARY KEY,
	name varchar(16) NOT NULL
);

-- Adds example records to the drivers table.
INSERT INTO public.drivers(name)
	VALUES ('Tom'), ('Matt'), ('Ronald'), ('Ashley');

-- Adds driver_id to cars and links it to the drivers table.
ALTER TABLE cars ADD COLUMN driver_id INTEGER REFERENCES drivers(id);
