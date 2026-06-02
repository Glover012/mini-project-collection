-- ALTER TABLE allows modifying an existing table.
-- NUMERIC(10,2) stores up to 10 digits, including 2 decimal places.
-- DEFAULT 9999 sets the default value for new records.
ALTER TABLE cars ADD price NUMERIC(10,2) DEFAULT 9999;

-- Adds a color column with a default text value.
ALTER TABLE cars ADD color VARCHAR(12) DEFAULT 'Not set';

-- Removes the color column from the table.
ALTER TABLE cars DROP COLUMN color;
