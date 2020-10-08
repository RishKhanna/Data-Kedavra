-- MySQL dump 10.13  Distrib 8.0.21, for osx10.15 (x86_64)
--
-- Host: localhost    Database: data_kedavra
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `data_kedavra`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `data_kedavra` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `data_kedavra`;
--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article` (
  `volume_no` int NOT NULL,
  `issue_no` int NOT NULL,
  `page_no` int NOT NULL,
  `category` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`volume_no`,`issue_no`,`page_no`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`volume_no`, `issue_no`) REFERENCES `magazine` (`volume_no`, `issue_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,4,1,'Science','2017 in Tech'),(1,4,16,'Science','Nobel Prizes 2017'),(1,4,31,'Entertainment','Netflix Review: DARK'),(3,4,1,'Sports','IPL Predictions'),(3,4,11,'Politics','US Elections: Preview');
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `author` (
  `id` int NOT NULL,
  `languages` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `author_ibfk_1` FOREIGN KEY (`id`) REFERENCES `members` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES (101,'English'),(102,'Hindi'),(103,'English');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cartoon`
--

DROP TABLE IF EXISTS `cartoon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cartoon` (
  `image_url` varchar(500) COLLATE utf8mb4_general_ci NOT NULL,
  `caption` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tags` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `volume_no` int NOT NULL,
  `issue_no` int NOT NULL,
  PRIMARY KEY (`image_url`,`volume_no`,`issue_no`),
  KEY `volume_no` (`volume_no`,`issue_no`),
  CONSTRAINT `cartoon_ibfk_1` FOREIGN KEY (`volume_no`, `issue_no`) REFERENCES `magazine` (`volume_no`, `issue_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cartoon`
--

LOCK TABLES `cartoon` WRITE;
/*!40000 ALTER TABLE `cartoon` DISABLE KEYS */;
INSERT INTO `cartoon` VALUES ('www.freak.in/cartoon/01.png','NaMo is back','Politics',1,4),('www.freak.in/cartoon/02.png','Chandrayan-2','News',1,4),('www.freak.in/cartoon/03.png','Kagaz Nahi Dikhayenge','Politics',1,4),('www.freak.in/cartoon/04.png','\"Happy\" New Year','Humour',3,4),('www.freak.in/cartoon/05.png','China Strikes Again','Corona',3,4),('www.freak.in/cartoon/06.png','Indefinite Homecoming','Corona',3,4),('www.freak.in/cartoon/07.png','Online Education','Corona',3,4),('www.freak.in/cartoon/08.png','WhiteHat Jr','Current Affairs',3,4),('www.freak.in/cartoon/09.png','PUBG Ban','News',3,4);
/*!40000 ALTER TABLE `cartoon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contribute`
--

DROP TABLE IF EXISTS `contribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contribute` (
  `editor_id` int DEFAULT NULL,
  `author_id` int DEFAULT NULL,
  `designer_id` int DEFAULT NULL,
  `volume_no` int DEFAULT NULL,
  `issue_no` int DEFAULT NULL,
  `page_no` int DEFAULT NULL,
  KEY `editor_id` (`editor_id`),
  KEY `author_id` (`author_id`),
  KEY `designer_id` (`designer_id`),
  KEY `volume_no` (`volume_no`,`issue_no`,`page_no`),
  CONSTRAINT `contribute_ibfk_1` FOREIGN KEY (`editor_id`) REFERENCES `editor` (`id`),
  CONSTRAINT `contribute_ibfk_2` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`),
  CONSTRAINT `contribute_ibfk_3` FOREIGN KEY (`designer_id`) REFERENCES `designer` (`id`),
  CONSTRAINT `contribute_ibfk_4` FOREIGN KEY (`volume_no`, `issue_no`, `page_no`) REFERENCES `article` (`volume_no`, `issue_no`, `page_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contribute`
--

LOCK TABLES `contribute` WRITE;
/*!40000 ALTER TABLE `contribute` DISABLE KEYS */;
INSERT INTO `contribute` VALUES (202,101,302,1,4,1),(201,103,301,1,4,16),(202,102,302,1,4,31),(203,103,301,3,4,1),(201,101,302,3,4,11);
/*!40000 ALTER TABLE `contribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `designer`
--

DROP TABLE IF EXISTS `designer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `designer` (
  `id` int NOT NULL,
  `softwaress` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `designer_ibfk_1` FOREIGN KEY (`id`) REFERENCES `members` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `designer`
--

LOCK TABLES `designer` WRITE;
/*!40000 ALTER TABLE `designer` DISABLE KEYS */;
INSERT INTO `designer` VALUES (301,'Photoshop'),(302,'GIMP');
/*!40000 ALTER TABLE `designer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `draws`
--

DROP TABLE IF EXISTS `draws`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `draws` (
  `cartoon` varchar(300) COLLATE utf8mb4_general_ci NOT NULL,
  `designer_id` int DEFAULT NULL,
  PRIMARY KEY (`cartoon`),
  KEY `designer_id` (`designer_id`),
  CONSTRAINT `draws_ibfk_1` FOREIGN KEY (`designer_id`) REFERENCES `designer` (`id`),
  CONSTRAINT `draws_ibfk_2` FOREIGN KEY (`cartoon`) REFERENCES `cartoon` (`image_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `draws`
--

LOCK TABLES `draws` WRITE;
/*!40000 ALTER TABLE `draws` DISABLE KEYS */;
INSERT INTO `draws` VALUES ('www.freak.in/cartoon/01.png',301),('www.freak.in/cartoon/03.png',301),('www.freak.in/cartoon/06.png',301),('www.freak.in/cartoon/07.png',301),('www.freak.in/cartoon/02.png',302),('www.freak.in/cartoon/04.png',302),('www.freak.in/cartoon/05.png',302),('www.freak.in/cartoon/08.png',302),('www.freak.in/cartoon/09.png',302);
/*!40000 ALTER TABLE `draws` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editor`
--

DROP TABLE IF EXISTS `editor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editor` (
  `id` int NOT NULL,
  `genres` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `editor_ibfk_1` FOREIGN KEY (`id`) REFERENCES `members` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editor`
--

LOCK TABLES `editor` WRITE;
/*!40000 ALTER TABLE `editor` DISABLE KEYS */;
INSERT INTO `editor` VALUES (201,'Science'),(202,'Sports'),(203,'Business');
/*!40000 ALTER TABLE `editor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Magazine`
--

DROP TABLE IF EXISTS `Magazine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Magazine` (
  `volume_no` int NOT NULL,
  `issue_no` int NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`volume_no`,`issue_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Magazine`
--

LOCK TABLES `Magazine` WRITE;
/*!40000 ALTER TABLE `Magazine` DISABLE KEYS */;
INSERT INTO `Magazine` VALUES (1,4,'2018-01-01'),(3,4,'2020-07-01');
/*!40000 ALTER TABLE `Magazine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marketing`
--

DROP TABLE IF EXISTS `marketing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marketing` (
  `id` int NOT NULL,
  `platforms` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `marketing_ibfk_1` FOREIGN KEY (`id`) REFERENCES `members` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marketing`
--

LOCK TABLES `marketing` WRITE;
/*!40000 ALTER TABLE `marketing` DISABLE KEYS */;
/*!40000 ALTER TABLE `marketing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Members`
--

DROP TABLE IF EXISTS `Members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Members` (
  `member_id` int NOT NULL,
  `f_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `m_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `l_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `join_date` date DEFAULT NULL,
  `superviser_id` int DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Members`
--

LOCK TABLES `Members` WRITE;
/*!40000 ALTER TABLE `Members` DISABLE KEYS */;
INSERT INTO `Members` VALUES (101,'Sugma','','Sharma','2017-10-06',201,'sugma.sharma@freak.in'),(102,'Sukh','Deep','Gill','2017-10-07',101,'sukh.gill@freak.in'),(103,'E','Rex','Sean','2018-01-27',101,'e.sean@freak.in'),(201,'Ligma','','Kapoor','2017-10-06',NULL,'editor.in.chief@freak.in'),(202,'Vye','','Brator','2018-05-03',201,'vye.brator@freak.in'),(203,'Lee','','Nover','2018-09-13',201,'lee.nover@freak.in'),(301,'Hugh','','Jazz','2017-10-28',201,'hugh.jazz@freak.in'),(302,'I','P','Freely','2018-03-21',301,'i.freely@freak.in'),(401,'Ben','','Chaudhary','2017-11-17',201,'info@freak.in'),(402,'Harry','','Cox','2018-07-08',401,'harry.cox@freak.in');
/*!40000 ALTER TABLE `Members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `selling_advert`
--

DROP TABLE IF EXISTS `selling_advert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `selling_advert` (
  `sponsor_id` int NOT NULL,
  `marketers_id` int NOT NULL,
  PRIMARY KEY (`sponsor_id`,`marketers_id`),
  KEY `marketers_id` (`marketers_id`),
  CONSTRAINT `selling_advert_ibfk_2` FOREIGN KEY (`sponsor_id`) REFERENCES `sponsors` (`sponsor_id`),
  CONSTRAINT `selling_advert_ibfk_3` FOREIGN KEY (`marketers_id`) REFERENCES `marketing` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `selling_advert`
--

LOCK TABLES `selling_advert` WRITE;
/*!40000 ALTER TABLE `selling_advert` DISABLE KEYS */;
/*!40000 ALTER TABLE `selling_advert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sponsors`
--

DROP TABLE IF EXISTS `Sponsors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Sponsors` (
  `sponsor_id` int NOT NULL,
  `product` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `payment` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`sponsor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sponsors`
--

LOCK TABLES `Sponsors` WRITE;
/*!40000 ALTER TABLE `Sponsors` DISABLE KEYS */;
/*!40000 ALTER TABLE `Sponsors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscribers`
--

DROP TABLE IF EXISTS `subscribers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subscribers` (
  `email` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `sub_type` int DEFAULT NULL,
  `sub_date` date DEFAULT NULL,
  `f_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `m_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `l_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscribers`
--

LOCK TABLES `subscribers` WRITE;
/*!40000 ALTER TABLE `subscribers` DISABLE KEYS */;
INSERT INTO `subscribers` VALUES ('angelpriya01@gmail.com',1,'2017-11-26','Ashok','','Kumar'),('codelixir@gmail.com',3,'2020-10-06','Vesper','','Paul'),('deutranium@gmail.com',3,'2020-10-04','Shitrija','','Jaglumiere'),('dungeon_master@gmail.com',1,'2018-02-28','Apollo','','Dionysus'),('heart_hacker@gmail.com',1,'2017-12-04','Rinku','','Mishra'),('ilove80085@gmail.com',1,'2017-12-28','Bobby','','Deol'),('kyabacchahai@gmail.com',3,'2020-10-05','Risabh','','Bhasin'),('sexyboy69@hotmail.com',2,'2018-01-23','Binod','','Sharma'),('souljaboy123@gmail.com',1,'2017-11-01','Martin','Luther','King'),('stevejobsfanboy@gmail.com',2,'2018-03-13','Mark','','Zuckerberg');
/*!40000 ALTER TABLE `subscribers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscribes`
--

DROP TABLE IF EXISTS `subscribes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subscribes` (
  `volume` int NOT NULL,
  `issue` int NOT NULL,
  `subscriber` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`volume`,`issue`,`subscriber`),
  KEY `subscriber` (`subscriber`),
  CONSTRAINT `subscribes_ibfk_1` FOREIGN KEY (`subscriber`) REFERENCES `subscribers` (`email`),
  CONSTRAINT `subscribes_ibfk_2` FOREIGN KEY (`volume`, `issue`) REFERENCES `magazine` (`volume_no`, `issue_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscribes`
--

LOCK TABLES `subscribes` WRITE;
/*!40000 ALTER TABLE `subscribes` DISABLE KEYS */;
INSERT INTO `subscribes` VALUES (1,4,'angelpriya01@gmail.com'),(3,4,'codelixir@gmail.com'),(3,4,'deutranium@gmail.com'),(3,4,'dungeon_master@gmail.com'),(1,4,'heart_hacker@gmail.com'),(1,4,'ilove80085@gmail.com'),(3,4,'kyabacchahai@gmail.com'),(1,4,'sexyboy69@hotmail.com'),(1,4,'souljaboy123@gmail.com'),(3,4,'stevejobsfanboy@gmail.com');
/*!40000 ALTER TABLE `subscribes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supervise`
--

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-08 19:05:52
