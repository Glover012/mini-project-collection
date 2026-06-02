-- RIGHT JOIN returns all rows from the right table (drivers), including rows without a matching car.
SELECT cars.id AS "Car ID", cars.brand, cars.model, drivers.id AS "Driver ID", drivers.name FROM CARS RIGHT JOIN drivers
ON cars.driver_id = drivers.id;
