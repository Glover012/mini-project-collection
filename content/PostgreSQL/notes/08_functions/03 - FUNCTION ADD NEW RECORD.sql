CREATE OR REPLACE FUNCTION add_car(brand VARCHAR, model VARCHAR)
RETURNS VOID AS $$ -- The function inserts a new row and does not return a value.
DECLARE
-- RANDOM returns a value between 0 and 1.
-- :: casts a value to another data type.
-- floor() rounds the value down.
	top_speed INTEGER := (100 + floor(random()*151))::INTEGER;
BEGIN
	INSERT INTO cars(brand, model, top_speed) VALUES (brand, model, top_speed);
END;
$$ LANGUAGE plpgsql;
