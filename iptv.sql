-- MySQL dump 10.13  Distrib 5.7.29, for linux-glibc2.12 (x86_64)
--
-- Host: 127.0.0.1    Database: iptv
-- ------------------------------------------------------
-- Server version	5.7.30-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agent`
--

DROP TABLE IF EXISTS `agent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip_control` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `ip_receive_multicast` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cpu` smallint(6) DEFAULT NULL,
  `ram` smallint(6) DEFAULT NULL,
  `disk` smallint(6) DEFAULT NULL,
  `location` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `is_monitor` int(11) DEFAULT NULL,
  `is_alarm` int(11) DEFAULT NULL,
  `signal_monitor` int(11) DEFAULT NULL,
  `video_monitor` int(11) DEFAULT NULL,
  `audio_monitor` int(11) DEFAULT NULL,
  `run_thread` int(11) DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `date_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip_control` (`ip_control`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agent`
--

LOCK TABLES `agent` WRITE;
/*!40000 ALTER TABLE `agent` DISABLE KEYS */;
/*!40000 ALTER TABLE `agent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `agent_has_group_profile`
--

DROP TABLE IF EXISTS `agent_has_group_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agent_has_group_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) NOT NULL,
  `group_profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `agent_has_group_profile_agent_id_group_profile_id_04256946_uniq` (`agent_id`,`group_profile_id`),
  KEY `agent_has_group_prof_group_profile_id_a52ccfb4_fk_group_pro` (`group_profile_id`),
  CONSTRAINT `agent_has_group_prof_group_profile_id_a52ccfb4_fk_group_pro` FOREIGN KEY (`group_profile_id`) REFERENCES `group_profile` (`id`),
  CONSTRAINT `agent_has_group_profile_agent_id_173b276d_fk_agent_id` FOREIGN KEY (`agent_id`) REFERENCES `agent` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agent_has_group_profile`
--

LOCK TABLES `agent_has_group_profile` WRITE;
/*!40000 ALTER TABLE `agent_has_group_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `agent_has_group_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `agent_has_vlan`
--

DROP TABLE IF EXISTS `agent_has_vlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agent_has_vlan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) NOT NULL,
  `vlan_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `agent_has_vlan_vlan_id_agent_id_17fecf0b_uniq` (`vlan_id`,`agent_id`),
  KEY `agent_has_vlan_agent_id_582f97e6_fk_agent_id` (`agent_id`),
  CONSTRAINT `agent_has_vlan_agent_id_582f97e6_fk_agent_id` FOREIGN KEY (`agent_id`) REFERENCES `agent` (`id`),
  CONSTRAINT `agent_has_vlan_vlan_id_b25a7b85_fk_vlan_id` FOREIGN KEY (`vlan_id`) REFERENCES `vlan` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agent_has_vlan`
--

