CREATE DATABASE IF NOT EXISTS clientDB;
USE clientDB;
CREATE TABLE IF NOT EXISTS clientData (
    id varchar(50) NOT NULL,
    name varchar(50),
    plan varchar(20),
    token varchar(100),
    PRIMARY KEY (ID)
);
CREATE USER 'clientDBuname'@'%' IDENTIFIED BY 'ClientPW';
GRANT ALL ON clientDB TO 'clientDBuname'@'%';
