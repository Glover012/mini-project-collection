-- Column aliases change the names returned in the query result.
-- External code should reference these alias names when reading the result.
SELECT 
id AS "ID", 
brand AS "Producer", 
model AS "Car model", 
num_gears AS "Gears amount",
top_speed AS "Max speed",
production_date AS "Procution date",
created AS "Record created"
FROM cars;
