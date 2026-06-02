-- RETURNING id returns the id of the newly inserted row.
INSERT INTO public.cars( brand, model )
	VALUES ('Aston Martin', 'DB9') RETURNING id;
