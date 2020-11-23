-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Nov 20, 2020 at 02:38 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ikeo2`
--

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

CREATE TABLE `clients` (
  `id_c` int(3) UNSIGNED NOT NULL,
  `raison_c` varchar(55) NOT NULL,
  `adresse_c` varchar(255) NOT NULL,
  `type_c` varchar(55) NOT NULL,
  `ville_c` varchar(55) NOT NULL,
  `pays_c` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `clients`
--

INSERT INTO `clients` (`id_c`, `raison_c`, `adresse_c`, `type_c`, `ville_c`, `pays_c`) VALUES
(1, 'Bo Meuble', 'Place Vendôme', 'Magasin', 'Paris', 'France'),
(2, 'Mobel', 'Porte de Brandebourg', 'Magasin', 'Berlin', 'Allemagne'),
(4, 'Tout A La Maison', 'Rue de la Bastille', 'Magasin', 'Paris', 'France'),
(5, 'Bo Meuble', 'Avenue des Trois Dragons', 'Magasin', 'Barcelone', 'Espagne'),
(6, 'The World Compagny', 'Oxford street', 'Central d\'achat', 'Londres', 'Angleterre'),
(7, 'The Best Greatest BeautifulestFurniture', 'Coven Garden', 'Magasin', 'Londres', 'Angleterre');

-- --------------------------------------------------------

--
-- Table structure for table `commandes`
--

CREATE TABLE `commandes` (
  `id_co` int(3) UNSIGNED NOT NULL,
  `id_p` int(3) UNSIGNED NOT NULL,
  `quantite_co` int(3) UNSIGNED NOT NULL,
  `id_f` int(3) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `commandes`
--

INSERT INTO `commandes` (`id_co`, `id_p`, `quantite_co`, `id_f`) VALUES
(1, 1, 20, 1),
(2, 2, 30, 1),
(3, 3, 10, 1),
(4, 8, 25, 2),
(5, 4, 32, 2),
(6, 3, 80, 3),
(7, 5, 70, 3),
(8, 6, 60, 3),
(9, 4, 60, 3),
(10, 9, 120, 3),
(11, 7, 90, 3),
(12, 1, 10, 4),
(13, 2, 10, 4),
(14, 6, 30, 4),
(15, 1, 25, 5),
(16, 7, 34, 5),
(17, 2, 40, 6),
(18, 5, 38, 6),
(19, 6, 54, 6),
(20, 4, 20, 7),
(21, 5, 34, 7),
(22, 6, 45, 7);

-- --------------------------------------------------------

--
-- Table structure for table `factures`
--

CREATE TABLE `factures` (
  `id_f` int(3) UNSIGNED NOT NULL,
  `date_f` date NOT NULL,
  `id_c` int(3) UNSIGNED NOT NULL,
  `numero_f` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `factures`
--

INSERT INTO `factures` (`id_f`, `date_f`, `id_c`, `numero_f`) VALUES
(1, '2018-06-15', 1, 'MSQ291'),
(2, '2018-06-23', 5, 'MSQ292'),
(3, '2018-06-23', 6, 'MSQ293'),
(4, '2018-06-28', 1, 'MSQ294'),
(5, '2018-07-01', 4, 'MSQ295'),
(6, '2018-07-04', 6, 'MSQ296'),
(7, '2018-07-12', 2, 'MSQ297');

-- --------------------------------------------------------

--
-- Table structure for table `produits`
--

CREATE TABLE `produits` (
  `id_p` int(3) UNSIGNED NOT NULL,
  `nom_p` varchar(55) NOT NULL,
  `ref_p` varchar(55) NOT NULL,
  `descrip_p` varchar(255) NOT NULL,
  `abandon_p` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `produits`
--

INSERT INTO `produits` (`id_p`, `nom_p`, `ref_p`, `descrip_p`, `abandon_p`) VALUES
(1, 'Knutsen', 'OANT72', 'Table basse pour poser les bières', 0),
(2, 'Moen', 'OANT34', 'Chaise haute de bar', 1),
(3, 'Eide', 'OANT67', 'Porte-serviettes pour 100 serviettes', 0),
(4, 'Gulbrandsen', 'LXAL34', 'Lit nuage en lévitation', 0),
(5, 'Naess', 'LXAL56', 'Table 128 convives', 0),
(6, 'Lund', 'LXAL 78', 'Bureau-cafetière électrique', 0),
(7, 'Dahl', 'LXAL12', 'Tiroir à rond de serviette', 1),
(8, 'Ruud', 'OANT90', 'Bureau-lit conbiné', 0),
(9, 'Apfelgluk', 'OANT12', 'Panier à chien (ou à chat)', 0);

-- --------------------------------------------------------

--
-- Table structure for table `produits_usines`
--

CREATE TABLE `produits_usines` (
  `id_pu` int(3) UNSIGNED NOT NULL,
  `usine_id` int(3) UNSIGNED NOT NULL,
  `produit_id` int(3) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `produits_usines`
--

INSERT INTO `produits_usines` (`id_pu`, `usine_id`, `produit_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 1, 2),
(4, 2, 2),
(5, 1, 3),
(6, 3, 3),
(7, 3, 4),
(8, 1, 5),
(9, 2, 5),
(10, 3, 5),
(11, 1, 6),
(12, 3, 6),
(13, 2, 7),
(14, 3, 7),
(15, 3, 8),
(16, 3, 9);

