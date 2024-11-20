-- Script that creates the table unique_id on your MySQL server.
-- The database name will be passed as an argument of the mysql command

-- Create the table 'unique_id' if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1, -- id column with default value of 1 and UNIQUE constraint
	name VARCHAR(256)        -- name column with VARCHAR(256) type
);
