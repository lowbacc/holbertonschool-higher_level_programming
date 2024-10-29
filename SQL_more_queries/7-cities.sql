-- Create a new table cities with the following fields:
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'hbtn_0d_usa')
BEGIN
    CREATE DATABASE hbtn_0d_usa;
END;

USE hbtn_0d_usa;

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'cities')
BEGIN
    CREATE TABLE cities (
    id INT IDENTITY(1,1) UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
    );
END;