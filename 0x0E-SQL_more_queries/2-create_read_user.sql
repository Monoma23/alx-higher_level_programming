-- Creates the databasee hbtn_0d_2
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- Createss the user user_0d_2 withh password 
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grantss ability to connect to the server
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- Grants SELECTT privilege to user_0d_2 on database hbtn_0d_2 
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
