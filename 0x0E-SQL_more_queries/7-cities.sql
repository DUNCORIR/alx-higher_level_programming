-- script that creates the database hbtn_0d_usa and the table
-- cities (in the database hbtn_0d_usa) on your MySQL server

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,  -- Unique, auto-generated, primary key
	state_id INT NOT NULL,  -- Foreign key to states(id), not null
       	name VARCHAR(256) NOT NULL,  -- Non-null name column
	FOREIGN KEY (state_id) REFERENCES states(id) -- Foreign key constraint
);
