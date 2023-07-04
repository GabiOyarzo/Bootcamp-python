-- Aplica ingeniería avanzada al esquema_libros del capítulo anterior
use esquema_libros;

DELETE FROM usuarios WHERE id > 0;

ALTER TABLE usuarios AUTO_INCREMENT = 1;

DELETE FROM libros WHERE id > 0;

ALTER TABLE libros AUTO_INCREMENT = 1;

DELETE FROM favoritos WHERE id > 0;

ALTER TABLE favoritos AUTO_INCREMENT = 1;


select * from usuarios;

select * from libros;

select * from favoritos;

-- Consulta: crea 5 usuarios diferentes: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu
INSERT INTO usuarios (nombre, created_at,updated_at)
VALUE ('Jane Austen',now(),now()),
	  ('Emily Dickinson',now(),now()),
      ('Fyodor Dostoevsky',now(),now()),
      ('William Shakespeare',now(),now()),
      ('Lau Tzu',now(),now());
      
-- Consulta: crea 5 libros con los siguientes nombres: C Sharp, Java, Python, PHP, Ruby
INSERT INTO libros (titulo, numpag, created_at, updated_at)
VALUE ('C Sharp',150,now(),now()),
	  ('Java',180,now(),now()),
      ('Python',250,now(),now()),
      ('PHP',100,now(),now()),
      ('Ruby',50,now(),now());

-- Consulta: cambia el nombre del libro de C Sharp a C#

UPDATE libros
SET titulo = 'C#'
WHERE titulo = 'C Sharp';

-- Consulta: cambia el nombre del cuarto usuario a Bill
UPDATE usuarios
SET nombre = 'Bill'
WHERE id = 4;

-- Consulta: haz que el primer usuario marque como favorito los 2 primeros libros
INSERT INTO favoritos (libro_id, usuario_id)
VALUES (1, 1), (2, 1);

-- Consulta: haz que el segundo usuario marque como favorito los primeros 3 libros
INSERT INTO favoritos (libro_id, usuario_id)
VALUES (1, 2), (2, 2),(3,2);

-- Consulta: haz que el tercer usuario marque como favorito los 4 primeros libros
INSERT INTO favoritos (libro_id, usuario_id)
VALUES (1, 3), (2, 3),(3,3),(4,3);

-- Consulta: Haz que el cuarto usuario marque como favorito todos los libros
INSERT INTO favoritos (libro_id, usuario_id)
SELECT id, 4
FROM libros;

-- Consulta: recupera todos los usuarios que marcaron como favorito el tercer libro
SELECT u.*
FROM usuarios u
INNER JOIN favoritos f ON u.id = f.usuario_id
WHERE f.libro_id = 3;

-- Consulta: elimina el primer usuario de los favoritos del tercer libro
DELETE FROM favoritos
WHERE libro_id = 3 AND usuario_id = 1
LIMIT 1;

-- Consulta: Haz que el quinto usuario marque como favorito el segundo libro
INSERT INTO favoritos (libro_id, usuario_id)
VALUES (2, 5);

-- Encuentra todos los libros que el tercer usuario marcó como favoritos
SELECT l.*
FROM libros l
INNER JOIN favoritos f ON l.id = f.libro_id
WHERE f.usuario_id = 3;

-- Consulta: encuentra todos los usuarios que marcaron como favorito el quinto libro
SELECT u.*
FROM usuarios u
INNER JOIN favoritos f ON u.id = f.usuario_id
WHERE f.libro_id = 5;