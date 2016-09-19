-- MySQL dump 10.13  Distrib 5.6.19, for osx10.7 (i386)
--
-- Host: 127.0.0.1    Database: auto
-- ------------------------------------------------------
-- Server version	5.6.23

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
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (30,1,'asdfasfdadf',1452081168,0,1,2,0,0,0,0,0,NULL,0,0,NULL),(31,2,'hello,nihao',1452081187,0,0,2,0,0,0,0,0,NULL,0,0,NULL),(32,1,'nihao',1452081221,0,1,2,0,0,0,0,0,NULL,0,0,NULL),(33,1,'nihao',1452081243,0,1,2,0,0,0,0,0,NULL,0,0,NULL),(34,1,'1.11',1452523164,0,1,2,0,0,0,0,0,NULL,0,0,NULL),(35,1,'2016 3.7',1457362582,0,0,2,0,0,0,0,0,NULL,0,0,NULL);
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `answer_comments`
--

LOCK TABLES `answer_comments` WRITE;
/*!40000 ALTER TABLE `answer_comments` DISABLE KEYS */;
INSERT INTO `answer_comments` VALUES (12,32,2,'hi',1454166505),(13,32,2,'hiii',1454170463),(14,33,2,'hi',1454170676),(15,33,2,'hello',1454170689);
/*!40000 ALTER TABLE `answer_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `answer_vote`
--

LOCK TABLES `answer_vote` WRITE;
/*!40000 ALTER TABLE `answer_vote` DISABLE KEYS */;
INSERT INTO `answer_vote` VALUES (85,32,2,2,1452611182,1,1),(103,33,2,2,1456237143,1,1),(104,30,2,2,1463156233,1,1);
/*!40000 ALTER TABLE `answer_vote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (2,'hellowego@gmail.com','hello','$2a$12$N9uhR2g6dq6ZILjA3wLF8OKrtHLY2j8kG9h3jqRRBWoYo/MXhoU4u'),(3,'hi@hi.com','hi','$2a$12$1ba0oXIEGdVFDnjRBwDSE.3BkA9Rc7OqeFY3DYLP1LZKLWWgSAgFG'),(4,'aa@aa.com','aa','$2a$12$jR.y58L23VVU30o/Q2Stl.UPVx2d9tKZpPPNQwW.AGXucqD.xQcdm');
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `captcha`
--

LOCK TABLES `captcha` WRITE;
/*!40000 ALTER TABLE `captcha` DISABLE KEYS */;
/*!40000 ALTER TABLE `captcha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `catalog`
--

LOCK TABLES `catalog` WRITE;
/*!40000 ALTER TABLE `catalog` DISABLE KEYS */;
INSERT INTO `catalog` VALUES (1,'新手上路','/newdriver',NULL);
/*!40000 ALTER TABLE `catalog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `entries`
--

LOCK TABLES `entries` WRITE;
/*!40000 ALTER TABLE `entries` DISABLE KEYS */;
INSERT INTO `entries` VALUES (1,2,'auto','auto','let\'s go !','<p>let\'s go !</p>','2015-08-04 15:07:52','2015-08-04 15:07:52');
/*!40000 ALTER TABLE `entries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `link`
--

LOCK TABLES `link` WRITE;
/*!40000 ALTER TABLE `link` DISABLE KEYS */;
INSERT INTO `link` VALUES (1,0,'baidu','http://baidu.com',26,6,1468334176,1),(2,0,'微博','http://weibo.com/',0,0,1472029397,0),(3,0,'网易','http://163.com',0,0,1472047253,0),(4,0,'搜狐','http://sohu.com',0,0,1472047319,0),(5,0,'新浪','http://sina.com',0,0,1472049310,0),(6,0,'腾讯','http://qq.com',0,0,1472049428,0),(7,0,'淘宝','http://taobao.com',0,0,1472049447,0),(8,0,'京东','http://jd.com',0,0,1472049458,0),(9,0,'亚马逊中国','http://z.cn',0,0,1472049487,0),(10,0,'优酷','http://youku.com',0,0,1472049639,0),(11,0,'谷歌','http://google.com',0,0,1472049654,0),(12,1,'youtube','http://youtube.com',0,0,1472049708,0),(13,1,'脸书','http://facebook.com',0,0,1472049738,0),(14,1,'推特','http://twitter.com',0,0,1472049788,0),(15,1,'雅虎','http://yahoo.com',0,0,1472050334,0),(16,1,'亚马逊','http://amazon.com',0,0,1472050523,0),(17,1,'bing','http://bing.com',0,3,1472050603,0),(18,2,'易贝','http://ebay.com',1,1,1472051970,0),(19,2,'msn','http://msn.com',0,4,1472052558,0);
/*!40000 ALTER TABLE `link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'首页在哪？hi','首页在哪里？111',1444567491,1444567491,1,10,0,50,10,0,0,1,0,0,0,0,NULL,0,2130706433,0,1.602059991328,1444661821,0,0,0,'3931839029 2231221738',0,NULL,NULL,NULL,0),(2,'首页在哪？','首页在哪里？222',1444567491,1444567491,1,10,0,50,10,0,0,1,0,0,0,0,NULL,0,2130706433,0,1.602059991328,1444661821,0,0,0,'3931839029 2231221738',0,NULL,NULL,NULL,0),(3,'首页在哪？','首页在哪里？333',1444567491,1444567491,1,10,0,50,10,0,0,1,0,0,0,0,NULL,0,2130706433,0,1.602059991328,1444661821,0,0,0,'3931839029 2231221738',0,NULL,NULL,NULL,0),(4,'首页在哪？','首页在哪里？4444',1444567491,1444567491,1,10,0,50,10,0,0,1,0,0,0,0,NULL,0,2130706433,0,1.602059991328,1444661821,0,0,0,'3931839029 2231221738',0,NULL,NULL,NULL,0),(5,'1111','2222',1463069341,1463069341,2,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,0,NULL,0,NULL,NULL,NULL,0),(6,'','',1463153496,1463153496,2,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,0,NULL,0,NULL,NULL,NULL,0),(7,'ddasdfasdf','asdfa3333',1463154128,1463154128,2,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,0,NULL,0,NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user_follow`
--

LOCK TABLES `user_follow` WRITE;
/*!40000 ALTER TABLE `user_follow` DISABLE KEYS */;
INSERT INTO `user_follow` VALUES (1,1,2,'2016-02-24 21:59:31'),(2,1,3,'2016-02-24 21:59:31'),(3,2,3,'2016-02-24 21:59:31'),(4,2,1,'2016-03-02 21:10:30');
/*!40000 ALTER TABLE `user_follow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user_vote`
--

LOCK TABLES `user_vote` WRITE;
/*!40000 ALTER TABLE `user_vote` DISABLE KEYS */;
INSERT INTO `user_vote` VALUES (2,18,1,1472320977),(2,19,0,1472320970);
/*!40000 ALTER TABLE `user_vote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'hi','aa1@a.com',NULL,'$2a$12$tzXpTV2ajhQejJoq86Sm4eEDPhCh6PnuhCuplVlwxgHyxvFXIhWeK',NULL,NULL,NULL,NULL,NULL,NULL,0,'2016-02-22 22:13:05',NULL,0,NULL,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,'2016-02-22 22:13:05',0,0,0,NULL,'hi',0,NULL,NULL,NULL,NULL,NULL),(2,'hello','hellowego@gmail.com',NULL,'$2a$12$s8zZw/8z2PvffBqx2nhxmOagwxR8tJClfGymP5bwm0VG.tDnAZrnO',NULL,NULL,NULL,NULL,NULL,NULL,0,'2016-02-22 22:43:42',NULL,0,NULL,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,1,10,12,0,11,'2016-02-22 22:43:42',0,22,0,NULL,'hello',0,NULL,NULL,NULL,NULL,NULL),(3,'你好','hello@gmail.com',NULL,'$2a$12$BwEk.wX0fe/1V5v/EWNTMua6TeKgi3yztCdUXQ4/im.6LpP6.pwI2',NULL,NULL,NULL,NULL,NULL,NULL,0,'2016-03-02 21:15:54',NULL,0,NULL,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,'2016-03-02 21:15:54',0,0,0,NULL,'你好',0,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'auto'
--

--
-- Dumping routines for database 'auto'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-19 20:35:18
