-- create a database and the table.
CREATE DATABASE if NOT EXISTS hbtn_0d_usa;
CREATE Table IF NOT EXISTS `hbtn_0d_usa`.`states`(PRIMARY KEY(id), id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL);