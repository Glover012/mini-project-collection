-- Creates the cars table only if it does not already exist.
-- The table includes basic text, numeric, date and timestamp columns.
CREATE TABLE IF NOT EXISTS cars (
	id SERIAL PRIMARY KEY,
	brand VARCHAR(24) NOT NULL,
	model VARCHAR(24) NOT NULL,
	num_gears SMALLINT DEFAULT 4,
	top_speed NUMERIC(6,2),
	production_date DATE DEFAULT CURRENT_DATE,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);
