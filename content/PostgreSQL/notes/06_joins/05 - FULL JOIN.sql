-- FULL JOIN returns matching rows plus unmatched rows from both tables.
SELECT cars.id AS "Car ID", cars.brand, cars.model, drivers.id AS "Driver ID", drivers.name FROM cars FULL JOIN drivers
ON cars.driver_id = drivers.id;
