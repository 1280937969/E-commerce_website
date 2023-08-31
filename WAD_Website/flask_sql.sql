-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: flask_sql
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `cart_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `total_price` int DEFAULT NULL,
  PRIMARY KEY (`cart_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (1,1,NULL,NULL);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'women\'s clothing'),(2,'menswear'),(3,'cosmetics'),(4,'toy'),(5,'digital product'),(6,'snack');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `comment_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `item_id` int DEFAULT NULL,
  `comment_details` text,
  `name` text,
  `mark` int DEFAULT NULL,
  `comment_time` datetime DEFAULT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `user_id` (`user_id`),
  KEY `item_id` (`item_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `category_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `cart_id` int DEFAULT NULL,
  `order_id` int DEFAULT NULL,
  `item_name` varchar(20) NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `item_details` varchar(255) DEFAULT NULL,
  `price` float NOT NULL,
  `duration` varchar(255) DEFAULT NULL,
  `discount_limit` float DEFAULT NULL,
  `liked_quantity` int DEFAULT NULL,
  `disliked_quantity` int DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  KEY `category_id` (`category_id`),
  KEY `user_id` (`user_id`),
  KEY `cart_id` (`cart_id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `item_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`),
  CONSTRAINT `item_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `item_ibfk_3` FOREIGN KEY (`cart_id`) REFERENCES `cart` (`cart_id`),
  CONSTRAINT `item_ibfk_4` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,2,NULL,NULL,NULL,'Trousers','../static/picture/menswear5.jpg','china','Black trousers',96.2,'2023/5/19',0.3,16,0),(2,5,NULL,NULL,NULL,'Phone','../static/picture/digital product2.jpg','USA','Huawei Mobile phone',100,'2023/5/20',0.3,20,0),(3,2,NULL,NULL,NULL,'T-shirt','../static/picture/menswear2.jpg','USA','Black T-shirt',120,'2023/5/20',0.9,3,0),(4,4,NULL,NULL,NULL,'Bird toys','../static/picture/toy1.jpg','USA','Cute Little Bird Toys',200,'2023/5/30',0.4,100,0),(5,4,NULL,NULL,NULL,'Little Bear Toys','../static/picture/toy.jpg','china','Cute little bear toy',180,'2023/5/20',1,19,0),(6,3,NULL,NULL,NULL,'face cream','../static/picture/cosmetics3.jpg','UK','L\'oreal',400,'2023/5/30',1,80,0),(7,1,NULL,NULL,NULL,'Women\'s skirt','../static/picture/women\'s wear3.jpg','UK','A beautiful skirt',130,'2023/5/30',0.5,80,0),(8,1,NULL,NULL,NULL,'Dress','../static/picture/women\'s wear1.jpg','UK','Cheap skirt',80,'2023/5/30',0.9,80,0),(9,6,NULL,NULL,NULL,'Cookie','../static/picture/snack2.jpg','UK','delicious',80,'2023/5/30',0.9,80,0);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `message_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `item_id` int DEFAULT NULL,
  `recipient` int DEFAULT NULL,
  `content` text,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`message_id`),
  KEY `user_id` (`user_id`),
  KEY `item_id` (`item_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `message_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,NULL,NULL,1,'Welcome to the e-commerce website!','2023-05-21 16:32:47');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `cart_id` int DEFAULT NULL,
  `total_price` float DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `user_id` (`user_id`),
  KEY `cart_id` (`cart_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`cart_id`) REFERENCES `cart` (`cart_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT NULL,
  `email` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'user','gz@qq.com','guozhe998',NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_item_interaction`
--

DROP TABLE IF EXISTS `user_item_interaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_item_interaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `item_id` int DEFAULT NULL,
  `liked` tinyint(1) DEFAULT NULL,
  `disliked` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `item_id` (`item_id`),
  CONSTRAINT `user_item_interaction_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `user_item_interaction_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_item_interaction`
--

LOCK TABLES `user_item_interaction` WRITE;
/*!40000 ALTER TABLE `user_item_interaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_item_interaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'flask_sql'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-21 16:38:23
