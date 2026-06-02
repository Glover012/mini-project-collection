-- Inserts rows into the cars table.
INSERT INTO cars(brand, model, num_gears, top_speed) -- Lists the columns that receive new values.
-- Values are provided in the same order as the column list.
VALUES ('Dodge', 'Viper', 6, 290.123), 
-- Multiple rows can be inserted in one statement by separating them with commas.
('Ford', 'Mustang', '5', 230.456),
('Plymouth', 'Hemi-Cuda', '4', 200),
('Dodge', 'Charger', '4', 190);
