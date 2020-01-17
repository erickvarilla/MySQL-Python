-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 17-01-2020 a las 22:54:51
-- Versión del servidor: 5.7.26
-- Versión de PHP: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `comic`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compra`
--

DROP TABLE IF EXISTS `compra`;
CREATE TABLE IF NOT EXISTS `compra` (
  `id_compra` int(10) NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de la tabla',
  `id_comic` int(11) NOT NULL COMMENT 'id de la tabla revista',
  `id_persona` int(11) NOT NULL COMMENT 'id de la tabla persona',
  `fecha_compra` datetime NOT NULL COMMENT 'fecha en la que se compra el comic',
  PRIMARY KEY (`id_compra`,`id_comic`,`id_persona`),
  KEY `id_comic` (`id_comic`),
  KEY `id_persona` (`id_persona`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `compra`
--

INSERT INTO `compra` (`id_compra`, `id_comic`, `id_persona`, `fecha_compra`) VALUES
(3, 7, 3, '2020-01-17 17:29:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

DROP TABLE IF EXISTS `persona`;
CREATE TABLE IF NOT EXISTS `persona` (
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL COMMENT 'nombre de la persona',
  `apellido` varchar(100) COLLATE utf8_spanish_ci NOT NULL COMMENT 'apellido de la persona',
  `telefono` varchar(10) COLLATE utf8_spanish_ci NOT NULL COMMENT 'telefono de la persona',
  `dirreccion` varchar(100) COLLATE utf8_spanish_ci NOT NULL COMMENT 'dirrecion de la persona',
  `email` varchar(100) COLLATE utf8_spanish_ci NOT NULL COMMENT 'email de la persona',
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `identificacion` int(30) NOT NULL COMMENT 'identificacion de la persona',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `persona`
--

INSERT INTO `persona` (`nombre`, `apellido`, `telefono`, `dirreccion`, `email`, `id`, `identificacion`) VALUES
('felipe', 'tirado', '3116542233', 'calle 11 # 3-22', 'felipe@gmail.com', 2, 198543276),
('Fabien', 'Herrera', '311223344', 'calle 21 #4-12', 'fabien@hotmail.com', 3, 1234589);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `revista`
--

DROP TABLE IF EXISTS `revista`;
CREATE TABLE IF NOT EXISTS `revista` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Llave primaria',
  `nombre_comic` varchar(100) COLLATE utf8_spanish_ci NOT NULL COMMENT 'nombre del comic',
  `autor` varchar(100) COLLATE utf8_spanish_ci NOT NULL COMMENT 'autor del comic',
  `fecha` datetime NOT NULL COMMENT 'fecha que se lanza el comic',
  `precio` double NOT NULL COMMENT 'precio del comic',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `revista`
--

INSERT INTO `revista` (`id`, `nombre_comic`, `autor`, `fecha`, `precio`) VALUES
(1, 'flash', 'hernando', '2019-10-10 00:00:00', 1234),
(3, 'franquistan', 'franb', '2018-03-12 00:00:00', 4.99),
(4, 'w', 'SD', '2020-12-12 00:00:00', 3.2),
(5, 'D', 'D', '2000-12-12 00:00:00', 2),
(6, 'Batman', 'Word', '2013-03-09 00:00:00', 34.21),
(7, 'SuperMan', 'Disney', '1999-02-22 00:00:00', 12.99);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
