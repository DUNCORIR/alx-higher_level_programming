-- Script that creates the table id_not_null on your MySQL server.
-- The database name will be passed as an argument of the mysql command.

-- Create the table 'id_not_null' if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,  -- Set default value of id to 1
	name VARCHAR(256)  -- name column of type VARCHAR(256)
);
