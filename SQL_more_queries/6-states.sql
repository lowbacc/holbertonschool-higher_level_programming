-- Create a new database hbtn_0d_usa and a new table states with the following requirements:
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'hbtn_0d_usa')
BEGIN
    CREATE DATABASE hbtn_0d_usa;
END;

USE hbtn_0d_usa;

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'states')
BEGIN
    CREATE TABLE states (
        id INT IDENTITY(1,1) UNIQUE NOT NULL PRIMARY KEY,
        name VARCHAR(256) NOT NULL
    );
END;