DROP database IF EXISTS Portfolio;
create database Portfolio;
use Portfolio;
DROP TABLE IF EXISTS `Equipo`;

CREATE TABLE `usuario` (
  `Email` VARCHAR(40) not NULL,
  `Contraseña` VARCHAR(200) not NULL
);

CREATE TABLE `info` (
   id int auto_increment primary key,
  `tipo` VARCHAR(50),
  `tamano` BIGINT,
  `pixel` LONGBLOB,
  `sobre_mi` VARCHAR(400) not NULL,
  `tel` VARCHAR(400) not NULL,
  `mail` VARCHAR(400) not NULL,
  `dir` VARCHAR(400) not NULL,
  `edad` int not NULL
);
CREATE TABLE `Experiencia` (
  id int auto_increment primary key,
  exp VARCHAR(400) not NULL
);

CREATE TABLE `Proyectos` (
 id int auto_increment primary key,
 `tipo` VARCHAR(50),
 `tamano` BIGINT,
 `pixel` LONGBLOB,
 `descripcion` VARCHAR(400) not NULL,
 `titulo` VARCHAR(50) not NULL,
 `link` VARCHAR(100) not NULL
);

CREATE TABLE `EDUCACIÓN` (
id int auto_increment primary key,
  edu VARCHAR(400) not NULL
);

create TABLE `links` (
   id int auto_increment primary key,
  `name` VARCHAR(400) not NULL,
  `url` VARCHAR(400) not NULL
);

insert into Portfolio.usuario values ('yuro2105@gmail.com', 'scrypt:32768:8:1$dOxTmky4Y7jQwiuA$082705d7615c5bc3573d42bd3a74976cd62385090f1ab7ee7179c8447bfd9f1cf160d6b36a43591719e36fcef3c246c4f1dedc428b9b125ede8ec2bf5bee9da5'
);
