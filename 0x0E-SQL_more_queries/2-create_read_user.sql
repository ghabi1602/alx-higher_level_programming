-- create database and user with select privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2
USE DATABASE hbtn_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
