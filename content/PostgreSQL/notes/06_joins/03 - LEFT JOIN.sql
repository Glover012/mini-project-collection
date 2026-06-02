-- LEFT JOIN returns all rows from the left table (cars), including rows without a match.
SELECT cars.id AS "Car ID", cars.brand, cars.model, drivers.id AS "Driver ID", drivers.name FROM CARS LEFT JOIN drivers
ON cars.driver_id = drivers.id;
