-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: hotel_reservasi
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `fasilitas`
--

DROP TABLE IF EXISTS `fasilitas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fasilitas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_fasilitas` varchar(100) DEFAULT NULL,
  `deskripsi` text,
  `gambar_fasilitas` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fasilitas`
--

LOCK TABLES `fasilitas` WRITE;
/*!40000 ALTER TABLE `fasilitas` DISABLE KEYS */;
INSERT INTO `fasilitas` VALUES (1,'Kolam Renang','Kolam renang luas dengan pemandangan kota dan area santai di sekelilingnya. Tersedia kursi santai dan layanan handuk gratis.','kolam_renang.png'),(2,'Restoran','Restoran eksklusif dengan pilihan menu lokal dan internasional, buka dari pagi hingga malam.','restoran.png'),(3,'Pusat Kebugaran','Pusat kebugaran lengkap dengan alat modern, terbuka 24 jam untuk tamu hotel.','gym.png'),(4,'Spa & Sauna','Layanan spa profesional dan sauna yang nyaman untuk relaksasi dan perawatan tubuh.','spa_sauna.png'),(5,'Ruang Rapat','Ruang rapat lengkap dengan proyektor, AC, dan koneksi Wi-Fi untuk keperluan bisnis.','ruang_rapat.png'),(6,'Area Bermain Anak','Area bermain indoor dan outdoor yang aman dan menyenangkan untuk anak-anak.','playground.png'),(7,'Layanan Antar-Jemput','Layanan antar-jemput bandara gratis dengan mobil eksklusif hotel.','shuttle.png'),(8,'Wi-Fi Gratis','Wi-Fi kecepatan tinggi tersedia di seluruh area hotel tanpa biaya tambahan.','wifi.png'),(9,'Parkir Luas','Area parkir luas dan aman, tersedia untuk tamu tanpa biaya tambahan.','parkir.png'),(10,'Layanan Kamar 24 Jam','Layanan kamar tersedia 24 jam dengan menu makanan dan minuman lengkap.','room_service.png');
/*!40000 ALTER TABLE `fasilitas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kamar`
--

DROP TABLE IF EXISTS `kamar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kamar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nomor_kamar` varchar(10) DEFAULT NULL,
  `tipe_kamar` varchar(100) DEFAULT NULL,
  `gambar_kamar` varchar(255) DEFAULT NULL,
  `deskripsi` text,
  `harga` decimal(10,2) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kamar`
--

LOCK TABLES `kamar` WRITE;
/*!40000 ALTER TABLE `kamar` DISABLE KEYS */;
INSERT INTO `kamar` VALUES (1,'101','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(2,'102','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(3,'103','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'terisi'),(4,'104','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(5,'105','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(6,'106','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'terisi'),(7,'107','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(8,'108','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(9,'109','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(10,'110','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'terisi'),(11,'111','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(12,'112','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(13,'113','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(14,'114','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(15,'115','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'terisi'),(16,'116','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(17,'117','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(18,'118','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(19,'119','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(20,'120','Standard','kamar_standard.png','Kamar Standard cocok untuk 2 orang, dilengkapi AC dan kamar mandi dalam.',300000.00,'tersedia'),(21,'201','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(22,'202','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(23,'203','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'terisi'),(24,'204','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(25,'205','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(26,'206','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(27,'207','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(28,'208','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(29,'209','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(30,'210','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'terisi'),(31,'211','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(32,'212','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(33,'213','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(34,'214','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'terisi'),(35,'215','Deluxe','kamar_deluxe.png','Kamar Deluxe luas untuk 3 orang, tersedia TV, AC, dan balkon pribadi.',450000.00,'tersedia'),(36,'301','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(37,'302','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(38,'303','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'terisi'),(39,'304','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(40,'305','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(41,'306','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(42,'307','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(43,'308','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(44,'309','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(45,'310','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(46,'311','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(47,'312','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'terisi'),(48,'313','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(49,'314','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia'),(50,'315','Suite','kamar_suite.png','Suite eksklusif untuk 4 orang dengan ruang tamu, bathtub, dan minibar.',700000.00,'tersedia');
/*!40000 ALTER TABLE `kamar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservasi`
--

DROP TABLE IF EXISTS `reservasi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservasi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `id_kamar` int NOT NULL,
  `nomor_kamar` int DEFAULT NULL,
  `tanggal_checkin` date DEFAULT NULL,
  `tanggal_checkout` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_user` (`id_user`),
  KEY `id_kamar` (`id_kamar`),
  CONSTRAINT `reservasi_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`),
  CONSTRAINT `reservasi_ibfk_2` FOREIGN KEY (`id_kamar`) REFERENCES `kamar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservasi`
--

LOCK TABLES `reservasi` WRITE;
/*!40000 ALTER TABLE `reservasi` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservasi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) DEFAULT NULL,
  `no_telepon` varchar(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
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

-- Dump completed on 2025-06-25 14:22:17
