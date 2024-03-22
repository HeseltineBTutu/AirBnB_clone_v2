-- Create the database only if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user only if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant full privileges on the 'hbnb_test_db' database 
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Ensure changes take effect
FLUSH PRIVILEGES;
