-- Host: 127.0.0.1    Database: securityagency
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_SYSTEM=@@CHARACTER_SET_SYSTEM */;
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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_customuser'),(22,'Can change user',6,'change_customuser'),(23,'Can delete user',6,'delete_customuser'),(24,'Can view user',6,'view_customuser'),(25,'Can add agency information',7,'add_agencyinformation'),(26,'Can change agency information',7,'change_agencyinformation'),(27,'Can delete agency information',7,'delete_agencyinformation'),(28,'Can view agency information',7,'view_agencyinformation'),(29,'Can add contract',8,'add_contract'),(30,'Can change contract',8,'change_contract'),(31,'Can delete contract',8,'delete_contract'),(32,'Can view contract',8,'view_contract'),(33,'Can add ddo',9,'add_ddo'),(34,'Can change ddo',9,'change_ddo'),(35,'Can delete ddo',9,'delete_ddo'),(36,'Can view ddo',9,'view_ddo'),(37,'Can add designation',10,'add_designation'),(38,'Can change designation',10,'change_designation'),(39,'Can delete designation',10,'delete_designation'),(40,'Can view designation',10,'view_designation'),(41,'Can add firearm',11,'add_firearm'),(42,'Can change firearm',11,'change_firearm'),(43,'Can delete firearm',11,'delete_firearm'),(44,'Can view firearm',11,'view_firearm'),(45,'Can add guard',12,'add_guard'),(46,'Can change guard',12,'change_guard'),(47,'Can delete guard',12,'delete_guard'),(48,'Can view guard',12,'view_guard'),(49,'Can add instruction',13,'add_instruction'),(50,'Can change instruction',13,'change_instruction'),(51,'Can delete instruction',13,'delete_instruction'),(52,'Can view instruction',13,'view_instruction'),(53,'Can add location',14,'add_location'),(54,'Can change location',14,'change_location'),(55,'Can delete location',14,'delete_location'),(56,'Can view location',14,'view_location'),(57,'Can add shift',15,'add_shift'),(58,'Can change shift',15,'change_shift'),(59,'Can delete shift',15,'delete_shift'),(60,'Can view shift',15,'view_shift'),(61,'Can add post',16,'add_post'),(62,'Can change post',16,'change_post'),(63,'Can delete post',16,'delete_post'),(64,'Can view post',16,'view_post'),(65,'Can add firearm assignment',17,'add_firearmassignment'),(66,'Can change firearm assignment',17,'change_firearmassignment'),(67,'Can delete firearm assignment',17,'delete_firearmassignment'),(68,'Can view firearm assignment',17,'view_firearmassignment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_security_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_security_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `security_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-08-09 08:55:29.217000','1','Polytechnic University of the Philippines',3,'',14,1),(2,'2022-08-09 09:00:23.592000','2','Marc Stephen Gabres',3,'',6,1),(3,'2022-08-09 09:00:31.228000','2','Monday - 20:00:00',3,'',15,1),(4,'2022-08-09 09:00:31.230000','1','Monday - 08:00:00',3,'',15,1),(5,'2022-08-09 09:00:31.231000','4','Tuesday - 20:00:00',3,'',15,1),(6,'2022-08-09 09:00:31.232000','3','Tuesday - 08:00:00',3,'',15,1),(7,'2022-08-09 09:00:31.233000','6','Wednesday - 20:00:00',3,'',15,1),(8,'2022-08-09 09:00:31.235000','5','Wednesday - 08:00:00',3,'',15,1),(9,'2022-08-09 09:00:31.237000','8','Thursday - 20:00:00',3,'',15,1),(10,'2022-08-09 09:00:31.238000','7','Thursday - 08:00:00',3,'',15,1),(11,'2022-08-09 09:00:31.239000','10','Friday - 20:00:00',3,'',15,1),(12,'2022-08-09 09:00:31.240000','9','Friday - 08:00:00',3,'',15,1),(13,'2022-08-09 09:00:31.241000','12','Saturday - 20:00:00',3,'',15,1),(14,'2022-08-09 09:00:31.242000','11','Saturday - 08:00:00',3,'',15,1),(15,'2022-08-09 09:00:31.244000','14','Sunday - 20:00:00',3,'',15,1),(16,'2022-08-09 09:00:31.246000','13','Sunday - 08:00:00',3,'',15,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(7,'security','agencyinformation'),(8,'security','contract'),(6,'security','customuser'),(9,'security','ddo'),(10,'security','designation'),(11,'security','firearm'),(17,'security','firearmassignment'),(12,'security','guard'),(13,'security','instruction'),(14,'security','location'),(16,'security','post'),(15,'security','shift'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-08-10 08:04:49.041542'),(2,'contenttypes','0002_remove_content_type_name','2022-08-10 08:04:49.097394'),(3,'auth','0001_initial','2022-08-10 08:04:49.328443'),(4,'auth','0002_alter_permission_name_max_length','2022-08-10 08:04:49.381755'),(5,'auth','0003_alter_user_email_max_length','2022-08-10 08:04:49.389755'),(6,'auth','0004_alter_user_username_opts','2022-08-10 08:04:49.396758'),(7,'auth','0005_alter_user_last_login_null','2022-08-10 08:04:49.407760'),(8,'auth','0006_require_contenttypes_0002','2022-08-10 08:04:49.412762'),(9,'auth','0007_alter_validators_add_error_messages','2022-08-10 08:04:49.420764'),(10,'auth','0008_alter_user_username_max_length','2022-08-10 08:04:49.430766'),(11,'auth','0009_alter_user_last_name_max_length','2022-08-10 08:04:49.445770'),(12,'auth','0010_alter_group_name_max_length','2022-08-10 08:04:49.464773'),(13,'auth','0011_update_proxy_permissions','2022-08-10 08:04:49.473776'),(14,'auth','0012_alter_user_first_name_max_length','2022-08-10 08:04:49.480777'),(15,'security','0001_initial','2022-08-10 08:04:51.182498'),(16,'admin','0001_initial','2022-08-10 08:04:51.306533'),(17,'admin','0002_logentry_remove_auto_add','2022-08-10 08:04:51.320541'),(18,'admin','0003_logentry_add_action_flag_choices','2022-08-10 08:04:51.333543'),(19,'security','0002_alter_nbi_owner','2022-08-10 08:04:51.448478'),(20,'security','0003_delete_duration','2022-08-10 08:04:51.462481'),(21,'security','0004_remove_contract_nbi','2022-08-10 08:04:51.544430'),(22,'security','0005_delete_nbi','2022-08-10 08:04:51.565420'),(23,'security','0006_nbi','2022-08-10 08:04:51.648660'),(24,'security','0007_rename_nbi_clearance_id_nbi_clearance_id','2022-08-10 08:04:51.670646'),(25,'security','0008_rename_clearance_id_nbi_nbi_clearance_id','2022-08-10 08:04:51.690650'),(26,'security','0009_alter_nbi_nbi_clearance_id','2022-08-10 08:04:51.736205'),(27,'security','0010_alter_contract_options_contract_issued_date_and_more','2022-08-10 08:04:51.797121'),(28,'security','0011_alter_contract_issued_date','2022-08-10 08:04:51.816125'),(29,'security','0012_delete_license_guard_lesp_issued_date_delete_nbi','2022-08-10 08:04:51.859572'),(30,'security','0013_guard_nbi_issued_date_alter_guard_nbi_clearance_id','2022-08-10 08:04:51.882449'),(31,'security','0014_customuser_organization_address_and_more','2022-08-10 08:04:51.973470'),(32,'security','0015_contract_daily_wage_alter_contract_months_and_more','2022-08-10 08:04:52.091033'),(33,'security','0016_jobrequest','2022-08-10 08:04:52.112036'),(34,'security','0017_jobrequest_is_approved_jobrequest_months_and_more','2022-08-10 08:04:52.158047'),(35,'security','0018_jobrequest_link','2022-08-10 08:04:52.183053'),(36,'security','0019_alter_jobrequest_daily_wage','2022-08-10 08:04:52.228062'),(37,'security','0020_delete_jobrequest','2022-08-10 08:04:52.246068'),(38,'security','0021_customuser_sex','2022-08-10 08:04:52.313082'),(39,'security','0022_customuser_position','2022-08-10 08:04:52.375097'),(40,'security','0023_alter_customuser_position','2022-08-10 08:04:52.388099'),(41,'security','0024_jobrequest','2022-08-10 08:04:52.477120'),(42,'security','0025_delete_jobrequest','2022-08-10 08:04:52.494364'),(43,'security','0026_remove_contract_is_approved_contract_status','2022-08-10 08:04:52.561379'),(44,'security','0027_remove_customuser_sss_alter_contract_status','2022-08-10 08:04:52.613390'),(45,'sessions','0001_initial','2022-08-10 08:04:52.658752');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('7bl0zp2ew3m7u4r3yt56p36ub3esddk5','.eJxVjDsOwjAQBe_iGln-rINDSZ8zRLveBQeQLcVJhbg7iZQC2jcz761GXJc8rk3mcWJ1UV6dfjfC9JSyA35guVedalnmifSu6IM2PVSW1_Vw_w4ytrzV0Ti4AXDvBG3qyQozBqZg2EG3oZDOVjoXrItgQvQ2MXn2hIDiGdXnC-MnOBY:1oLL7o:tBvJ5Ngf6xZsrDZqlDoQYysZ0vO_vCrC8k59mSxfvjs','2022-08-23 09:02:08.458000'),('tbrjz3dh5hwhubxfejsy9v0a5ztdlnmt','.eJxVjEEOwiAQRe_C2pB2ShnGpXvPQIYBpGpoUtqV8e7apAvd_vfefynP21r81tLip6jOqlen3y2wPFLdQbxzvc1a5rouU9C7og_a9HWO6Xk53L-Dwq186xAZOwCCESUzB3GcOUNnRrJIKCguIfQAKHYw1nFgKySSsqFMYVDvD_WcOHI:1oLKsl:sCrIwqZhqp-5AisW-3YyFWY_N5z-M4CVlyq_Vqd0DKw','2022-08-23 08:46:35.023000'),('zbeppim2dtj3isunj5z9hkb6qyjd9vh4','.eJxVjMEOwiAQRP-FsyFgFxCP3vsNZBcWqRpISnsy_rtt0oPeZubNzFsEXJcS1s5zmJK4ChCn34wwPrnuID2w3puMrS7zRHKvyIN2ObbEr9vR_Tso2Mu2VhaZjGMi5cAhIVqIJtvBbBqivei8W_QKfE46abDJZO3zOTseAMXnCwlMOMA:1oLmju:ng_b34_Mtr205_tkZ4qqvJLVVgk2WmUql4cwEFDTRzI','2022-08-24 14:31:18.947382');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_agencyinformation`
--

