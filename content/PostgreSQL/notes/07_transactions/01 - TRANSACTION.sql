-- Transactions help protect a set of database operations from partial completion.
-- If one statement fails, the transaction can be rolled back.
-- This lets the database return to its previous state instead of applying only some changes.
-- Changes are saved only when all statements complete successfully.

BEGIN; -- Starts the transaction.

INSERT INTO cars (brand, model) VALUES ('Ford', 'GT');

SELECT * FROM cars;

COMMIT; -- Commits the transaction.
