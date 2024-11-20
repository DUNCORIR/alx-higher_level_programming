-- Script that creates the MySQL server user user_0d_1.
-- user_0d_1 should have all privileges on your MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd.
-- If the user user_0d_1 already exists, your script should not fail

-- Check if the user exists and create if user if not.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Reload privileges to apply changes
FLUSH PRIVILEGES;
