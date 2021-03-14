-- 
-- Set character set the client will use to send SQL statements to the server
--
SET NAMES 'utf8';

--
-- Set default database
--
USE safepass;

--
-- Create table `user`
--
CREATE TABLE user (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(100) DEFAULT NULL,
  passwords varchar(100) DEFAULT NULL,
  date_added datetime DEFAULT NULL,
  PRIMARY KEY (id)
)
ENGINE = INNODB,
AUTO_INCREMENT = 11,
AVG_ROW_LENGTH = 8192,
CHARACTER SET utf8,
COLLATE utf8_general_ci;