DROP TABLE IF EXISTS `security_agencyinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_agencyinformation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fa_validity` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_agencyinformation`
--

LOCK TABLES `security_agencyinformation` WRITE;
/*!40000 ALTER TABLE `security_agencyinformation` DISABLE KEYS */;
/*!40000 ALTER TABLE `security_agencyinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_contract`
--

DROP TABLE IF EXISTS `security_contract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_contract` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start_date` date DEFAULT NULL,
  `years` int DEFAULT NULL,
  `months` int DEFAULT NULL,
  `is_finished` tinyint(1) NOT NULL,
  `link` varchar(150) DEFAULT NULL,
  `client_id` bigint DEFAULT NULL,
  `issued_date` date NOT NULL,
  `daily_wage` double DEFAULT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `security_contract_client_id_befa4c95_fk_security_customuser_id` (`client_id`),
  CONSTRAINT `security_contract_client_id_befa4c95_fk_security_customuser_id` FOREIGN KEY (`client_id`) REFERENCES `security_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_contract`
--

LOCK TABLES `security_contract` WRITE;
/*!40000 ALTER TABLE `security_contract` DISABLE KEYS */;
INSERT INTO `security_contract` VALUES (2,'2022-08-01',1,NULL,1,'/contract/2/full',3,'2022-08-09',450,3),(3,'2022-08-20',6,NULL,1,'/contract/3/full',5,'2022-08-10',502,3),(4,NULL,NULL,NULL,0,'/contract/4/locations/',5,'2022-08-10',NULL,1);
/*!40000 ALTER TABLE `security_contract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_customuser`
--

DROP TABLE IF EXISTS `security_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone_number` varchar(11) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `organization_address` varchar(150) DEFAULT NULL,
  `organization_name` varchar(150) DEFAULT NULL,
  `sex` varchar(1) NOT NULL,
  `position` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_customuser`
--

LOCK TABLES `security_customuser` WRITE;
/*!40000 ALTER TABLE `security_customuser` DISABLE KEYS */;
INSERT INTO `security_customuser` VALUES (1,'pbkdf2_sha256$320000$jNkYTCAtUhskZlUgD11Wlm$fbdasqXYUfvxPn3feEzb+RyLraiSH0+kuN809vVRnYc=','2022-08-09 08:47:59.929000',1,'VincentVollachia','','','',1,1,'2022-08-09 08:46:30.524000',NULL,NULL,NULL,NULL,'M',NULL),(3,'pbkdf2_sha256$320000$IrEib9gTQ4npRS7LOdMPiw$EZahZUrHsdgP3M7tH6kzAnqqXMtXVHgZ+XhhRmXcPGE=','2022-08-10 14:18:04.694102',0,'RikuDola','Marc Stephen','Gabres','arclight04@gmail.com',0,1,'2022-08-09 09:01:58.848000','09202750407','2001-08-01','1016 Anonas, Sta. Mesa, Maynila, Kalakhang Maynila','Polytechnic University of the Philippines','M','President'),(4,'pbkdf2_sha256$320000$mHMsLUXV0jGPRgqQIzIImt$ntykdNcNgb+PtiakK9I9EWGrWGdyaVS18oXoXixe2bU=','2022-08-10 14:31:18.945381',1,'NashAdmin','','','pqndaemonium@gmail.com',1,1,'2022-08-10 08:12:21.284565',NULL,NULL,NULL,NULL,'M',NULL),(5,'pbkdf2_sha256$320000$A2LtNkGeucJTBvgZmWw6Er$bf3pn5/DNCenKqD7O1VCBP6+s2ill1+Mx7TgxbN84SQ=','2022-08-10 14:28:39.916834',0,'NashClient','Jericko Nash','Bautista','jnpbautista@gmail.com',0,1,'2022-08-10 08:23:55.556698','09266156010','2002-04-29','11 A 1 Hope St., Teresa Village','Teresa Village Home Owners','M','Village Representative');
/*!40000 ALTER TABLE `security_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_customuser_groups`
--

DROP TABLE IF EXISTS `security_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `security_customuser_groups_customuser_id_group_id_6bf43db6_uniq` (`customuser_id`,`group_id`),
  KEY `security_customuser_groups_group_id_fbf25be6_fk_auth_group_id` (`group_id`),
  CONSTRAINT `security_customuser__customuser_id_1f07dbb3_fk_security_` FOREIGN KEY (`customuser_id`) REFERENCES `security_customuser` (`id`),
  CONSTRAINT `security_customuser_groups_group_id_fbf25be6_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_customuser_groups`
--

LOCK TABLES `security_customuser_groups` WRITE;
/*!40000 ALTER TABLE `security_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `security_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_customuser_user_permissions`
--

DROP TABLE IF EXISTS `security_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `security_customuser_user_customuser_id_permission_3fb08146_uniq` (`customuser_id`,`permission_id`),
  KEY `security_customuser__permission_id_8ec7431e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `security_customuser__customuser_id_a400f923_fk_security_` FOREIGN KEY (`customuser_id`) REFERENCES `security_customuser` (`id`),
  CONSTRAINT `security_customuser__permission_id_8ec7431e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_customuser_user_permissions`
--

LOCK TABLES `security_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `security_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `security_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_ddo`
--

DROP TABLE IF EXISTS `security_ddo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_ddo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_issued` datetime(6) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `operations_manager` varchar(50) NOT NULL,
  `validity` int NOT NULL,
  `link` varchar(250) DEFAULT NULL,
  `is_finished` tinyint(1) NOT NULL,
  `location_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `security_ddo_location_id_1b80e467_fk_security_location_id` (`location_id`),
  CONSTRAINT `security_ddo_location_id_1b80e467_fk_security_location_id` FOREIGN KEY (`location_id`) REFERENCES `security_location` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_ddo`
--

LOCK TABLES `security_ddo` WRITE;
/*!40000 ALTER TABLE `security_ddo` DISABLE KEYS */;
INSERT INTO `security_ddo` VALUES (2,'2022-08-10 08:14:17.153403','2022-08-06','Riku Dola',30,'/ddo/2/detail/',1,3),(4,'2022-08-10 14:32:00.194277',NULL,'Riku Dola',0,'/ddo/4/post/2/initial/',0,3),(5,'2022-08-10 14:32:06.638118',NULL,'Riku Dola',0,'/ddo/5/post/3/initial/',0,4),(6,'2022-08-10 14:32:28.918400','2022-08-31','Riku Dola',30,'/ddo/6/post/4/assign/',0,4);
/*!40000 ALTER TABLE `security_ddo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_designation`
--

DROP TABLE IF EXISTS `security_designation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_designation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `designation_type` int NOT NULL,
  `day_off_id` bigint DEFAULT NULL,
  `ddo_id` bigint DEFAULT NULL,
  `guard_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `security_designation_day_off_id_a74a7e74_fk_security_` (`day_off_id`),
  KEY `security_designation_ddo_id_94f883d4_fk_security_ddo_id` (`ddo_id`),
  KEY `security_designation_guard_id_59df5291_fk_security_guard_id` (`guard_id`),
  CONSTRAINT `security_designation_day_off_id_a74a7e74_fk_security_` FOREIGN KEY (`day_off_id`) REFERENCES `security_instruction` (`id`),
  CONSTRAINT `security_designation_ddo_id_94f883d4_fk_security_ddo_id` FOREIGN KEY (`ddo_id`) REFERENCES `security_ddo` (`id`),
  CONSTRAINT `security_designation_guard_id_59df5291_fk_security_guard_id` FOREIGN KEY (`guard_id`) REFERENCES `security_guard` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_designation`
--

LOCK TABLES `security_designation` WRITE;
/*!40000 ALTER TABLE `security_designation` DISABLE KEYS */;
INSERT INTO `security_designation` VALUES (1,1,15,2,45),(2,1,18,2,34),(3,1,19,2,35),(4,1,24,2,12),(5,2,NULL,2,13);
/*!40000 ALTER TABLE `security_designation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_firearm`
--

DROP TABLE IF EXISTS `security_firearm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_firearm` (
  `serial_number` varchar(20) NOT NULL,
  `make` varchar(20) NOT NULL,
  `kind` int NOT NULL,
  `caliber` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`serial_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_firearm`
--

LOCK TABLES `security_firearm` WRITE;
/*!40000 ALTER TABLE `security_firearm` DISABLE KEYS */;
/*!40000 ALTER TABLE `security_firearm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_firearmassignment`
--

DROP TABLE IF EXISTS `security_firearmassignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_firearmassignment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ddo_id` bigint DEFAULT NULL,
  `post_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `security_firearmassignment_ddo_id_f6d63ecd_fk_security_ddo_id` (`ddo_id`),
  KEY `security_firearmassignment_post_id_c22be74c_fk_security_post_id` (`post_id`),
  CONSTRAINT `security_firearmassignment_ddo_id_f6d63ecd_fk_security_ddo_id` FOREIGN KEY (`ddo_id`) REFERENCES `security_ddo` (`id`),
  CONSTRAINT `security_firearmassignment_post_id_c22be74c_fk_security_post_id` FOREIGN KEY (`post_id`) REFERENCES `security_post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_firearmassignment`
--

LOCK TABLES `security_firearmassignment` WRITE;
/*!40000 ALTER TABLE `security_firearmassignment` DISABLE KEYS */;
INSERT INTO `security_firearmassignment` VALUES (1,5,3),(2,6,4);
/*!40000 ALTER TABLE `security_firearmassignment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_firearmassignment_firearms`
--

DROP TABLE IF EXISTS `security_firearmassignment_firearms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_firearmassignment_firearms` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firearmassignment_id` bigint NOT NULL,
  `firearm_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `security_firearmassignme_firearmassignment_id_fir_30ef493e_uniq` (`firearmassignment_id`,`firearm_id`),
  KEY `security_firearmassi_firearm_id_b13d6202_fk_security_` (`firearm_id`),
  CONSTRAINT `security_firearmassi_firearm_id_b13d6202_fk_security_` FOREIGN KEY (`firearm_id`) REFERENCES `security_firearm` (`serial_number`),
  CONSTRAINT `security_firearmassi_firearmassignment_id_c80f9a4b_fk_security_` FOREIGN KEY (`firearmassignment_id`) REFERENCES `security_firearmassignment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_firearmassignment_firearms`
--

LOCK TABLES `security_firearmassignment_firearms` WRITE;
/*!40000 ALTER TABLE `security_firearmassignment_firearms` DISABLE KEYS */;
/*!40000 ALTER TABLE `security_firearmassignment_firearms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_guard`
--

DROP TABLE IF EXISTS `security_guard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_guard` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `sex` varchar(100) DEFAULT NULL,
  `residence_address` varchar(150) NOT NULL,
  `nbi_clearance_id` varchar(21) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `highest_education` int NOT NULL,
  `sss` varchar(14) DEFAULT NULL,
  `agency_affiliation` date DEFAULT NULL,
  `lesp_issued_date` date DEFAULT NULL,
  `nbi_issued_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_guard`
--

LOCK TABLES `security_guard` WRITE;
/*!40000 ALTER TABLE `security_guard` DISABLE KEYS */;
INSERT INTO `security_guard` VALUES (12,'Theresia','Astrea','2001-01-01','F','2213-B F Zobel 1200  Makati City, Metro Manila','12345678901','09004357880',1,'12-3456789-0','2022-07-28','2022-08-09',NULL),(13,'Reinhardt','Astrea','2001-01-01','M','62 Old Samson Road  Quezon City, Metro Manila','12345678901','09942379923',1,'12-3456789-0','2022-07-28','2022-08-09',NULL),(14,'Julius','Euclius','2001-01-01','M','154 Shaw Boulevard Corner 29 de Agosto Street  Mandaluyong City, Metro Manila','12345678901','09917163917',1,'12-3456789-0','2022-07-28','2022-08-09',NULL),(15,'Mamiya','Takuji','2001-01-01','M','2921 Taft Avenue 1300  Pasay City, Metro Manila','12345678901','09467593691',1,'12-3456789-0','2022-07-28','2022-08-09',NULL),(16,'Crusch','Karsten','2001-01-01','F','2/F Building 12 Ccmc CompoundVeterans Center  Taguig City','12345678901','09593215700',1,'25-5664303-3','2022-07-28','2022-08-09',NULL),(17,'Yuuki','Minakami','2001-01-01','F','Dr A Santos Avenue 1700  Paranaque City','12345678901','09332193794',1,'52-8064963-3','2022-07-28','2022-08-09',NULL),(18,'Ash','Ketchum','2001-01-01','M','340 A. Amang Rodriguez Ave. Manggahan  Pasig City','12345678901','09902763875',1,'31-5524945-9','2022-07-28','2022-08-09',NULL),(19,'Childe','Tartaglia','2001-01-01','M','1129 Quirino Highway Kaligayahan Novaliches 1124  Quezon City','12345678901','09533291703',1,'58-1361043-7','2022-07-28','2022-08-09',NULL),(20,'Takuru','Miyashiro','2001-01-01','M','167 Biak-Na-Bato  Quezon City','12345678901','09791538238',2,'69-6030514-2','2022-07-28','2022-08-09',NULL),(21,'Juan','Dela Cruz','1991-04-01','M','114 Everlasting  Paranaque City','12345678901','09560416921',1,'43-0659314-7','2022-07-31','2022-08-09',NULL),(22,'Corbin','Isidro','1972-09-02','M','Congbalay Building 520 N. Lopez Avenue Sucat 1700  Paranaque City','12345678901','09262852546',1,'45-3216321-7','2021-10-19','2022-08-09',NULL),(23,'Isko','Smith','1998-11-17','M','673 BMI Avenue, Mandaluyong City','12345678901','09476602389',1,'41-3018522-3','2021-03-18','2022-08-09',NULL),(24,'Fermin','Rosario','1992-11-13','M','Suite 3903-3905 Discovery Center, 25 ADB Avenue, Ortigas Center  Pasig City','12345678901','09120768877',1,'37-7564323-7','2021-02-19','2022-08-09',NULL),(25,'Homobono','Pereira','1973-03-19','M','88 Luzon Avenue  Quezon City, Metro Manila','12345678901','09323038685',1,'49-2808331-5','2021-07-29','2022-08-09',NULL),(26,'Bagwis','Enriquez','1996-09-25','M','Vernida Cond Alfaro Street Salcedo Village 1200  Makati City, Metro Manila','12345678901','09905021617',1,'36-8457334-9','2021-06-21','2022-08-09',NULL),(27,'Gener','Baker','2000-07-07','M','Aguirre Building, 2211 Commonwealth Avenue, Capitol District  Quezon City, Metro Manila','12345678901','09434384509',1,'86-1650996-6','2021-01-14','2022-08-09',NULL),(28,'Honesto','Delos Reyes','1985-12-25','M','Sales And Marketing Office 960 Aurora Boulevard  Quezon City','12345678901','09604453823',1,'46-1054457-8','2021-02-01','2022-08-09',NULL),(29,'Huwan','Enriquez','1999-08-25','M','Aguirre Avenue Corner F. Ortigas Street, BF Homes  Paranaque City, Metro Manila','12345678901','09533023490',1,'62-1535830-6','2021-09-28','2022-08-09',NULL),(30,'Honesto','Guzman','1994-05-15','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'66-2837531-9','2021-07-24','2022-08-09',NULL),(31,'Benjie','Rodriguez','1993-09-05','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'32-4732293-4','2021-09-19','2022-08-09',NULL),(32,'Renz','Borja','1975-05-22','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'46-8609942-5','2021-12-26','2022-08-09',NULL),(33,'Igme','Velasco','1999-06-08','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'24-3069652-7','2021-11-14','2022-08-09',NULL),(34,'Fermin','Agustin','1999-09-02','M','1 Ligaya Street Corner A Bonifacio, Balintawak  Quezon City, Metro Manila','12345678901','09905095991',2,'95-1179769-5','2021-06-07','2022-08-09',NULL),(35,'Rosito','Alvarez','1992-03-15','M','22 Sct Tuazon 1100  Quezon City, Quezon City','12345678901','09139434613',1,'97-1757594-6','2021-04-16','2022-08-09',NULL),(36,'Crisanto','Fernando','1982-05-04','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'59-1639806-7','2021-01-23','2022-08-09',NULL),(37,'Igme','Ruan','2000-09-16','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'13-2053048-8','2021-07-30','2022-08-09',NULL),(38,'Marcus','Morgan','1977-07-08','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'80-2904904-5','2021-02-07','2022-08-09',NULL),(39,'Rizal','Soriano','1973-11-27','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'42-9749924-9','2021-09-16','2022-08-09',NULL),(40,'Rommel','Manuel','1981-02-07','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'51-5470947-2','2021-03-27','2022-08-09',NULL),(41,'Liberato','Pasion','1997-12-25','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'67-1835046-4','2021-01-08','2022-08-09',NULL),(42,'Sherwin','Zamora','1983-03-19','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'70-5706640-7','2021-10-08','2022-08-09',NULL),(43,'Christian','Miller','1995-12-04','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'84-3605984-6','2021-10-18','2022-08-09',NULL),(44,'Melchor','Ramos','1990-03-24','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'27-1151617-1','2021-12-02','2022-08-09',NULL),(45,'Edcel','Aguilar','1977-06-27','M','22a Grace Avenue, Grace Village, 1115  Quezon City, Metro Manila','12345678901','09736108612',2,'13-8871357-5','2021-01-25','2022-08-09',NULL),(46,'Erick','Ligaya','1981-11-11','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'49-8276720-4','2021-04-26','2022-08-09',NULL),(47,'Larry','Meija','1974-03-08','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'70-7040053-5','2021-10-01','2022-08-09',NULL),(48,'Romel','Reyes','1973-10-03','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'23-9749385-5','2021-12-23','2022-08-09',NULL),(49,'Ramil','Manalo','1994-06-30','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'31-6232801-4','2021-06-15','2022-08-09',NULL),(50,'Mark','De Leon','1982-08-27','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'82-4495878-2','2021-04-11','2022-08-09',NULL),(51,'Pacifico','Cunanan','1999-04-17','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'72-1282997-5','2021-09-10','2022-08-09',NULL),(52,'Joselito','Trinidad','1979-02-24','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'89-0396643-7','2021-03-28','2022-08-09',NULL),(53,'Rextopher','Hill','1991-08-23','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'71-2636482-6','2021-04-06','2022-08-09',NULL),(54,'Mario','Gutierrez','1999-11-19','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'59-5678391-3','2021-05-23','2022-08-09',NULL),(55,'Heherson','Manzano','1981-04-15','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'48-2351403-8','2021-07-11','2022-08-09',NULL),(56,'Capitan','Torres','1990-08-18','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'66-4052604-9','2021-07-31','2022-08-09',NULL),(57,'Rodel','Flores','1991-03-09','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'59-2824403-8','2021-09-21','2022-08-09',NULL),(58,'Rizaldo','Scott','1991-05-22','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'75-3090379-2','2021-02-28','2022-08-09',NULL),(59,'Fermin','Dsouza','1990-04-09','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'25-3724861-1','2021-12-16','2022-08-09',NULL),(60,'Jaydee','Mallari','1982-11-14','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'71-1833599-5','2021-09-21','2022-08-09',NULL),(61,'Melchor','Gabriel','1997-03-11','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'48-2921780-1','2021-03-06','2022-08-09',NULL),(62,'Rodel','Ocampo','1977-12-14','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'41-3864810-3','2021-08-04','2022-08-09',NULL),(63,'Jason','Miranda','1988-12-07','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'85-2691407-2','2021-07-21','2022-08-09',NULL),(64,'Rizalino','Simon','1997-04-01','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'98-8950449-8','2021-11-20','2022-08-09',NULL),(65,'Isagani','Reyes','2000-03-26','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'95-8430953-6','2021-09-08','2022-08-09',NULL),(66,'Andrew','Villanueva','1997-12-13','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'02-0131002-8','2021-11-28','2022-08-09',NULL),(67,'Blue','Magno','1972-10-21','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'27-7308616-7','2021-07-21','2022-08-09',NULL),(68,'Resituto','Gray','1997-05-29','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'48-1705988-5','2021-05-08','2022-08-09',NULL),(69,'Crisanto','Murphy','1988-07-21','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'81-2702905-5','2021-06-18','2022-08-09',NULL),(70,'Melchor','Reed','1975-02-05','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'16-3482240-3','2021-03-02','2022-08-09',NULL),(71,'Jay','Clark','1998-12-20','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'29-0057785-5','2021-04-05','2022-08-09',NULL),(72,'Arnel','Scott','1998-06-15','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'18-0997703-1','2021-04-08','2022-08-09',NULL),(73,'Ernesto','Navarro','1998-09-12','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'09-5271335-5','2021-11-23','2022-08-09',NULL),(74,'Joselito','Bartolome','1985-08-18','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09191297922',1,'46-3615890-5','2021-04-30','2022-08-09',NULL),(75,'Luzvimindo','Ruan','1980-07-14','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'96-7170118-1','2021-04-20','2022-08-09',NULL),(76,'Ignacio','Robredo','1978-07-27','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'60-2654035-7','2021-12-09','2022-08-09',NULL),(77,'Biktor','Magtanggol','1972-02-28','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'77-4665523-8','2021-12-28','2022-08-09',NULL),(78,'Cardo','Dalisay','1985-09-20','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'95-8673259-7','2021-03-13','2022-08-09',NULL),(79,'Rommel','Padua','1989-11-07','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'93-8613743-4','2021-12-05','2022-08-09',NULL),(80,'Brother','Martinez','1974-07-20','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'40-0266276-1','2021-05-07','2022-08-09',NULL),(81,'Benji','Cordero','1984-11-30','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'39-5183277-5','2021-05-20','2022-08-09',NULL),(82,'Ramil','Velasco','1979-07-28','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'66-8426554-6','2021-09-14','2022-08-09',NULL),(83,'Naruto','Uzumaki','1990-07-02','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'36-7052044-8','2021-10-17','2022-08-09',NULL),(84,'Rizalina','Fernandez','1997-05-30','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'49-6580775-6','2021-03-08','2022-08-09',NULL),(85,'Marilag','Ruan','1978-12-17','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'16-7050328-9','2021-05-25','2022-08-09',NULL),(86,'Flordeliza','Santiago','1976-07-25','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'74-4125056-9','2021-03-12','2022-08-09',NULL),(87,'Dalisaya','White','1995-07-04','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'14-4468442-3','2021-05-06','2022-08-09',NULL),(88,'Liwayway','Espiritu','1996-05-02','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'73-5261662-4','2021-05-24','2022-08-09',NULL),(89,'Charlita','Robinson','1992-12-11','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'53-2339986-3','2021-02-04','2022-08-09',NULL),(90,'Diwa','Stewart','1981-02-21','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'84-1742464-1','2021-02-10','2022-08-09',NULL),(91,'Irish','Sanchez','1986-09-10','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'03-7398000-7','2022-01-26','2022-08-09',NULL),(92,'Luntian','Harris','1972-11-27','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'88-8400089-2','2021-10-26','2022-08-09',NULL),(93,'Iska','Collins','1998-07-29','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'42-7977728-5','2021-01-20','2022-08-09',NULL),(94,'Sakura','Haruno','1993-02-08','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'93-3168047-6','2021-09-17','2022-08-09',NULL),(95,'Sasha','Blouse','1972-09-23','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'60-7643323-8','2021-08-26','2022-08-09',NULL),(96,'Cassie','Chio','1985-03-05','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'53-2300718-8','2021-10-26','2022-08-09',NULL),(97,'Matia','Sembrano','1986-11-28','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'78-1408341-2','2021-05-18','2022-08-09',NULL),(98,'Estefani','Ignacio','1984-06-04','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'81-4379815-7','2021-12-27','2022-08-09',NULL),(99,'Mirari','Dimayuga','1983-01-14','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'76-7625239-1','2021-08-14','2022-08-09',NULL),(100,'Luveina','Hontiveros','1993-05-09','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'05-0964746-4','2021-03-27','2022-08-09',NULL),(101,'Julina','Jimenez','1975-05-11','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'01-4048851-9','2021-07-30','2022-08-09',NULL),(102,'Gia','Despujol','1997-04-27','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'94-1699567-6','2021-04-09','2022-08-09',NULL),(103,'Marlina','Malapitan','1979-08-08','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'34-1866112-3','2021-12-24','2022-08-09',NULL),(104,'Brenda','Marcelo','1998-11-20','F','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'65-3649020-9','2021-09-30','2022-08-09',NULL),(105,'Shaniya','Asuncion','1986-09-24','F','38 Chicago Street Cubao 1100  Quezon City','12345678901','09844266746',1,'33-9195919-2','2021-11-12','2022-08-09',NULL),(106,'Jeff','Mangahas','1985-10-07','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'56-8511891-1','2021-01-26','2022-08-09',NULL),(107,'Elian','Iriberri','1982-06-22','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'97-8436985-7','2021-10-31','2022-08-09',NULL),(108,'Angelino','Banaga','1998-03-06','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09535577613',1,'65-5061209-4','2021-01-07','2022-08-09',NULL),(109,'Enrique','Macalipay','1995-07-29','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'79-6154551-7','2021-10-04','2022-08-09',NULL),(110,'Adam','Gatchalian','1987-01-29','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'27-8216516-8','2021-12-08','2022-08-09',NULL),(111,'Bryan','Cordova','1972-07-13','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'80-2943065-1','2021-07-04','2022-08-09',NULL),(112,'Cesario','Pangan','1981-10-23','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'98-0455989-2','2021-02-08','2022-08-09',NULL),(113,'Gabino','Bataller','1976-11-24','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'94-7016803-2','2021-02-14','2022-08-09',NULL),(114,'Derrick','Baylosis','1972-04-30','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'11-5127122-6','2021-06-22','2022-08-09',NULL),(115,'Malik','Estillore','1991-04-02','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'79-1085368-5','2021-03-21','2022-08-09',NULL),(116,'Dorian','Villaruz','1991-10-13','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'73-8114597-4','2021-07-23','2022-08-09',NULL),(117,'Alijah','Fernando','1972-03-06','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'99-0445149-3','2021-03-05','2022-08-09',NULL),(118,'Mano','Monteverde','1992-06-30','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'83-3210066-1','2021-06-24','2022-08-09',NULL),(119,'Sidney','Centino','1973-07-10','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'76-4878135-3','2021-08-18','2022-08-09',NULL),(120,'Sterling','Deseo','1977-04-15','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'14-4111777-6','2021-07-21','2022-08-09',NULL),(121,'Alexander','Montenegro','1981-09-19','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'63-2212513-2','2021-03-28','2022-08-09',NULL),(122,'Gerald','Yamada','1972-04-12','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'40-1631034-3','2021-09-26','2022-08-09',NULL),(123,'Fernando','Torrealba','1987-10-13','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'99-5727045-1','2021-07-27','2022-08-09',NULL),(124,'Colton','Salinas','1994-04-14','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'82-1442973-1','2021-08-11','2022-08-09',NULL),(125,'Montel','Payumo','1979-09-15','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'10-5366952-9','2021-04-01','2022-08-09',NULL),(126,'Scott','Villamar','1973-04-29','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'71-5399636-3','2021-10-08','2022-08-09',NULL),(127,'Gaspard','Mindoro','1976-03-13','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09202341123',1,'56-1157527-7','2021-05-29','2022-08-09',NULL),(128,'Ian','Bana','1983-05-04','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09472800187',1,'94-7774538-3','2021-02-13','2022-08-09',NULL),(129,'Marcus','Padilla','2001-08-02','M','02 Javier St., Poblacion, San Juan, Batangas','12345678901','09139686566',2,'12-3456789-0','2001-01-01','2022-08-09',NULL),(130,'Alex','Suaco','2001-07-08','M','02 Javier St., Poblacion, San Juan, Batangas','a9b9a0d9gd-a9g9ac9hdf','09274937506',1,'13-4395945-2','2022-08-05','2022-08-09',NULL);
/*!40000 ALTER TABLE `security_guard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_instruction`
--

DROP TABLE IF EXISTS `security_instruction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_instruction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `number_of_guards` int NOT NULL,
  `post_id` bigint NOT NULL,
  `shift_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `security_instruction_post_id_b1161847_fk_security_post_id` (`post_id`),
  KEY `security_instruction_shift_id_8ebac5ad_fk_security_shift_id` (`shift_id`),
  CONSTRAINT `security_instruction_post_id_b1161847_fk_security_post_id` FOREIGN KEY (`post_id`) REFERENCES `security_post` (`id`),
  CONSTRAINT `security_instruction_shift_id_8ebac5ad_fk_security_shift_id` FOREIGN KEY (`shift_id`) REFERENCES `security_shift` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_instruction`
--

LOCK TABLES `security_instruction` WRITE;
/*!40000 ALTER TABLE `security_instruction` DISABLE KEYS */;
INSERT INTO `security_instruction` VALUES (15,2,2,15),(16,2,2,16),(17,2,2,17),(18,2,2,18),(19,2,2,19),(20,2,2,20),(21,2,2,21),(22,2,2,22),(23,2,2,23),(24,2,2,24),(25,2,2,25),(26,2,2,26),(27,2,2,27),(28,2,2,28),(29,1,3,29),(30,1,3,30),(31,1,3,31),(32,1,3,32),(33,1,3,33),(34,1,3,34),(35,1,3,35),(36,1,3,36),(37,1,3,37),(38,1,3,38),(39,1,3,39),(40,1,3,40),(41,1,3,41),(42,1,3,42),(43,1,4,43),(44,1,4,44),(45,1,4,45),(46,1,4,46),(47,1,4,47),(48,1,4,48),(49,1,4,49),(50,1,4,50),(51,1,4,51),(52,1,4,52),(53,1,4,53),(54,1,4,54),(55,1,4,55),(56,1,4,56),(57,2,5,57),(58,2,5,58),(59,2,5,59),(60,2,5,60),(61,2,5,61),(62,2,5,62),(63,2,5,63),(64,2,5,64),(65,2,5,65),(66,2,5,66),(67,2,5,67),(68,2,5,68),(69,2,5,69),(70,2,5,70);
/*!40000 ALTER TABLE `security_instruction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_instruction_designations`
--

DROP TABLE IF EXISTS `security_instruction_designations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_instruction_designations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `instruction_id` bigint NOT NULL,
  `designation_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `security_instruction_des_instruction_id_designati_4f22b119_uniq` (`instruction_id`,`designation_id`),
  KEY `security_instruction_designation_id_5f3a4e27_fk_security_` (`designation_id`),
  CONSTRAINT `security_instruction_designation_id_5f3a4e27_fk_security_` FOREIGN KEY (`designation_id`) REFERENCES `security_designation` (`id`),
  CONSTRAINT `security_instruction_instruction_id_d2515b06_fk_security_` FOREIGN KEY (`instruction_id`) REFERENCES `security_instruction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_instruction_designations`
--

LOCK TABLES `security_instruction_designations` WRITE;
/*!40000 ALTER TABLE `security_instruction_designations` DISABLE KEYS */;
INSERT INTO `security_instruction_designations` VALUES (13,15,3),(25,15,5),(7,16,2),(19,16,4),(1,17,1),(14,17,3),(20,18,4),(26,18,5),(2,19,1),(27,19,5),(8,20,2),(21,20,4),(3,21,1),(15,21,3),(9,22,2),(22,22,4),(4,23,1),(16,23,3),(10,24,2),(28,24,5),(5,25,1),(17,25,3),(11,26,2),(23,26,4),(6,27,1),(18,27,3),(12,28,2),(24,28,4);
/*!40000 ALTER TABLE `security_instruction_designations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_location`
--

DROP TABLE IF EXISTS `security_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_location` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `include` tinyint(1) NOT NULL,
  `owner_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `address` (`address`),
  KEY `security_location_owner_id_179d3671_fk_security_customuser_id` (`owner_id`),
  CONSTRAINT `security_location_owner_id_179d3671_fk_security_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `security_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_location`
--

LOCK TABLES `security_location` WRITE;
/*!40000 ALTER TABLE `security_location` DISABLE KEYS */;
INSERT INTO `security_location` VALUES (3,'Polytechnic University of the Philippines','1016 Anonas, Sta. Mesa, Maynila, Kalakhang Maynila',0,3),(4,'Teresa Village Entrance','Teresa Village, Brgy. Bahay Toro',0,5),(5,'University of Santo Tomas','España Blvd, Sampaloc, Manila, 1008 Metro Manila',0,5);
/*!40000 ALTER TABLE `security_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_location_contracts`
--

DROP TABLE IF EXISTS `security_location_contracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_location_contracts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `location_id` bigint NOT NULL,
  `contract_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `security_location_contra_location_id_contract_id_e1f7c719_uniq` (`location_id`,`contract_id`),
  KEY `security_location_co_contract_id_91fd9b10_fk_security_` (`contract_id`),
  CONSTRAINT `security_location_co_contract_id_91fd9b10_fk_security_` FOREIGN KEY (`contract_id`) REFERENCES `security_contract` (`id`),
  CONSTRAINT `security_location_co_location_id_2dbad59f_fk_security_` FOREIGN KEY (`location_id`) REFERENCES `security_location` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_location_contracts`
--

LOCK TABLES `security_location_contracts` WRITE;
/*!40000 ALTER TABLE `security_location_contracts` DISABLE KEYS */;
INSERT INTO `security_location_contracts` VALUES (1,3,2),(2,4,3),(3,5,4);
/*!40000 ALTER TABLE `security_location_contracts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_post`
--

DROP TABLE IF EXISTS `security_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_post` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `place` varchar(50) DEFAULT NULL,
  `remarks` varchar(100) DEFAULT NULL,
  `is_armed` tinyint(1) NOT NULL,
  `location_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `security_post_location_id_81b8a590_fk_security_location_id` (`location_id`),
  CONSTRAINT `security_post_location_id_81b8a590_fk_security_location_id` FOREIGN KEY (`location_id`) REFERENCES `security_location` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_post`
--

LOCK TABLES `security_post` WRITE;
/*!40000 ALTER TABLE `security_post` DISABLE KEYS */;
INSERT INTO `security_post` VALUES (2,'Main Entrance',NULL,0,3),(3,'Village Entrance Parking',NULL,1,4),(4,'Village Entrance Stand',NULL,1,4),(5,'Main Bldg.',NULL,1,5);
/*!40000 ALTER TABLE `security_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_shift`
--

DROP TABLE IF EXISTS `security_shift`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_shift` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `day` int DEFAULT NULL,
  `start_time` time(6) DEFAULT NULL,
  `end_time` time(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_shift`
--

LOCK TABLES `security_shift` WRITE;
/*!40000 ALTER TABLE `security_shift` DISABLE KEYS */;
INSERT INTO `security_shift` VALUES (15,1,'08:00:00.000000','20:00:00.000000'),(16,1,'20:00:00.000000','08:00:00.000000'),(17,2,'08:00:00.000000','20:00:00.000000'),(18,2,'20:00:00.000000','08:00:00.000000'),(19,3,'08:00:00.000000','20:00:00.000000'),(20,3,'20:00:00.000000','08:00:00.000000'),(21,4,'08:00:00.000000','20:00:00.000000'),(22,4,'20:00:00.000000','08:00:00.000000'),(23,5,'08:00:00.000000','20:00:00.000000'),(24,5,'20:00:00.000000','08:00:00.000000'),(25,6,'08:00:00.000000','20:00:00.000000'),(26,6,'20:00:00.000000','08:00:00.000000'),(27,7,'08:00:00.000000','20:00:00.000000'),(28,7,'20:00:00.000000','08:00:00.000000'),(29,1,'08:00:00.000000','16:00:00.000000'),(30,1,'16:00:00.000000','00:00:00.000000'),(31,2,'08:00:00.000000','16:00:00.000000'),(32,2,'16:00:00.000000','00:00:00.000000'),(33,3,'08:00:00.000000','16:00:00.000000'),(34,3,'16:00:00.000000','00:00:00.000000'),(35,4,'08:00:00.000000','16:00:00.000000'),(36,4,'16:00:00.000000','00:00:00.000000'),(37,5,'08:00:00.000000','16:00:00.000000'),(38,5,'16:00:00.000000','00:00:00.000000'),(39,6,'08:00:00.000000','16:00:00.000000'),(40,6,'16:00:00.000000','00:00:00.000000'),(41,7,'08:00:00.000000','16:00:00.000000'),(42,7,'16:00:00.000000','00:00:00.000000'),(43,1,'08:00:00.000000','16:00:00.000000'),(44,1,'16:00:00.000000','00:00:00.000000'),(45,2,'08:00:00.000000','16:00:00.000000'),(46,2,'16:00:00.000000','00:00:00.000000'),(47,3,'08:00:00.000000','16:00:00.000000'),(48,3,'16:00:00.000000','00:00:00.000000'),(49,4,'08:00:00.000000','16:00:00.000000'),(50,4,'16:00:00.000000','00:00:00.000000'),(51,5,'08:00:00.000000','16:00:00.000000'),(52,5,'16:00:00.000000','00:00:00.000000'),(53,6,'08:00:00.000000','16:00:00.000000'),(54,6,'16:00:00.000000','00:00:00.000000'),(55,7,'08:00:00.000000','16:00:00.000000'),(56,7,'16:00:00.000000','00:00:00.000000'),(57,1,'08:00:00.000000','16:00:00.000000'),(58,1,'16:00:00.000000','00:00:00.000000'),(59,2,'08:00:00.000000','16:00:00.000000'),(60,2,'16:00:00.000000','00:00:00.000000'),(61,3,'08:00:00.000000','16:00:00.000000'),(62,3,'16:00:00.000000','00:00:00.000000'),(63,4,'08:00:00.000000','16:00:00.000000'),(64,4,'16:00:00.000000','00:00:00.000000'),(65,5,'08:00:00.000000','16:00:00.000000'),(66,5,'16:00:00.000000','00:00:00.000000'),(67,6,'08:00:00.000000','16:00:00.000000'),(68,6,'16:00:00.000000','00:00:00.000000'),(69,7,'08:00:00.000000','16:00:00.000000'),(70,7,'16:00:00.000000','00:00:00.000000');
/*!40000 ALTER TABLE `security_shift` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-10 22:44:37

SHOW SESSION VARIABLES LIKE 'character\_set\_%';
show variables like 'char%';
