-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 06, 2019 at 11:35 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `movies`
--

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
CREATE TABLE IF NOT EXISTS `movie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ac_id` int(11) NOT NULL,
  `titre` varchar(512) DEFAULT NULL,
  `cover` varchar(512) DEFAULT NULL,
  `date_sortie` varchar(256) DEFAULT NULL,
  `durree` varchar(256) DEFAULT NULL,
  `nationalite` varchar(256) DEFAULT NULL,
  `acteurs` varchar(512) DEFAULT NULL,
  `genres` varchar(512) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf16;
COMMIT;
