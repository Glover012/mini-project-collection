-- LIKE searches for text patterns when the exact value is not known.
-- % matches any sequence of characters, before, after or between known text.
-- Examples: '%th' matches values ending with 'th', and 'Do%' matches values starting with 'Do'.
-- _ matches exactly one character, for example '__rd' or '_o%'.
SELECT * FROM cars WHERE brand LIKE '_o%';
