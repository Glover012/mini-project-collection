-- INNER JOIN returns only rows that have matching keys in both tables.
-- In this example, cars without an assigned driver_id are not returned.
SELECT cars.id AS "Car ID", cars.brand, cars.model, drivers.id AS "Driver ID", drivers.name FROM CARS INNER JOIN drivers
ON cars.driver_id = drivers.id;
