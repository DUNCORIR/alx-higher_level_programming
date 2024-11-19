-- Scripts that lists all rows of the table first-table
-- from database hbtn_0c_0 in MySQL server.

SELECT column_name, column_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0'
AND table_name = 'first_table';