-- --------------------------------------------------------

--
-- Table structure for table `usines`
--

CREATE TABLE `usines` (
  `id_u` int(3) UNSIGNED NOT NULL,
  `nom_u` varchar(55) NOT NULL,
  `adresse_u` varchar(255) NOT NULL,
  `ville_u` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usines`
--

INSERT INTO `usines` (`id_u`, `nom_u`, `adresse_u`, `ville_u`) VALUES
(1, 'Harald', 'Quai Pipervika', 'Oslo'),
(2, 'Sverre', 'Rue Strangehagen', 'Bergen'),
(3, 'Olaf', 'Place Nidaros', 'Trondheim');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`id_c`);

--
-- Indexes for table `commandes`
--
ALTER TABLE `commandes`
  ADD PRIMARY KEY (`id_co`),
  ADD KEY `fk_co_p` (`id_p`),
  ADD KEY `fk_co_f` (`id_f`);

--
-- Indexes for table `factures`
--
ALTER TABLE `factures`
  ADD PRIMARY KEY (`id_f`),
  ADD KEY `fk_f_c` (`id_c`);

--
-- Indexes for table `produits`
--
ALTER TABLE `produits`
  ADD PRIMARY KEY (`id_p`);

--
-- Indexes for table `produits_usines`
--
ALTER TABLE `produits_usines`
  ADD PRIMARY KEY (`id_pu`),
  ADD KEY `fk_pu_u` (`usine_id`),
  ADD KEY `fk_pu_p` (`produit_id`);

--
-- Indexes for table `usines`
--
ALTER TABLE `usines`
  ADD PRIMARY KEY (`id_u`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clients`
--
ALTER TABLE `clients`
  MODIFY `id_c` int(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `commandes`
--
ALTER TABLE `commandes`
  MODIFY `id_co` int(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `factures`
--
ALTER TABLE `factures`
  MODIFY `id_f` int(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `produits`
--
ALTER TABLE `produits`
  MODIFY `id_p` int(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `produits_usines`
--
ALTER TABLE `produits_usines`
  MODIFY `id_pu` int(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `usines`
--
ALTER TABLE `usines`
  MODIFY `id_u` int(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `commandes`
--
ALTER TABLE `commandes`
  ADD CONSTRAINT `fk_co_f` FOREIGN KEY (`id_f`) REFERENCES `factures` (`id_f`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_co_p` FOREIGN KEY (`id_p`) REFERENCES `produits` (`id_p`);

--
-- Constraints for table `factures`
--
ALTER TABLE `factures`
  ADD CONSTRAINT `fk_f_c` FOREIGN KEY (`id_c`) REFERENCES `clients` (`id_c`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `produits_usines`
--
ALTER TABLE `produits_usines`
  ADD CONSTRAINT `fk_pu_p` FOREIGN KEY (`produit_id`) REFERENCES `produits` (`id_p`),
  ADD CONSTRAINT `fk_pu_u` FOREIGN KEY (`usine_id`) REFERENCES `usines` (`id_u`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
