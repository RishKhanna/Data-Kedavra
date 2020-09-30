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

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `data_kedavra` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `data_kedavra`;

--
-- Table structure for table `Article`
--

DROP TABLE IF EXISTS `Article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Article` (
  `page_no` int NOT NULL,
  `category` varchar(100) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`page_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Article`
--

LOCK TABLES `Article` WRITE;
/*!40000 ALTER TABLE `Article` DISABLE KEYS */;
/*!40000 ALTER TABLE `Article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Author`
--

DROP TABLE IF EXISTS `Author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Author` (
  `id` int NOT NULL,
  `languages` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Author`
--

LOCK TABLES `Author` WRITE;
/*!40000 ALTER TABLE `Author` DISABLE KEYS */;
/*!40000 ALTER TABLE `Author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cartoon`
--

DROP TABLE IF EXISTS `Cartoon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cartoon` (
  `image_url` varchar(500) DEFAULT NULL,
  `caption` varchar(200) DEFAULT NULL,
  `tags` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cartoon`
--

LOCK TABLES `Cartoon` WRITE;
/*!40000 ALTER TABLE `Cartoon` DISABLE KEYS */;
/*!40000 ALTER TABLE `Cartoon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Contains`
--

DROP TABLE IF EXISTS `Contains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Contains` (
  `volume` int DEFAULT NULL,
  `issue` int DEFAULT NULL,
  `cartoon` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contains`
--

LOCK TABLES `Contains` WRITE;
/*!40000 ALTER TABLE `Contains` DISABLE KEYS */;
/*!40000 ALTER TABLE `Contains` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Contribute`
--

DROP TABLE IF EXISTS `Contribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Contribute` (
  `editor_id` int DEFAULT NULL,
  `author_id` int DEFAULT NULL,
  `designer_id` int DEFAULT NULL,
  `volume_no` int DEFAULT NULL,
  `issue_no` int DEFAULT NULL,
  `page_no` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contribute`
--

LOCK TABLES `Contribute` WRITE;
/*!40000 ALTER TABLE `Contribute` DISABLE KEYS */;
/*!40000 ALTER TABLE `Contribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Designer`
--

DROP TABLE IF EXISTS `Designer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Designer` (
  `id` int NOT NULL,
  `softwaress` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Designer`
--

LOCK TABLES `Designer` WRITE;
/*!40000 ALTER TABLE `Designer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Designer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Draws`
--

DROP TABLE IF EXISTS `Draws`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Draws` (
  `cartoon` varchar(300) DEFAULT NULL,
  `designer_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Draws`
--

LOCK TABLES `Draws` WRITE;
/*!40000 ALTER TABLE `Draws` DISABLE KEYS */;
/*!40000 ALTER TABLE `Draws` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Editor`
--

DROP TABLE IF EXISTS `Editor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Editor` (
  `id` int DEFAULT NULL,
  `genres` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Editor`
--

LOCK TABLES `Editor` WRITE;
/*!40000 ALTER TABLE `Editor` DISABLE KEYS */;
/*!40000 ALTER TABLE `Editor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Includes`
--

DROP TABLE IF EXISTS `Includes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Includes` (
  `issue` int DEFAULT NULL,
  `volume` int DEFAULT NULL,
  `page` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Includes`
--

LOCK TABLES `Includes` WRITE;
/*!40000 ALTER TABLE `Includes` DISABLE KEYS */;
/*!40000 ALTER TABLE `Includes` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Magazine`
--

LOCK TABLES `Magazine` WRITE;
/*!40000 ALTER TABLE `Magazine` DISABLE KEYS */;
/*!40000 ALTER TABLE `Magazine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Marketing`
--

DROP TABLE IF EXISTS `Marketing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Marketing` (
  `id` int NOT NULL,
  `platforms` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Marketing`
--

LOCK TABLES `Marketing` WRITE;
/*!40000 ALTER TABLE `Marketing` DISABLE KEYS */;
/*!40000 ALTER TABLE `Marketing` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Members`
--

LOCK TABLES `Members` WRITE;
/*!40000 ALTER TABLE `Members` DISABLE KEYS */;
/*!40000 ALTER TABLE `Members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Selling_advert`
--

DROP TABLE IF EXISTS `Selling_advert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Selling_advert` (
  `sponsor_id` int NOT NULL,
  `marketers_id` int NOT NULL,
  PRIMARY KEY (`sponsor_id`,`marketers_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Selling_advert`
--

LOCK TABLES `Selling_advert` WRITE;
/*!40000 ALTER TABLE `Selling_advert` DISABLE KEYS */;
/*!40000 ALTER TABLE `Selling_advert` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sponsors`
--

LOCK TABLES `Sponsors` WRITE;
/*!40000 ALTER TABLE `Sponsors` DISABLE KEYS */;
/*!40000 ALTER TABLE `Sponsors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Subscribers`
--

DROP TABLE IF EXISTS `Subscribers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Subscribers` (
  `email` varchar(200) DEFAULT NULL,
  `sub_type` int DEFAULT NULL,
  `sub_date` date DEFAULT NULL,
  `f_name` varchar(100) DEFAULT NULL,
  `m_name` varchar(100) DEFAULT NULL,
  `l_name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Subscribers`
--

LOCK TABLES `Subscribers` WRITE;
/*!40000 ALTER TABLE `Subscribers` DISABLE KEYS */;
/*!40000 ALTER TABLE `Subscribers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscribes`
--

DROP TABLE IF EXISTS `subscribes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subscribes` (
  `volume` int DEFAULT NULL,
  `issue` int DEFAULT NULL,
  `subscriber` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscribes`
--

LOCK TABLES `subscribes` WRITE;
/*!40000 ALTER TABLE `subscribes` DISABLE KEYS */;
/*!40000 ALTER TABLE `subscribes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supervise`
--

DROP TABLE IF EXISTS `Supervise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supervise` (
  `member` int DEFAULT NULL,
  `superviser` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supervise`
--

LOCK TABLES `Supervise` WRITE;
/*!40000 ALTER TABLE `Supervise` DISABLE KEYS */;
/*!40000 ALTER TABLE `Supervise` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-30 11:40:08
