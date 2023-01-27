CREATE DATABASE IF NOT EXISTS testDB;
USE testDB;
CREATE TABLE IF NOT EXISTS testtable (
    id varchar(50) NOT NULL,
    name varchar(50),
    plan varchar(20),
    token varchar(100),
    PRIMARY KEY (ID)
);
CREATE USER 'testuser'@'%' IDENTIFIED BY 'testPW';
GRANT ALL ON testDB.* TO 'testuser'@'%';
