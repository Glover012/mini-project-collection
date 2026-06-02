-- GROUP BY groups rows by the selected column before applying aggregate functions.
SELECT COUNT(id), brand FROM cars GROUP BY brand;
