CREATE OR REPLACE FUNCTION add_car_and_driver(car_brand VARCHAR, car_model VARCHAR, driver_name VARCHAR)
RETURNS VOID AS $$
DECLARE -- Defines local variables used inside the function.
	driver_id INTEGER; -- Local variable.
BEGIN
	-- Gets the driver id and stores it in the local driver_id variable.
	-- This also checks whether the driver exists.
	SELECT id INTO driver_id FROM drivers WHERE name = driver_name;
	-- If no driver with this name exists, driver_id will be NULL.
	IF driver_id IS NULL THEN
		-- If the driver does not exist, insert it into drivers and store its new id.
		-- This id is then used in the cars table.
		INSERT INTO drivers (name) VALUES (driver_name) RETURNING id INTO driver_id;
	END IF;

	INSERT INTO cars (brand, model, driver_id) VALUES (car_brand, car_model, driver_id);
END;
$$ LANGUAGE plpgsql;
