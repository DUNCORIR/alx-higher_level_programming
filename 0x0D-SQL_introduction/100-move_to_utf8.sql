-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4
--  collate utf8mb4_unicode_ci) in your MySQL server.

USE hbtn_0c_0;

-- Converts database to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Converts table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Converts 'name' field in the first_table to utf8mb4
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
