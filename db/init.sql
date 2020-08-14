CREATE DATABASE if not exists task_sqlalchemy;

use task_sqlalchemy;

CREATE TABLE `items` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `created_at` timestamp(50) DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `item_pics` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `items_id` int(50) DEFAULT NULL,
  `pic_name` varchar(50) DEFAULT NULL,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `user` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `useremail` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;