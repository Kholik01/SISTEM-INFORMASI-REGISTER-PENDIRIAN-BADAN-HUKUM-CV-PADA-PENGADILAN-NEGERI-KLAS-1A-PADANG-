-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 11, 2026 at 05:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hukum`
--

-- --------------------------------------------------------

--
-- Table structure for table `loginadmin`
--

CREATE TABLE `loginadmin` (
  `nik` varchar(20) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `nama_petugas` varchar(100) NOT NULL,
  `user_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notaris`
--

CREATE TABLE `notaris` (
  `kd_notaris` varchar(10) NOT NULL,
  `nm_notaris` varchar(100) NOT NULL,
  `jk` enum('L','P') NOT NULL,
  `almt_notaris` varchar(200) DEFAULT NULL,
  `no_tlp` varchar(20) DEFAULT NULL,
  `nik` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notaris`
--

INSERT INTO `notaris` (`kd_notaris`, `nm_notaris`, `jk`, `almt_notaris`, `no_tlp`, `nik`) VALUES
('002', 'koamma', 'L', 'kemabngjati', '0298339', NULL),
('2634', 'akbar', 'L', 'jaya', '0853', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `pemilik`
--

CREATE TABLE `pemilik` (
  `kd_pemilik` varchar(10) NOT NULL,
  `nm_pemilik` varchar(100) NOT NULL,
  `jk` enum('L','P') NOT NULL,
  `almt_pemilik` varchar(200) DEFAULT NULL,
  `no_tlp` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pemilik`
--

INSERT INTO `pemilik` (`kd_pemilik`, `nm_pemilik`, `jk`, `almt_pemilik`, `no_tlp`) VALUES
('018', 'ilham', 'L', 'hasan basri', '08527437'),
('023', 'bowo', 'L', '', ''),
('111', 'pra bwo', 'P', 'aluh aluh', '092738938');

-- --------------------------------------------------------

--
-- Table structure for table `prosesregister`
--

CREATE TABLE `prosesregister` (
  `no_register` varchar(10) NOT NULL,
  `tgl_register` date NOT NULL,
  `berkas_pendirian` varchar(100) DEFAULT NULL,
  `keterangan` text DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `kd_cv` varchar(10) DEFAULT NULL,
  `kd_pemilik` varchar(10) DEFAULT NULL,
  `nik` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `register_cv`
--

CREATE TABLE `register_cv` (
  `no_register` varchar(20) NOT NULL,
  `kode_cv` varchar(20) NOT NULL,
  `nama_cv` varchar(100) NOT NULL,
  `alamat_cv` varchar(200) DEFAULT NULL,
  `tgl_berdiri` date DEFAULT NULL,
  `notaris` varchar(100) DEFAULT NULL,
  `modal` decimal(15,2) DEFAULT NULL,
  `jangka_berdiri` varchar(50) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register_cv`
--

INSERT INTO `register_cv` (`no_register`, `kode_cv`, `nama_cv`, `alamat_cv`, `tgl_berdiri`, `notaris`, `modal`, `jangka_berdiri`, `status`) VALUES
('REG001', 'CV001', 'CV MAJU JAYA', 'Padang', '2018-01-10', 'Notaris Andi, SH', 50000000.00, '10 Tahun', 'AKTIF'),
('REG002', 'CV002', 'CV SEJAHTERA BERSAMA', 'Padang', '2018-05-21', 'Notaris Andi, SH', 75000000.00, '10 Tahun', 'AKTIF'),
('REG003', 'CV003', 'CV SUMBER REZEKI', 'Bukittinggi', '2019-03-15', 'Notaris Rina, SH', 60000000.00, '5 Tahun', 'AKTIF'),
('REG004', 'CV004', 'CV MITRA USAHA', 'Payakumbuh', '2019-07-02', 'Notaris Rina, SH', 45000000.00, '5 Tahun', 'AKTIF'),
('REG005', 'CV005', 'CV CAHAYA ABADI', 'Padang', '2020-01-08', 'Notaris Dedi, SH', 90000000.00, '10 Tahun', 'AKTIF'),
('REG006', 'CV006', 'CV BERKAH JAYA', 'Padang Pariaman', '2020-04-17', 'Notaris Dedi, SH', 30000000.00, '5 Tahun', 'AKTIF'),
('REG007', 'CV007', 'CV ANUGERAH MANDIRI', 'Solok', '2020-09-12', 'Notaris Lina, SH', 55000000.00, '5 Tahun', 'AKTIF'),
('REG008', 'CV008', 'CV KARYA BERSAMA', 'Padang', '2021-02-20', 'Notaris Lina, SH', 70000000.00, '10 Tahun', 'AKTIF'),
('REG009', 'CV009', 'CV BINTANG UTAMA', 'Bukittinggi', '2021-06-11', 'Notaris Andi, SH', 65000000.00, '5 Tahun', 'AKTIF'),
('REG010', 'CV010', 'CV SENTOSA ABADI', 'Padang', '2021-11-03', 'Notaris Dedi, SH', 80000000.00, '10 Tahun', 'AKTIF'),
('REG011', 'CV011', 'CV HARAPAN BARU', 'Padang', '2022-01-19', 'Notaris Rina, SH', 40000000.00, '5 Tahun', 'AKTIF'),
('REG012', 'CV012', 'CV GLOBAL NIAGA', 'Padang', '2022-04-07', 'Notaris Lina, SH', 120000000.00, '10 Tahun', 'AKTIF'),
('REG013', 'CV013', 'CV PRIMA JAYA', 'Solok', '2022-07-22', 'Notaris Andi, SH', 95000000.00, '10 Tahun', 'AKTIF'),
('REG014', 'CV014', 'CV BERSAMA MAJU', 'Payakumbuh', '2022-10-14', 'Notaris Rina, SH', 50000000.00, '5 Tahun', 'AKTIF'),
('REG015', 'CV015', 'CV MITRA KENCANA', 'Padang', '2023-02-05', 'Notaris Lina, SH', 65000000.00, '5 Tahun', 'AKTIF'),
('REG016', 'CV016', 'CV USAHA MAKMUR', 'Padang', '2023-04-18', 'Notaris Dedi, SH', 70000000.00, '10 Tahun', 'AKTIF'),
('REG017', 'CV017', 'CV NUSANTARA JAYA', 'Bukittinggi', '2023-06-30', 'Notaris Andi, SH', 85000000.00, '10 Tahun', 'AKTIF'),
('REG018', 'CV018', 'CV SINAR ABADI', 'Padang Pariaman', '2023-09-12', 'Notaris Lina, SH', 55000000.00, '5 Tahun', 'AKTIF'),
('REG019', 'CV019', 'CV BERKAH UTAMA', 'Solok', '2024-01-08', 'Notaris Rina, SH', 60000000.00, '5 Tahun', 'AKTIF'),
('REG020', 'CV020', 'CV MAKMUR SENTOSA', 'Padang', '2024-03-21', 'Notaris Andi, SH', 100000000.00, '10 Tahun', 'AKTIF');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `loginadmin`
--
ALTER TABLE `loginadmin`
  ADD PRIMARY KEY (`nik`);

--
-- Indexes for table `notaris`
--
ALTER TABLE `notaris`
  ADD PRIMARY KEY (`kd_notaris`),
  ADD KEY `fk_notaris_admin` (`nik`);

--
-- Indexes for table `pemilik`
--
ALTER TABLE `pemilik`
  ADD PRIMARY KEY (`kd_pemilik`);

--
-- Indexes for table `prosesregister`
--
ALTER TABLE `prosesregister`
  ADD PRIMARY KEY (`no_register`),
  ADD KEY `kd_cv` (`kd_cv`),
  ADD KEY `kd_pemilik` (`kd_pemilik`),
  ADD KEY `nik` (`nik`);

--
-- Indexes for table `register_cv`
--
ALTER TABLE `register_cv`
  ADD PRIMARY KEY (`no_register`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `notaris`
--
ALTER TABLE `notaris`
  ADD CONSTRAINT `fk_notaris_admin` FOREIGN KEY (`nik`) REFERENCES `loginadmin` (`nik`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `prosesregister`
--
ALTER TABLE `prosesregister`
  ADD CONSTRAINT `prosesregister_ibfk_1` FOREIGN KEY (`kd_cv`) REFERENCES `cv` (`kd_cv`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `prosesregister_ibfk_2` FOREIGN KEY (`kd_pemilik`) REFERENCES `pemilik` (`kd_pemilik`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `prosesregister_ibfk_3` FOREIGN KEY (`nik`) REFERENCES `loginadmin` (`nik`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
