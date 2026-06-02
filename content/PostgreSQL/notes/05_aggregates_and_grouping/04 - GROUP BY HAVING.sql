-- HAVING filters grouped results after GROUP BY.
SELECT COUNT(id), brand FROM cars GROUP BY brand HAVING COUNT(id) >= 2;
