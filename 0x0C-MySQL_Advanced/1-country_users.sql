-- script to create table 'users' with attributes:
-- id, email, name, and country. If the table exists it should not fail
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US')    
);