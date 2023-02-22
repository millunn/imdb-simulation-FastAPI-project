-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: imdb_simulation
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actor_actress_award_movie`
--

DROP TABLE IF EXISTS `actor_actress_award_movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actor_actress_award_movie` (
  `id` varchar(50) NOT NULL,
  `actor_actress_id` varchar(50) NOT NULL,
  `award_id` varchar(50) NOT NULL,
  `movie_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `actor_actress_award_movie_uc` (`actor_actress_id`,`award_id`,`movie_id`),
  KEY `award_id` (`award_id`),
  KEY `movie_id` (`movie_id`),
  CONSTRAINT `actor_actress_award_movie_ibfk_1` FOREIGN KEY (`actor_actress_id`) REFERENCES `actors_actresses` (`id`),
  CONSTRAINT `actor_actress_award_movie_ibfk_2` FOREIGN KEY (`award_id`) REFERENCES `awards` (`id`),
  CONSTRAINT `actor_actress_award_movie_ibfk_3` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actor_actress_award_movie`
--

LOCK TABLES `actor_actress_award_movie` WRITE;
/*!40000 ALTER TABLE `actor_actress_award_movie` DISABLE KEYS */;
INSERT INTO `actor_actress_award_movie` VALUES ('8144613a-9907-47ca-930d-4e6b7e96623d','170b5287-1bf6-437f-a73c-bdafbb2ab9ba','19d87238-3b5d-4b55-afa7-32cd97907b14','1e3b3c6a-2c02-437f-91c7-83337e5bf099'),('61dd41ca-665a-433a-93fd-4884df67b451','40d6b1b5-0dbb-4a3e-bbf1-37efc9f2d783','19d87238-3b5d-4b55-afa7-32cd97907b14','1e3b3c6a-2c02-437f-91c7-83337e5bf099'),('bb88847c-7069-4c4c-8e9b-964cc8a43273','654c6875-8b11-4656-9a00-67927a8f5c03','19d87238-3b5d-4b55-afa7-32cd97907b14','07cf8b53-696b-4be4-8585-a6b6a40153b2'),('dc718280-691d-42ec-bac0-a8303f6b293b','654c6875-8b11-4656-9a00-67927a8f5c03','19d87238-3b5d-4b55-afa7-32cd97907b14','0ba36696-aa9b-4bf2-8966-040188f970b8'),('312e7b07-de77-4ce5-9e41-d99bbdec2c27','654c6875-8b11-4656-9a00-67927a8f5c03','19d87238-3b5d-4b55-afa7-32cd97907b14','8a583bc1-f8fb-473d-8bca-d09950ed84f3');
/*!40000 ALTER TABLE `actor_actress_award_movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `actor_actress_award_tv_show`
--

