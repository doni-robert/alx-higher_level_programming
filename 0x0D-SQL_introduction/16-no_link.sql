-- Lists all records of the table second_table of the database except rows
-- with a NULL name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
