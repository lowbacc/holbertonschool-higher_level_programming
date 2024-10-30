-- Create states table in hbtn_0e_0_usa with some data
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'hbtn_0e_0_usa')
BEGIN
    CREATE DATABASE hbtn_0e_0_usa;
END;
USE hbtn_0e_0_usa;
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'states')
BEGIN
    CREATE TABLE states ( 
        id INT NOT NULL IDENTITY(1,1), 
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
    );
END;
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