LOCK TABLES `agent_has_vlan` WRITE;
/*!40000 ALTER TABLE `agent_has_vlan` DISABLE KEYS */;
/*!40000 ALTER TABLE `agent_has_vlan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add agent',7,'add_agent'),(26,'Can change agent',7,'change_agent'),(27,'Can delete agent',7,'delete_agent'),(28,'Can view agent',7,'view_agent'),(29,'Can add channel',8,'add_channel'),(30,'Can change channel',8,'change_channel'),(31,'Can delete channel',8,'delete_channel'),(32,'Can view channel',8,'view_channel'),(33,'Can add encoder',9,'add_encoder'),(34,'Can change encoder',9,'change_encoder'),(35,'Can delete encoder',9,'delete_encoder'),(36,'Can view encoder',9,'view_encoder'),(37,'Can add enviroment',10,'add_enviroment'),(38,'Can change enviroment',10,'change_enviroment'),(39,'Can delete enviroment',10,'delete_enviroment'),(40,'Can view enviroment',10,'view_enviroment'),(41,'Can add group channel',11,'add_groupchannel'),(42,'Can change group channel',11,'change_groupchannel'),(43,'Can delete group channel',11,'delete_groupchannel'),(44,'Can view group channel',11,'view_groupchannel'),(45,'Can add group profile',12,'add_groupprofile'),(46,'Can change group profile',12,'change_groupprofile'),(47,'Can delete group profile',12,'delete_groupprofile'),(48,'Can view group profile',12,'view_groupprofile'),(49,'Can add multicast ip',13,'add_multicastip'),(50,'Can change multicast ip',13,'change_multicastip'),(51,'Can delete multicast ip',13,'delete_multicastip'),(52,'Can view multicast ip',13,'view_multicastip'),(53,'Can add profile quality',14,'add_profilequality'),(54,'Can change profile quality',14,'change_profilequality'),(55,'Can delete profile quality',14,'delete_profilequality'),(56,'Can view profile quality',14,'view_profilequality'),(57,'Can add satellite dishe',15,'add_satellitedishe'),(58,'Can change satellite dishe',15,'change_satellitedishe'),(59,'Can delete satellite dishe',15,'delete_satellitedishe'),(60,'Can view satellite dishe',15,'view_satellitedishe'),(61,'Can add vlan provider',16,'add_vlanprovider'),(62,'Can change vlan provider',16,'change_vlanprovider'),(63,'Can delete vlan provider',16,'delete_vlanprovider'),(64,'Can view vlan provider',16,'view_vlanprovider'),(65,'Can add vlan',17,'add_vlan'),(66,'Can change vlan',17,'change_vlan'),(67,'Can delete vlan',17,'delete_vlan'),(68,'Can view vlan',17,'view_vlan'),(69,'Can add profile',18,'add_profile'),(70,'Can change profile',18,'change_profile'),(71,'Can delete profile',18,'delete_profile'),(72,'Can view profile',18,'view_profile'),(73,'Can add user has multicast ip',19,'add_userhasmulticastip'),(74,'Can change user has multicast ip',19,'change_userhasmulticastip'),(75,'Can delete user has multicast ip',19,'delete_userhasmulticastip'),(76,'Can view user has multicast ip',19,'view_userhasmulticastip'),(77,'Can add satellite dishe has multicast ip',20,'add_satellitedishehasmulticastip'),(78,'Can change satellite dishe has multicast ip',20,'change_satellitedishehasmulticastip'),(79,'Can delete satellite dishe has multicast ip',20,'delete_satellitedishehasmulticastip'),(80,'Can view satellite dishe has multicast ip',20,'view_satellitedishehasmulticastip'),(81,'Can add monitor',21,'add_monitor'),(82,'Can change monitor',21,'change_monitor'),(83,'Can delete monitor',21,'delete_monitor'),(84,'Can view monitor',21,'view_monitor'),(85,'Can add group profile has profile',22,'add_groupprofilehasprofile'),(86,'Can change group profile has profile',22,'change_groupprofilehasprofile'),(87,'Can delete group profile has profile',22,'delete_groupprofilehasprofile'),(88,'Can view group profile has profile',22,'view_groupprofilehasprofile'),(89,'Can add group channel has channel',23,'add_groupchannelhaschannel'),(90,'Can change group channel has channel',23,'change_groupchannelhaschannel'),(91,'Can delete group channel has channel',23,'delete_groupchannelhaschannel'),(92,'Can view group channel has channel',23,'view_groupchannelhaschannel'),(93,'Can add encoder input profile',24,'add_encoderinputprofile'),(94,'Can change encoder input profile',24,'change_encoderinputprofile'),(95,'Can delete encoder input profile',24,'delete_encoderinputprofile'),(96,'Can view encoder input profile',24,'view_encoderinputprofile'),(97,'Can add encoder has vlan',25,'add_encoderhasvlan'),(98,'Can change encoder has vlan',25,'change_encoderhasvlan'),(99,'Can delete encoder has vlan',25,'delete_encoderhasvlan'),(100,'Can view encoder has vlan',25,'view_encoderhasvlan'),(101,'Can add agent has vlan',26,'add_agenthasvlan'),(102,'Can change agent has vlan',26,'change_agenthasvlan'),(103,'Can delete agent has vlan',26,'delete_agenthasvlan'),(104,'Can view agent has vlan',26,'view_agenthasvlan'),(105,'Can add agent has group profile',27,'add_agenthasgroupprofile'),(106,'Can change agent has group profile',27,'change_agenthasgroupprofile'),(107,'Can delete agent has group profile',27,'delete_agenthasgroupprofile'),(108,'Can view agent has group profile',27,'view_agenthasgroupprofile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$qn6uoXsIohsB$+Jd36mW46llhlJKZUEQ/4h7lgWSG+zqTqOtOg7XfCIs=',NULL,1,'admin','','','admin@gmail.com',1,1,'2020-12-13 10:00:52.547111');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `channel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `date_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel`
--

LOCK TABLES `channel` WRITE;
/*!40000 ALTER TABLE `channel` DISABLE KEYS */;
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'agent','agent'),(27,'agent','agenthasgroupprofile'),(26,'agent','agenthasvlan'),(8,'agent','channel'),(9,'agent','encoder'),(25,'agent','encoderhasvlan'),(24,'agent','encoderinputprofile'),(10,'agent','enviroment'),(11,'agent','groupchannel'),(23,'agent','groupchannelhaschannel'),(12,'agent','groupprofile'),(22,'agent','groupprofilehasprofile'),(21,'agent','monitor'),(13,'agent','multicastip'),(18,'agent','profile'),(14,'agent','profilequality'),(15,'agent','satellitedishe'),(20,'agent','satellitedishehasmulticastip'),(19,'agent','userhasmulticastip'),(17,'agent','vlan'),(16,'agent','vlanprovider'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-12-13 09:59:04.026748'),(2,'auth','0001_initial','2020-12-13 09:59:04.356181'),(3,'admin','0001_initial','2020-12-13 09:59:05.248290'),(4,'admin','0002_logentry_remove_auto_add','2020-12-13 09:59:05.470419'),(5,'admin','0003_logentry_add_action_flag_choices','2020-12-13 09:59:05.487314'),(6,'agent','0001_initial','2020-12-13 09:59:06.971019'),(7,'agent','0002_auto_20201213_0950','2020-12-13 09:59:14.819166'),(8,'contenttypes','0002_remove_content_type_name','2020-12-13 09:59:15.006436'),(9,'auth','0002_alter_permission_name_max_length','2020-12-13 09:59:15.103700'),(10,'auth','0003_alter_user_email_max_length','2020-12-13 09:59:15.212814'),(11,'auth','0004_alter_user_username_opts','2020-12-13 09:59:15.244638'),(12,'auth','0005_alter_user_last_login_null','2020-12-13 09:59:15.327977'),(13,'auth','0006_require_contenttypes_0002','2020-12-13 09:59:15.334417'),(14,'auth','0007_alter_validators_add_error_messages','2020-12-13 09:59:15.352139'),(15,'auth','0008_alter_user_username_max_length','2020-12-13 09:59:15.471851'),(16,'auth','0009_alter_user_last_name_max_length','2020-12-13 09:59:15.591567'),(17,'auth','0010_alter_group_name_max_length','2020-12-13 09:59:15.707606'),(18,'auth','0011_update_proxy_permissions','2020-12-13 09:59:15.768443'),(19,'sessions','0001_initial','2020-12-13 09:59:15.823204');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encoder`
--

DROP TABLE IF EXISTS `encoder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encoder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `ip` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `hardware` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `date_update` datetime(6) DEFAULT NULL,
  `enviroment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `ip` (`ip`),
  KEY `encoder_enviroment_id_849333b1_fk_enviroment_id` (`enviroment_id`),
  CONSTRAINT `encoder_enviroment_id_849333b1_fk_enviroment_id` FOREIGN KEY (`enviroment_id`) REFERENCES `enviroment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encoder`
--

LOCK TABLES `encoder` WRITE;
/*!40000 ALTER TABLE `encoder` DISABLE KEYS */;
/*!40000 ALTER TABLE `encoder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encoder_has_vlan`
--

DROP TABLE IF EXISTS `encoder_has_vlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encoder_has_vlan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `encoder_id` int(11) NOT NULL,
  `vlan_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encoder_has_vlan_vlan_id_encoder_id_db568629_uniq` (`vlan_id`,`encoder_id`),
  KEY `encoder_has_vlan_encoder_id_71e84c38_fk_encoder_id` (`encoder_id`),
  CONSTRAINT `encoder_has_vlan_encoder_id_71e84c38_fk_encoder_id` FOREIGN KEY (`encoder_id`) REFERENCES `encoder` (`id`),
  CONSTRAINT `encoder_has_vlan_vlan_id_e64896cd_fk_vlan_id` FOREIGN KEY (`vlan_id`) REFERENCES `vlan` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encoder_has_vlan`
--

LOCK TABLES `encoder_has_vlan` WRITE;
/*!40000 ALTER TABLE `encoder_has_vlan` DISABLE KEYS */;
/*!40000 ALTER TABLE `encoder_has_vlan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encoder_input_profile`
--

DROP TABLE IF EXISTS `encoder_input_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encoder_input_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `encoder_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `encoder_input_profile_encoder_id_profile_id_d0569010_uniq` (`encoder_id`,`profile_id`),
  KEY `encoder_input_profile_profile_id_7cdd6ea4_fk_profile_id` (`profile_id`),
  CONSTRAINT `encoder_input_profile_encoder_id_9f00b4f8_fk_encoder_id` FOREIGN KEY (`encoder_id`) REFERENCES `encoder` (`id`),
  CONSTRAINT `encoder_input_profile_profile_id_7cdd6ea4_fk_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encoder_input_profile`
--

LOCK TABLES `encoder_input_profile` WRITE;
/*!40000 ALTER TABLE `encoder_input_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `encoder_input_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enviroment`
--

DROP TABLE IF EXISTS `enviroment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `enviroment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enviroment`
--

LOCK TABLES `enviroment` WRITE;
/*!40000 ALTER TABLE `enviroment` DISABLE KEYS */;
/*!40000 ALTER TABLE `enviroment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_channel`
--

DROP TABLE IF EXISTS `group_channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group_channel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_channel`
--

LOCK TABLES `group_channel` WRITE;
/*!40000 ALTER TABLE `group_channel` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_channel_has_channel`
--

DROP TABLE IF EXISTS `group_channel_has_channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group_channel_has_channel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `channel_id` int(11) NOT NULL,
  `group_channel_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_channel_has_channe_channel_id_group_channel_f4cbd8b2_uniq` (`channel_id`,`group_channel_id`),
  KEY `group_channel_has_ch_group_channel_id_14e80cc4_fk_group_cha` (`group_channel_id`),
  CONSTRAINT `group_channel_has_ch_group_channel_id_14e80cc4_fk_group_cha` FOREIGN KEY (`group_channel_id`) REFERENCES `group_channel` (`id`),
  CONSTRAINT `group_channel_has_channel_channel_id_b88eee7f_fk_channel_id` FOREIGN KEY (`channel_id`) REFERENCES `channel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_channel_has_channel`
--

LOCK TABLES `group_channel_has_channel` WRITE;
/*!40000 ALTER TABLE `group_channel_has_channel` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_channel_has_channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_profile`
--

DROP TABLE IF EXISTS `group_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_profile`
--

LOCK TABLES `group_profile` WRITE;
/*!40000 ALTER TABLE `group_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_profile_has_profile`
--

DROP TABLE IF EXISTS `group_profile_has_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group_profile_has_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_profile_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_profile_has_profil_profile_id_group_profile_294437bb_uniq` (`profile_id`,`group_profile_id`),
  KEY `group_profile_has_pr_group_profile_id_dcae7844_fk_group_pro` (`group_profile_id`),
  CONSTRAINT `group_profile_has_pr_group_profile_id_dcae7844_fk_group_pro` FOREIGN KEY (`group_profile_id`) REFERENCES `group_profile` (`id`),
  CONSTRAINT `group_profile_has_profile_profile_id_478de7c3_fk_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_profile_has_profile`
--

LOCK TABLES `group_profile_has_profile` WRITE;
/*!40000 ALTER TABLE `group_profile_has_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_profile_has_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitor`
--

DROP TABLE IF EXISTS `monitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status_signal` int(11) DEFAULT NULL,
  `status_video` int(11) DEFAULT NULL,
  `status_audio` int(11) DEFAULT NULL,
  `signal_monitor` int(11) DEFAULT NULL,
  `video_monitor` int(11) DEFAULT NULL,
  `audio_monitor` int(11) DEFAULT NULL,
  `is_enable` int(11) DEFAULT NULL,
  `date_update` datetime(6) DEFAULT NULL,
  `agent_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `monitor_profile_id_agent_id_68f15db3_uniq` (`profile_id`,`agent_id`),
  KEY `monitor_agent_id_5a087e23_fk_agent_id` (`agent_id`),
  CONSTRAINT `monitor_agent_id_5a087e23_fk_agent_id` FOREIGN KEY (`agent_id`) REFERENCES `agent` (`id`),
  CONSTRAINT `monitor_profile_id_f82705a8_fk_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitor`
--

LOCK TABLES `monitor` WRITE;
/*!40000 ALTER TABLE `monitor` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `multicast_ip`
--

DROP TABLE IF EXISTS `multicast_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `multicast_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip` (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `multicast_ip`
--

LOCK TABLES `multicast_ip` WRITE;
/*!40000 ALTER TABLE `multicast_ip` DISABLE KEYS */;
/*!40000 ALTER TABLE `multicast_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `desc` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `date_update` datetime(6) DEFAULT NULL,
  `is_original` int(11) NOT NULL,
  `channel_id` int(11) NOT NULL,
  `encoder_id` int(11) NOT NULL,
  `multicast_ip_id` int(11) NOT NULL,
  `profile_quality_id` int(11) NOT NULL,
  `vlan_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `profile_profile_quality_id_chann_3a26a9f7_uniq` (`profile_quality_id`,`channel_id`,`multicast_ip_id`),
  KEY `profile_channel_id_551733a3_fk_channel_id` (`channel_id`),
  KEY `profile_encoder_id_dbb23bc3_fk_encoder_id` (`encoder_id`),
  KEY `profile_multicast_ip_id_ac289963_fk_multicast_ip_id` (`multicast_ip_id`),
  KEY `profile_vlan_id_61f62736_fk_vlan_id` (`vlan_id`),
  CONSTRAINT `profile_channel_id_551733a3_fk_channel_id` FOREIGN KEY (`channel_id`) REFERENCES `channel` (`id`),
  CONSTRAINT `profile_encoder_id_dbb23bc3_fk_encoder_id` FOREIGN KEY (`encoder_id`) REFERENCES `encoder` (`id`),
  CONSTRAINT `profile_multicast_ip_id_ac289963_fk_multicast_ip_id` FOREIGN KEY (`multicast_ip_id`) REFERENCES `multicast_ip` (`id`),
  CONSTRAINT `profile_profile_quality_id_cc9c39bb_fk_profile_quality_id` FOREIGN KEY (`profile_quality_id`) REFERENCES `profile_quality` (`id`),
  CONSTRAINT `profile_vlan_id_61f62736_fk_vlan_id` FOREIGN KEY (`vlan_id`) REFERENCES `vlan` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile_quality`
--

DROP TABLE IF EXISTS `profile_quality`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profile_quality` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quality` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `quality` (`quality`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile_quality`
--

LOCK TABLES `profile_quality` WRITE;
/*!40000 ALTER TABLE `profile_quality` DISABLE KEYS */;
/*!40000 ALTER TABLE `profile_quality` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satellite_dishe`
--

DROP TABLE IF EXISTS `satellite_dishe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `satellite_dishe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `diameter` decimal(5,2) DEFAULT NULL,
  `location` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `date_update` datetime(6) DEFAULT NULL,
  `env_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `satellite_dishe_id_env_id_2f80475d_uniq` (`id`,`env_id`),
  KEY `satellite_dishe_env_id_53da9e09_fk_enviroment_id` (`env_id`),
  CONSTRAINT `satellite_dishe_env_id_53da9e09_fk_enviroment_id` FOREIGN KEY (`env_id`) REFERENCES `enviroment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satellite_dishe`
--

LOCK TABLES `satellite_dishe` WRITE;
/*!40000 ALTER TABLE `satellite_dishe` DISABLE KEYS */;
/*!40000 ALTER TABLE `satellite_dishe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satellite_dishe_has_multicast_ip`
--

DROP TABLE IF EXISTS `satellite_dishe_has_multicast_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `satellite_dishe_has_multicast_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `multicast_ip_id` int(11) NOT NULL,
  `satellite_dishe_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `satellite_dishe_has_mult_multicast_ip_id_satellit_c14eec7c_uniq` (`multicast_ip_id`,`satellite_dishe_id`),
  KEY `satellite_dishe_has__satellite_dishe_id_19ff48af_fk_satellite` (`satellite_dishe_id`),
  CONSTRAINT `satellite_dishe_has__multicast_ip_id_f2c46220_fk_multicast` FOREIGN KEY (`multicast_ip_id`) REFERENCES `multicast_ip` (`id`),
  CONSTRAINT `satellite_dishe_has__satellite_dishe_id_19ff48af_fk_satellite` FOREIGN KEY (`satellite_dishe_id`) REFERENCES `satellite_dishe` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satellite_dishe_has_multicast_ip`
--

LOCK TABLES `satellite_dishe_has_multicast_ip` WRITE;
/*!40000 ALTER TABLE `satellite_dishe_has_multicast_ip` DISABLE KEYS */;
/*!40000 ALTER TABLE `satellite_dishe_has_multicast_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_has_multicast_ip`
--

DROP TABLE IF EXISTS `user_has_multicast_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_has_multicast_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `multicast_ip_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_has_multicast_ip_multicast_ip_id_user_id_17d542fa_uniq` (`multicast_ip_id`,`user_id`),
  KEY `user_has_multicast_ip_user_id_38199347_fk_auth_user_id` (`user_id`),
  CONSTRAINT `user_has_multicast_i_multicast_ip_id_2d1668a0_fk_multicast` FOREIGN KEY (`multicast_ip_id`) REFERENCES `multicast_ip` (`id`),
  CONSTRAINT `user_has_multicast_ip_user_id_38199347_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_has_multicast_ip`
--

LOCK TABLES `user_has_multicast_ip` WRITE;
/*!40000 ALTER TABLE `user_has_multicast_ip` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_has_multicast_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vlan`
--

DROP TABLE IF EXISTS `vlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vlan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vlanid` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `date_update` datetime(6) DEFAULT NULL,
  `env_id` int(11) NOT NULL,
  `vlan_provider_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vlan_vlan_provider_id_env_id_vlanid_157c1516_uniq` (`vlan_provider_id`,`env_id`,`vlanid`),
  KEY `vlan_env_id_5aee5537_fk_enviroment_id` (`env_id`),
  CONSTRAINT `vlan_env_id_5aee5537_fk_enviroment_id` FOREIGN KEY (`env_id`) REFERENCES `enviroment` (`id`),
  CONSTRAINT `vlan_vlan_provider_id_09b095b8_fk_vlan_provider_id` FOREIGN KEY (`vlan_provider_id`) REFERENCES `vlan_provider` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vlan`
--

LOCK TABLES `vlan` WRITE;
/*!40000 ALTER TABLE `vlan` DISABLE KEYS */;
/*!40000 ALTER TABLE `vlan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vlan_provider`
--

DROP TABLE IF EXISTS `vlan_provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vlan_provider` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vlan_provider`
--

LOCK TABLES `vlan_provider` WRITE;
/*!40000 ALTER TABLE `vlan_provider` DISABLE KEYS */;
/*!40000 ALTER TABLE `vlan_provider` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-13 17:02:00
