-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: geektext
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `address` text NOT NULL,
  `city` varchar(30) NOT NULL,
  `state` varchar(2) NOT NULL,
  `postal_code` int(11) NOT NULL,
  `phone_num` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `address_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (1,1,'5076 NW 113th PL','Doral','FL',33178,'3059048724');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('bbc57fbb626f');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_post`
--

DROP TABLE IF EXISTS `blog_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `blog_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `title` varchar(140) NOT NULL,
  `text` text NOT NULL,
  `rating` varchar(140) DEFAULT NULL,
  `true_private` varchar(140) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `blog_post_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_post`
--

LOCK TABLES `blog_post` WRITE;
/*!40000 ALTER TABLE `blog_post` DISABLE KEYS */;
/*!40000 ALTER TABLE `blog_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `books` (
  `ISBN` varchar(13) NOT NULL,
  `title` text NOT NULL,
  `author` text NOT NULL,
  `genre` text NOT NULL,
  `publication_year` varchar(4) DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
  `description` varchar(800) NOT NULL,
  `average_rating` decimal(5,2) DEFAULT NULL,
  `ratings_count` int(11) DEFAULT NULL,
  `ratings_1` int(11) DEFAULT NULL,
  `ratings_2` int(11) DEFAULT NULL,
  `ratings_3` int(11) DEFAULT NULL,
  `ratings_4` int(11) DEFAULT NULL,
  `ratings_5` int(11) DEFAULT NULL,
  `image_url` text NOT NULL,
  `small_image_url` text NOT NULL,
  PRIMARY KEY (`ISBN`),
  UNIQUE KEY `ISBN` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('055357342X','A Storm of Swords','George R.R. Martin','Fantasy','2000',16.99,175,'Here is the third volume in George R.R. Martin\'s magnificent cycle of novels that includes�A Game of Thrones�and�A Clash of Kings. Together, this series comprises a genuine masterpiece of modern fantasy, destined to stand as one of the great achievements of imaginative fiction.',4.54,469022,1456,4820,36418,149268,335682,'https://images.gr-assets.com/books/1497931121m/62291.jpg','https://images.gr-assets.com/books/1497931121s/62291.jpg'),('345347951','Childhood\'s End','Arthur C. Clarke','Sci-Fi','1953',7.99,172,'The Overlords appeared suddenly over every city--intellectually, technologically, and militarily superior to humankind. Benevolent, they made few demands: unify earth, eliminate poverty, and end war. With little rebellion, humankind agreed, and a golden age began. But at what cost? With the advent of peace, man ceases to strive for creative greatness, and a malaise settles over the human race. To those who resist, it becomes evident that the Overlords have an agenda of their own. As civilization approaches the crossroads, will the Overlords spell the end for humankind . . . or the beginning?',4.09,87141,943,3578,18261,36854,37115,'https://images.gr-assets.com/books/1320552628m/414999.jpg','https://images.gr-assets.com/books/1320552628s/414999.jpg'),('345538374','The Hobbit and The Lord of the Rings','J.R.R. Tolkien','Fantasy','1973',42.99,74,'The Lord of the Rings tells of the great quest undertaken by Frodo Baggins and the Fellowship of the Ring: Gandalf the wizard; the hobbits Merry, Pippin, and Sam; Gimli the dwarf; Legolas the elf; Boromir of Gondor; and a tall, mysterious stranger called Strider. J.R.R. Tolkien\'s three volume masterpiece is at once a classic myth and a modern fairy tale�a story of high and heroic adventure set in the unforgettable landscape of Middle-earth.',4.59,90907,826,1281,5819,19982,66440,'https://images.gr-assets.com/books/1346072396m/30.jpg','https://images.gr-assets.com/books/1346072396s/30.jpg'),('452284244','Animal Farm: A Fairy Story','George Orwell','Satire','1945',12.99,896,'A farm is taken over by its overworked, mistreated animals. With flaming idealism and stirring slogans, they set out to create a paradise of progress, justice, and equality. Thus the stage is set for one of the most telling satiric fables ever penned �a razor-edged fairy tale for grown-ups that records the evolution from revolution against tyranny to a totalitarianism just as terrible.�When Animal Farm was first published, Stalinist Russia was seen as its target. Today it is devastatingly clear that wherever and whenever freedom is attacked, under whatever banner, the cutting clarity and savage comedy of George Orwell�s masterpiece have a meaning and message still ferociously fresh.',3.87,1881700,66854,135147,433432,698642,648912,'https://images.gr-assets.com/books/1424037542m/7613.jpg','https://images.gr-assets.com/books/1424037542s/7613.jpg'),('545044251','Complete Harry Potter Boxed Set','J.K. Rowling','Fantasy','1998',42.99,76,'All seven eBooks in the multi-award winning, internationally bestselling Harry Potter series, available as one download with stunning cover art by Olly Moss. Enjoy the stories that have captured the imagination of millions worldwide.',4.74,190050,1105,1285,7020,30666,164049,'https://images.gr-assets.com/books/1392579059m/862041.jpg','https://images.gr-assets.com/books/1392579059s/862041.jpg'),('671728687','The Rise and Fall of the Third Reich: A History of Nazi Germany','William L. Shirer','History','1960',22.99,1,'Hitler boasted that The Third Reich would last a thousand years. It lasted only 12. But those 12 years contained some of the most catastrophic events Western civilization has ever known. No other powerful empire ever bequeathed such mountains of evidence about its birth and destruction as the Third Reich. When the bitter war was over, and before the Nazis could destroy their files, the Allied demand for unconditional surrender produced an almost hour-by-hour record of the nightmare empire built by Adolph Hitler. This record included the testimony of Nazi leaders and of concentration camp inmates, the diaries of officials, transcripts of secret conferences, army orders, private letters�all the vast paperwork behind Hitler\'s drive to conquer the world.',4.15,64391,1201,2344,11463,23137,29859,'https://images.gr-assets.com/books/1331223772m/767171.jpg','https://images.gr-assets.com/books/1331223772s/767171.jpg'),('718154835','The Fry Chronicles: An Autobiography','Stephen Fry','Autobiography','2010',7.99,26,'Thirteen years ago, Moab Is My Washpot, Stephen Fry\'s autobiography of his early years, was published to rave reviews and was a huge best seller. In the years since, Stephen Fry has moved into a completely new stratosphere, both as a public figure, and a private man. Now he is not just a multi-award-winning comedian and actor, but also an author, director, and presenter.',3.87,14037,262,844,3743,6632,4249,'https://images.gr-assets.com/books/1376317909m/8649656.jpg','https://images.gr-assets.com/books/1376317909s/8649656.jpg'),('740748475','The Complete Calvin and Hobbes','Bill Watterson','Comics','2005',24.99,14,'Calvin and Hobbes�is unquestionably one of the most popular comic strips of all time. The imaginative world of a boy and his real-only-to-him tiger was first syndicated in 1985 and appeared in more than 2,400 newspapers when Bill Watterson retired on January 1, 1996. The entire body of�Calvin and Hobbescartoons published in a truly noteworthy tribute to this singular cartoon in�The Complete Calvin and Hobbes. Composed of three hardcover, four-color volumes in a sturdy slipcase, this�New York Times�best-selling edition includes all�Calvin and Hobbescartoons that ever appeared in syndication. This is the treasure that all�Calvin and Hobbes�fans seek.',4.82,28900,120,154,693,3117,25884,'https://images.gr-assets.com/books/1473064526m/24812.jpg','https://images.gr-assets.com/books/1473064526s/24812.jpg'),('743223136','John Adams','David McCullough','History','2001',18.99,38,'In this powerful, epic biography, David McCullough unfolds the adventurous life-journey of John Adams, the brilliant, fiercely independent, often irascible, always honest Yankee patriot -- \'the colossus of independence,\' as Thomas Jefferson called him -- who spared nothing in his zeal for the American Revolution; who rose to become the second President of the United States and saved the country from blundering into an unnecessary war; who was learned beyond all but a few and regarded by some as \'out of his senses\'; and whose marriage to the wise and valiant Abigail Adams is one of the moving love stories in American history.�',4.05,215780,11255,10372,30772,70601,97127,'https://images.gr-assets.com/books/1478144278m/2203.jpg','https://images.gr-assets.com/books/1478144278s/2203.jpg'),('767919386','At Home: A Short History of Private Life','Bill Bryson','History','2010',11.99,80,'Bill Bryson and his family live in a Victorian parsonage in a part of England where nothing of any great significance has happened since the Romans decamped. Yet one day, he began to consider how very little he knew about the ordinary things of life as he found it in that comfortable home. To remedy this, he formed the idea of journeying about his house from room to room to �write a history of the world without leaving home.� The bathroom provides the occasion for a history of hygiene; the bedroom, sex, death, and sleep; the kitchen, nutrition and the spice trade; and so on, as Bryson shows how each has figured in the evolution of private life. Whatever happens in the world, he demonstrates, ends up in our house, in the paint and the pipes and the pillows and every item of furniture.',3.96,55296,995,2954,13153,24324,19627,'https://images.gr-assets.com/books/1372727082m/7507825.jpg','https://images.gr-assets.com/books/1372727082s/7507825.jpg'),('785819118','On the Origin of Species by Means of Natural Selection or the Preservation of Favoured Races in the Struggle for Life','Charles Darwin','Science','1859',12.99,24,'Darwin\'s theory of natural selection issued a profound challenge to orthodox thought and belief: no being or species has been specifically created; all are locked into a pitiless struggle for existence, with extinction looming for those not fitted for the task.�Yet The Origin of Species (1859) is also a humane and inspirational vision of ecological interrelatedness, revealing the complex mutual interdependencies between animal and plant life, climate and physical environment, and - by implication - within the human world. ',3.97,64162,2513,4297,15150,22868,29228,'https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png','https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png'),('804139024','The Martian','Andy Weir','Sci-Fi','2012',12.99,148,'Six days ago, astronaut Mark Watney became one of the first people to walk on Mars.Now, he\'s sure he\'ll be the first person to die there. After a dust storm nearly kills him and forces his crew to evacuate while thinking him dead, Mark finds himself stranded and completely alone with no way to even signal Earth that he\'s alive and even if he could get word out, his supplies would be gone long before a rescue could arrive.',4.39,423344,4114,10856,49200,173861,291671,'https://images.gr-assets.com/books/1413706054m/18007564.jpg','https://images.gr-assets.com/books/1413706054s/18007564.jpg'),('896214400','The Shawshank Redemption','Stephen King','Drama','1982',10.99,37,'In The Shawshank Redemption, a man convicted of bloody murder lives in a prison brutally ruled by a sadistic warden and secretly run by a con who knows all the ropes and pulls all the strings. He has more brains than anyone else in this sinister slammer, and a diabolically cunning plan of revenge that no one can guess until it\'s far too late.',4.52,11499,16,115,1003,3776,7972,'https://images.gr-assets.com/books/1315100686m/39664.jpg','https://images.gr-assets.com/books/1315100686s/39664.jpg');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_image` varchar(25) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(64) NOT NULL,
  `username` varchar(64) NOT NULL,
  `password_hash` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'zowofjouet.jpg','Guillermo','Barquero','guillebarq@gmail.com','Geonidas','pbkdf2:sha256:50000$kS0Lp3eM$085513c1d552a26f53421a512e2e94eb2656f257f8cb9cf1080e18c06e38cedd');
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

-- Dump completed on 2019-07-13  0:38:34