DROP TABLE IF EXISTS `actor_actress_award_tv_show`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actor_actress_award_tv_show` (
  `id` varchar(50) NOT NULL,
  `actor_actress_id` varchar(50) NOT NULL,
  `award_id` varchar(50) NOT NULL,
  `tv_show_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `actor_actress_award_tv_show_uc` (`actor_actress_id`,`award_id`,`tv_show_id`),
  KEY `award_id` (`award_id`),
  KEY `tv_show_id` (`tv_show_id`),
  CONSTRAINT `actor_actress_award_tv_show_ibfk_1` FOREIGN KEY (`actor_actress_id`) REFERENCES `actors_actresses` (`id`),
  CONSTRAINT `actor_actress_award_tv_show_ibfk_2` FOREIGN KEY (`award_id`) REFERENCES `awards` (`id`),
  CONSTRAINT `actor_actress_award_tv_show_ibfk_3` FOREIGN KEY (`tv_show_id`) REFERENCES `tv_shows_and_series` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actor_actress_award_tv_show`
--

LOCK TABLES `actor_actress_award_tv_show` WRITE;
/*!40000 ALTER TABLE `actor_actress_award_tv_show` DISABLE KEYS */;
INSERT INTO `actor_actress_award_tv_show` VALUES ('15bc112c-6146-4bf3-bf0e-a2fc13093255','170b5287-1bf6-437f-a73c-bdafbb2ab9ba','d31d3fff-1a2b-41ac-8309-4e3e0c8b7a97','96b98bcd-b890-474c-aa4c-a30955860fe1'),('4ff6a564-7bc6-4af4-9899-4cfa010d2759','170b5287-1bf6-437f-a73c-bdafbb2ab9ba','d31d3fff-1a2b-41ac-8309-4e3e0c8b7a97','d04c70cc-8ddb-4117-8a69-99ab1f73a830'),('5a6d1deb-5305-4de0-ac2f-b794d1de9f2c','ac89b53b-9b03-4f11-b67e-088e2b673a2d','d31d3fff-1a2b-41ac-8309-4e3e0c8b7a97','96b98bcd-b890-474c-aa4c-a30955860fe1');
/*!40000 ALTER TABLE `actor_actress_award_tv_show` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `actors_actresses`
--

DROP TABLE IF EXISTS `actors_actresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actors_actresses` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `surname` varchar(50) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `about` varchar(180) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_surname_about_uc` (`name`,`surname`,`about`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actors_actresses`
--

LOCK TABLES `actors_actresses` WRITE;
/*!40000 ALTER TABLE `actors_actresses` DISABLE KEYS */;
INSERT INTO `actors_actresses` VALUES ('170b5287-1bf6-437f-a73c-bdafbb2ab9ba','Mila','Kunis','F','.......'),('2060035a-b077-4105-b8a3-814177b3fdd0','Charlie','Sheen','M','...'),('40d6b1b5-0dbb-4a3e-bbf1-37efc9f2d783','Brad','Smith','M','.........'),('654c6875-8b11-4656-9a00-67927a8f5c03','Sylvester','Stallone','M','...'),('707f853b-f040-42b1-9113-d5aea422de58','Ashton','Kutcher','M','...'),('ac89b53b-9b03-4f11-b67e-088e2b673a2d','Selma','Hayek','F','...');
/*!40000 ALTER TABLE `actors_actresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `awards`
--

DROP TABLE IF EXISTS `awards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `awards` (
  `id` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `subcategory` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `_category_subcategory_uc` (`category`,`subcategory`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `awards`
--

LOCK TABLES `awards` WRITE;
/*!40000 ALTER TABLE `awards` DISABLE KEYS */;
INSERT INTO `awards` VALUES ('19d87238-3b5d-4b55-afa7-32cd97907b14','Academy Award','Best Actor'),('d31d3fff-1a2b-41ac-8309-4e3e0c8b7a97','Academy Award','Best Actress'),('816764f2-00c8-4a47-b588-2b50ef4e0033','Academy Award','Best Director'),('cc918aa1-df1d-46a1-a022-0f5f0477f09a','Academy award','Best picture'),('200811b0-15db-495b-b5e0-1c41372c9673','Academy Award','Best Sound'),('f1ed2829-c8c9-48a2-b315-36b4376b08b1','Grammy','Best Actor'),('ae2c3f0a-91b9-4e72-a3bb-2a73e8bc8320','Grammy','Best Actress'),('7156b02b-34db-4fcf-a2f3-91650694785e','Grammy','Best TV Show');
/*!40000 ALTER TABLE `awards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `id` varchar(50) NOT NULL,
  `category` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES ('00ed117f-f901-4313-979b-3152371594c7','Comedy','...'),('690b78c3-4dd5-4627-94d8-0b4afd9d10ea','Action','.......'),('8c733f5d-0f59-4d3e-85a6-5e5658c3fa1f','Thriller','....');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `languages`
--

DROP TABLE IF EXISTS `languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `languages` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `abbreviation` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `languages`
--

LOCK TABLES `languages` WRITE;
/*!40000 ALTER TABLE `languages` DISABLE KEYS */;
INSERT INTO `languages` VALUES ('0dd312bb-4b0b-426f-8fe3-d76493484c62','English','EN'),('f1329bbe-9961-446f-9806-066fb32b98a8','French','FR');
/*!40000 ALTER TABLE `languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_actor_actress`
--

DROP TABLE IF EXISTS `movie_actor_actress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_actor_actress` (
  `id` varchar(50) NOT NULL,
  `movie_id` varchar(50) NOT NULL,
  `actor_actress_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `movie_actor_actress_uc` (`movie_id`,`actor_actress_id`),
  KEY `actor_actress_id` (`actor_actress_id`),
  CONSTRAINT `movie_actor_actress_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `movie_actor_actress_ibfk_2` FOREIGN KEY (`actor_actress_id`) REFERENCES `actors_actresses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_actor_actress`
--

LOCK TABLES `movie_actor_actress` WRITE;
/*!40000 ALTER TABLE `movie_actor_actress` DISABLE KEYS */;
INSERT INTO `movie_actor_actress` VALUES ('455c2491-6dba-4f83-844a-ded82d4de40b','07cf8b53-696b-4be4-8585-a6b6a40153b2','654c6875-8b11-4656-9a00-67927a8f5c03'),('2f8bd5a6-5cb9-4b16-b1b6-6923e224b0a5','07cf8b53-696b-4be4-8585-a6b6a40153b2','ac89b53b-9b03-4f11-b67e-088e2b673a2d'),('b44da359-c3a6-40a9-9ba0-b4c9ac1a84e7','1e3b3c6a-2c02-437f-91c7-83337e5bf099','170b5287-1bf6-437f-a73c-bdafbb2ab9ba'),('f3a7d003-23c2-4b59-9bd2-82c6ae80e7e1','1e3b3c6a-2c02-437f-91c7-83337e5bf099','40d6b1b5-0dbb-4a3e-bbf1-37efc9f2d783'),('a5a17371-a364-4d4b-8db2-c354b38173a1','1e3b3c6a-2c02-437f-91c7-83337e5bf099','707f853b-f040-42b1-9113-d5aea422de58');
/*!40000 ALTER TABLE `movie_actor_actress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_award`
--

DROP TABLE IF EXISTS `movie_award`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_award` (
  `id` varchar(50) NOT NULL,
  `movie_id` varchar(50) NOT NULL,
  `award_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `movie_award_uc` (`movie_id`,`award_id`),
  KEY `award_id` (`award_id`),
  CONSTRAINT `movie_award_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `movie_award_ibfk_2` FOREIGN KEY (`award_id`) REFERENCES `awards` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_award`
--

LOCK TABLES `movie_award` WRITE;
/*!40000 ALTER TABLE `movie_award` DISABLE KEYS */;
INSERT INTO `movie_award` VALUES ('a32e6ad1-dc10-4b17-bfe7-5b9e5559ae8f','07cf8b53-696b-4be4-8585-a6b6a40153b2','cc918aa1-df1d-46a1-a022-0f5f0477f09a'),('e58a462d-a1d0-4aa3-8b23-3f4b132ee402','0ba36696-aa9b-4bf2-8966-040188f970b8','200811b0-15db-495b-b5e0-1c41372c9673'),('58bf41e4-c34d-41d0-bad8-084d06606484','8a583bc1-f8fb-473d-8bca-d09950ed84f3','cc918aa1-df1d-46a1-a022-0f5f0477f09a');
/*!40000 ALTER TABLE `movie_award` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `id` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `plot` varchar(100) NOT NULL,
  `duration` int NOT NULL,
  `release_year` varchar(4) NOT NULL,
  `director` varchar(50) NOT NULL,
  `writer` varchar(50) NOT NULL,
  `producer` varchar(50) NOT NULL,
  `synopsis` varchar(180) NOT NULL,
  `language_name` varchar(30) NOT NULL,
  `genre_category` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title_release_year_uc` (`title`,`release_year`),
  KEY `language_name` (`language_name`),
  KEY `genre_category` (`genre_category`),
  CONSTRAINT `movies_ibfk_1` FOREIGN KEY (`language_name`) REFERENCES `languages` (`name`),
  CONSTRAINT `movies_ibfk_2` FOREIGN KEY (`genre_category`) REFERENCES `genres` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES ('07cf8b53-696b-4be4-8585-a6b6a40153b2','Roki_II','...',121,'1982','John Smith Jr','John Smith Jr','John Smith Jr','....','English','Action'),('0ba36696-aa9b-4bf2-8966-040188f970b8','Rambo_II','...',106,'1983','John Smith','John Smith','John Smith','....','English','Action'),('1e3b3c6a-2c02-437f-91c7-83337e5bf099','Jobs','...',120,'2012','John Smith III','John Smith III','John Smith III','....','English','Thriller'),('34222c07-5a6e-42a2-87d6-5f78afda5787','The Intouchables','...',135,'2011','John Smith III','John Smith III','John Smith III','....','French','Comedy'),('7928913a-6368-4066-b49a-be1ee86fc634','Cellular','...',135,'2006','John Smith III','John Smith III','John Smith III','....','English','Thriller'),('8a583bc1-f8fb-473d-8bca-d09950ed84f3','Roki','...',108,'1979','John Smith Jr','John Smith Jr','John Smith Jr','....','English','Action'),('b8102a41-fec2-4c4d-9432-15602157f037','Rambo','...',120,'1979','John Smith','John Smith','John Smith','....','English','Action'),('cb483982-7e92-46fe-a016-13aadc5658f0','Rambo_I','...',116,'1981','John Smith','John Smith','John Smith','....','English','Action');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies_rating_and_review`
--

DROP TABLE IF EXISTS `movies_rating_and_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies_rating_and_review` (
  `id` varchar(50) NOT NULL,
  `grade` int NOT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `comment_date` varchar(50) DEFAULT NULL,
  `movie_id` varchar(50) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `movie_user_uc` (`movie_id`,`user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `movies_rating_and_review_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `movies_rating_and_review_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies_rating_and_review`
--

LOCK TABLES `movies_rating_and_review` WRITE;
/*!40000 ALTER TABLE `movies_rating_and_review` DISABLE KEYS */;
INSERT INTO `movies_rating_and_review` VALUES ('09d476ec-9c0e-4a8d-98d8-61af32cb0f19',3,'...','2023-02-22, 00:47:04','0ba36696-aa9b-4bf2-8966-040188f970b8','03fab21b-30b4-4fbc-a51f-5afdca70859e'),('0affe284-a526-4cad-a52e-141b60b48a79',3,'...','2023-02-22, 00:47:04','0ba36696-aa9b-4bf2-8966-040188f970b8','6d839207-9e08-4b02-9253-a28ab68455c2'),('104ae56f-332c-4d27-9528-7786f6ff38d3',4,'...','2023-02-22, 00:47:04','1e3b3c6a-2c02-437f-91c7-83337e5bf099','7d5453d7-6cba-4882-9c20-19c74306007b'),('293e6bca-a7d0-4c95-8662-4ec98720dd37',4,'...','2023-02-22, 00:47:04','8a583bc1-f8fb-473d-8bca-d09950ed84f3','03fab21b-30b4-4fbc-a51f-5afdca70859e'),('9fd93ac1-fe5b-477c-97a9-fe29cfed69b0',5,'...','2023-02-22, 00:47:04','07cf8b53-696b-4be4-8585-a6b6a40153b2','03fab21b-30b4-4fbc-a51f-5afdca70859e'),('bb45dcc1-37e9-45e8-8ab8-94e2e8cac97b',3,'...','2023-02-22, 00:47:04','0ba36696-aa9b-4bf2-8966-040188f970b8','7d5453d7-6cba-4882-9c20-19c74306007b');
/*!40000 ALTER TABLE `movies_rating_and_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_show_actor_actress`
--

DROP TABLE IF EXISTS `tv_show_actor_actress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tv_show_actor_actress` (
  `id` varchar(50) NOT NULL,
  `tv_show_id` varchar(50) NOT NULL,
  `actor_actress_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tv_show_actor_actress_uc` (`tv_show_id`,`actor_actress_id`),
  KEY `actor_actress_id` (`actor_actress_id`),
  CONSTRAINT `tv_show_actor_actress_ibfk_1` FOREIGN KEY (`tv_show_id`) REFERENCES `tv_shows_and_series` (`id`),
  CONSTRAINT `tv_show_actor_actress_ibfk_2` FOREIGN KEY (`actor_actress_id`) REFERENCES `actors_actresses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_show_actor_actress`
--

LOCK TABLES `tv_show_actor_actress` WRITE;
/*!40000 ALTER TABLE `tv_show_actor_actress` DISABLE KEYS */;
INSERT INTO `tv_show_actor_actress` VALUES ('3183fd34-29e4-4c8d-a785-24da9f1a2df4','96b98bcd-b890-474c-aa4c-a30955860fe1','40d6b1b5-0dbb-4a3e-bbf1-37efc9f2d783'),('9ffacfff-7dbb-4ab9-b288-af1912938e0a','96b98bcd-b890-474c-aa4c-a30955860fe1','707f853b-f040-42b1-9113-d5aea422de58'),('4f02fa5b-8049-42aa-96ea-d435e7d78f9e','d04c70cc-8ddb-4117-8a69-99ab1f73a830','170b5287-1bf6-437f-a73c-bdafbb2ab9ba'),('6733de90-67a1-416e-a27e-7b4afae0ce5e','d04c70cc-8ddb-4117-8a69-99ab1f73a830','2060035a-b077-4105-b8a3-814177b3fdd0'),('a71b11e0-0f51-4f54-bb64-21bc8216b6d8','d04c70cc-8ddb-4117-8a69-99ab1f73a830','707f853b-f040-42b1-9113-d5aea422de58');
/*!40000 ALTER TABLE `tv_show_actor_actress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_show_award`
--

DROP TABLE IF EXISTS `tv_show_award`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tv_show_award` (
  `id` varchar(50) NOT NULL,
  `tv_show_id` varchar(50) NOT NULL,
  `award_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tv_show_award_uc` (`tv_show_id`,`award_id`),
  KEY `award_id` (`award_id`),
  CONSTRAINT `tv_show_award_ibfk_1` FOREIGN KEY (`tv_show_id`) REFERENCES `tv_shows_and_series` (`id`),
  CONSTRAINT `tv_show_award_ibfk_2` FOREIGN KEY (`award_id`) REFERENCES `awards` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_show_award`
--

LOCK TABLES `tv_show_award` WRITE;
/*!40000 ALTER TABLE `tv_show_award` DISABLE KEYS */;
INSERT INTO `tv_show_award` VALUES ('bd57828f-787b-4fd5-bf4e-3eead569d4f4','bc7f4b1d-46dd-4f64-a6e2-ea73c1487915','cc918aa1-df1d-46a1-a022-0f5f0477f09a'),('57ff8383-bb43-4808-93f3-fc6af6c93365','d04c70cc-8ddb-4117-8a69-99ab1f73a830','200811b0-15db-495b-b5e0-1c41372c9673'),('93aa8d77-dcf3-4a68-aebf-b64a6ad6cda7','d04c70cc-8ddb-4117-8a69-99ab1f73a830','cc918aa1-df1d-46a1-a022-0f5f0477f09a');
/*!40000 ALTER TABLE `tv_show_award` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_shows_and_series`
--

DROP TABLE IF EXISTS `tv_shows_and_series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tv_shows_and_series` (
  `id` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `plot` varchar(100) NOT NULL,
  `release_year` varchar(4) NOT NULL,
  `creator` varchar(50) NOT NULL,
  `seasons` int NOT NULL,
  `episodes` int NOT NULL,
  `episode_duration` int NOT NULL,
  `language_name` varchar(30) DEFAULT NULL,
  `genre_category` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `language_name` (`language_name`),
  KEY `genre_category` (`genre_category`),
  CONSTRAINT `tv_shows_and_series_ibfk_1` FOREIGN KEY (`language_name`) REFERENCES `languages` (`name`),
  CONSTRAINT `tv_shows_and_series_ibfk_2` FOREIGN KEY (`genre_category`) REFERENCES `genres` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_shows_and_series`
--

LOCK TABLES `tv_shows_and_series` WRITE;
/*!40000 ALTER TABLE `tv_shows_and_series` DISABLE KEYS */;
INSERT INTO `tv_shows_and_series` VALUES ('96b98bcd-b890-474c-aa4c-a30955860fe1','Big bang theory','...','2006','Chuck Lorre',12,22,23,'English','Comedy'),('bc7f4b1d-46dd-4f64-a6e2-ea73c1487915','Friends','...','1991','David Craine',10,22,22,'English','Comedy'),('d04c70cc-8ddb-4117-8a69-99ab1f73a830','Two and a half men','...','2002','Chuck Lorre',12,21,21,'English','Comedy');
/*!40000 ALTER TABLE `tv_shows_and_series` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_shows_rating_and_review`
--

DROP TABLE IF EXISTS `tv_shows_rating_and_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tv_shows_rating_and_review` (
  `id` varchar(50) NOT NULL,
  `grade` int NOT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `comment_date` varchar(50) DEFAULT NULL,
  `tv_show_id` varchar(50) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tv_show_user_uc` (`tv_show_id`,`user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `tv_shows_rating_and_review_ibfk_1` FOREIGN KEY (`tv_show_id`) REFERENCES `tv_shows_and_series` (`id`),
  CONSTRAINT `tv_shows_rating_and_review_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_shows_rating_and_review`
--

LOCK TABLES `tv_shows_rating_and_review` WRITE;
/*!40000 ALTER TABLE `tv_shows_rating_and_review` DISABLE KEYS */;
INSERT INTO `tv_shows_rating_and_review` VALUES ('3e610e8d-da80-447d-a88d-841a637b089e',4,'...','2023-02-22, 00:47:04','bc7f4b1d-46dd-4f64-a6e2-ea73c1487915','03fab21b-30b4-4fbc-a51f-5afdca70859e'),('68e26467-bc2f-430d-8108-a9f9e06f4159',3,'...','2023-02-22, 00:47:04','d04c70cc-8ddb-4117-8a69-99ab1f73a830','7d5453d7-6cba-4882-9c20-19c74306007b'),('7110e0da-116e-4004-b9cf-cfdd8fadab12',4,'...','2023-02-22, 00:47:04','d04c70cc-8ddb-4117-8a69-99ab1f73a830','03fab21b-30b4-4fbc-a51f-5afdca70859e'),('9ae4aaf3-9176-440c-b08d-f064ffb88b17',4,'...','2023-02-22, 00:47:04','d04c70cc-8ddb-4117-8a69-99ab1f73a830','6d839207-9e08-4b02-9253-a28ab68455c2'),('a551b746-ab93-42ee-a197-4df251790b0c',5,'...','2023-02-22, 00:47:04','96b98bcd-b890-474c-aa4c-a30955860fe1','03fab21b-30b4-4fbc-a51f-5afdca70859e');
/*!40000 ALTER TABLE `tv_shows_rating_and_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `surname` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('03fab21b-30b4-4fbc-a51f-5afdca70859e','Dean','Smith','dsmith@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1,0),('373724b6-1daf-47af-86ea-7fe1ed1b883b','Jane','Doe','jdoe@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1,1),('6d839207-9e08-4b02-9253-a28ab68455c2','John','Smith','jsmith@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1,0),('7d5453d7-6cba-4882-9c20-19c74306007b','Sean','Smith','ssmith@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 17:26:03
