-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 28, 2016 at 12:56 AM
-- Server version: 10.1.8-MariaDB
-- PHP Version: 5.6.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `laundry`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(10) NOT NULL,
  `user` varchar(255) NOT NULL,
  `pswd` varchar(255) NOT NULL,
  `akses` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  `hp` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `user`, `pswd`, `akses`, `alamat`, `hp`, `email`) VALUES
(1, 'Admin', 'Admin', 'Admin', 'Admin', 'Admin', 'Admin'),
(37, 'asdasd', 'asdasd', 'anggota', 'asdasd', 'asdasd', 'asdasd'),
(38, 'Gilang', 'aditya', 'anggota', 'rahman', '08130182412', 'gilangasdas'),
(39, 'Gilang', 'asdasd', 'anggota', 'asdasdas', 'asdasd', 'asdsad'),
(40, 'Gilang', 'asdasd', 'anggota', 'asdasd', 'asdasd', 'asdasd'),
(41, 'Gilang', 'asdasd', 'anggota', 'asdasdas', 'asdasd', 'asdasd'),
(42, 'Gilang aditya ', 'toor', 'anggota', 'Taman puri cendana 2', '081310821647', 'kikchiemedia@gmail.com'),
(43, 'Gilang', '01923012', 'anggota', 'Tamanaasdas', '08989238', '892839'),
(44, 'Gilang', 'asdas', 'anggota', 'asdasd', 'asdas', 'asdasd'),
(45, 'Gilang', 'asdasd', 'anggota', 'asdasd', 'asdasd', 'asdasd'),
(46, 'Gilang', 'asdas', 'anggota', 'asdas', 'asdasd', 'asdas'),
(47, 'Gilang', 'asdas', 'anggota', 'asdas', 'asdas', 'asdas'),
(48, 'Gilang', 'asdas', 'anggota', 'asdsad', 'asdas', 'asdas'),
(49, 'Gilang', 'aditya', 'anggota', 'asdas', 'asdasd', 'asdasd'),
(50, 'asdasd', 'asdasd', 'anggota', 'asdasd', 'asdasd', 'asdasd'),
(51, 'Gilang', 'asdas', 'anggota', 'asdas', 'asdasd', 'asdasd'),
(52, 'Gilang', 'asdasd', 'anggota', 'asdasd', 'asdasd', 'sadas'),
(53, 'Gilang', 'asdas', 'anggota', 'asdas', 'asdas', 'asdas'),
(54, 'Gilang', 'golgolgol', 'Anggota', 'asdasdas', 'asdasd', 'asdasd'),
(55, 'lolo', 'invite me', 'Anggota', 'kumpulbagi', 'bagikumpul', 'anjay@gmail.com'),
(56, 'taijutsu', 'asdasd', 'Anggota', 'wewee', 'wewrrt', 'qwwee');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
