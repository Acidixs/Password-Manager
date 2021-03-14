-- 
-- Set character set the client will use to send SQL statements to the server
--
SET NAMES 'utf8';

--
-- Set default database
--
USE safepass;

--
-- Create table `master`
--
CREATE TABLE master (
  master_password varchar(100) NOT NULL,
  PRIMARY KEY (master_password)
)
ENGINE = INNODB,
AVG_ROW_LENGTH = 16384,
CHARACTER SET utf8,
COLLATE utf8_general_ci;