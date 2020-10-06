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
  `category` varchar(20) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`volume_no`,`issue_no`,`page_no`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`volume_no`, `issue_no`) REFERENCES `magazine` (`volume_no`, `issue_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
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
  `languages` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `author_ibfk_1` FOREIGN KEY (`id`) REFERENCES `members` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cartoon`
--

DROP TABLE IF EXISTS `cartoon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cartoon` (
  `image_url` varchar(500) NOT NULL,
  `caption` varchar(200) DEFAULT NULL,
  `tags` varchar(200) DEFAULT NULL,
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
  `softwaress` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `designer_ibfk_1` FOREIGN KEY (`id`) REFERENCES `members` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `designer`
--

LOCK TABLES `designer` WRITE;
/*!40000 ALTER TABLE `designer` DISABLE KEYS */;
/*!40000 ALTER TABLE `designer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `draws`
--

DROP TABLE IF EXISTS `draws`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `draws` (
  `cartoon` varchar(300) NOT NULL,
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
  `genres` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `editor_ibfk_1` FOREIGN KEY (`id`) REFERENCES `members` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editor`
--

LOCK TABLES `editor` WRITE;
/*!40000 ALTER TABLE `editor` DISABLE KEYS */;
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
  `platforms` varchar(500) DEFAULT NULL,
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
  `f_name` varchar(100) DEFAULT NULL,
  `m_name` varchar(100) DEFAULT NULL,
  `l_name` varchar(100) DEFAULT NULL,
  `join_date` date DEFAULT NULL,
  `superviser_id` int DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Members`
--

LOCK TABLES `Members` WRITE;
/*!40000 ALTER TABLE `Members` DISABLE KEYS */;
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
  `product` varchar(200) DEFAULT NULL,
  `payment` varchar(200) DEFAULT NULL,
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
  `email` varchar(200) NOT NULL,
  `sub_type` int DEFAULT NULL,
  `sub_date` date DEFAULT NULL,
  `f_name` varchar(100) DEFAULT NULL,
  `m_name` varchar(100) DEFAULT NULL,
  `l_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscribers`
--

LOCK TABLES `subscribers` WRITE;
/*!40000 ALTER TABLE `subscribers` DISABLE KEYS */;
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
  `subscriber` varchar(100) NOT NULL,
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
/*!40000 ALTER TABLE `subscribes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supervise`
--

DROP TABLE IF EXISTS `supervise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supervise` (
  `member` int DEFAULT NULL,
  `supervisor` int DEFAULT NULL,
  KEY `member` (`member`),
  KEY `superviser` (`supervisor`),
  CONSTRAINT `supervise_ibfk_1` FOREIGN KEY (`member`) REFERENCES `members` (`member_id`),
  CONSTRAINT `supervise_ibfk_2` FOREIGN KEY (`supervisor`) REFERENCES `members` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supervise`
--

LOCK TABLES `supervise` WRITE;
/*!40000 ALTER TABLE `supervise` DISABLE KEYS */;
/*!40000 ALTER TABLE `supervise` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-06  6:04:19
