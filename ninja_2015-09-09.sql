# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.6.24)
# Database: ninja
# Generation Time: 2015-09-09 06:17:11 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table codes
# ------------------------------------------------------------

DROP TABLE IF EXISTS `codes`;

CREATE TABLE `codes` (
  `code_id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(32) DEFAULT '',
  `used` int(1) NOT NULL DEFAULT '0',
  `student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`code_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `codes` WRITE;
/*!40000 ALTER TABLE `codes` DISABLE KEYS */;

INSERT INTO `codes` (`code_id`, `code`, `used`, `student_id`)
VALUES
	(1,'g34m5',0,NULL),
	(2,'882ff',0,NULL),
	(3,'9t3e8',0,NULL),
	(4,'a4g1o',0,NULL),
	(5,'eenlm',0,NULL),
	(6,'3rpz3',0,NULL),
	(7,'dpkn1',0,NULL),
	(8,'fm6uh',0,NULL),
	(9,'0jv6l',0,NULL),
	(10,'9ldy3',0,NULL),
	(11,'d5gm9',0,NULL),
	(12,'cvi2c',0,NULL),
	(13,'fzlzh',0,NULL),
	(14,'cejg2',0,NULL),
	(15,'5gweu',0,NULL),
	(16,'2f3qo',0,NULL),
	(17,'5psgn',0,NULL),
	(18,'mmqqz',0,NULL),
	(19,'ozo08',0,NULL),
	(20,'sq0vc',0,NULL);

/*!40000 ALTER TABLE `codes` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
