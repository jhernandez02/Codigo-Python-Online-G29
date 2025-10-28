CREATE TABLE `categorias` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255)
);

CREATE TABLE `instructores` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombres` varchar(255),
  `apellidos` varchar(255)
);

CREATE TABLE `horarios` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255),
  `descripcion` varchar(255)
);

CREATE TABLE `cursos` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `codigo` char(8),
  `nombre` varchar(150),
  `descripcion` text,
  `temario` text,
  `precio` decimal(7,2),
  `horas` integer,
  `categoria_id` integer NOT NULL,
  `horario_id` integer NOT NULL,
  `instructor_id` integer NOT NULL
);

ALTER TABLE `cursos` ADD FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id`);

ALTER TABLE `cursos` ADD FOREIGN KEY (`horario_id`) REFERENCES `horarios` (`id`);

ALTER TABLE `cursos` ADD FOREIGN KEY (`instructor_id`) REFERENCES `instructores` (`id`);
