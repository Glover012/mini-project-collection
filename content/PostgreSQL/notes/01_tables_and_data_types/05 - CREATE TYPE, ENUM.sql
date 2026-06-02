-- Creates a custom data type with predefined values.
-- The enum type can be viewed in PostgreSQL types.
CREATE TYPE car_color AS ENUM( 'Black', 'Red', 'Blue', 'Green' );

-- Adds a color column using the car_color enum type.
-- The default value for new records is 'Red'.
ALTER TABLE cars ADD color car_color DEFAULT 'Red';
