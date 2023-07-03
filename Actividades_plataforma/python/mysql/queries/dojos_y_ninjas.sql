USE esquema_dojos_y_ninjas;

USE esquema_dojos_y_ninjas;

-- Eliminar todos los registros de la tabla ninjas
DELETE FROM ninjas;

-- Reiniciar el contador de identidad (auto_increment) para la tabla ninjas
ALTER TABLE ninjas AUTO_INCREMENT = 1;

-- Eliminar todos los registros de la tabla dojos
DELETE FROM dojos;

-- Reiniciar el contador de identidad (auto_increment) para la tabla dojos
ALTER TABLE dojos AUTO_INCREMENT = 1;

-- Insertar nuevos registros en la tabla dojos
INSERT INTO dojos (nombre, created_at, updated_at)
VALUES ('ECM - Altamirano', NOW(), NOW());
INSERT INTO dojos (nombre, created_at, updated_at)
VALUES ('ECM - Curauma', NOW(), NOW());
INSERT INTO dojos (nombre, created_at, updated_at)
VALUES ('ECM - Huinay', NOW(), NOW());

-- Mostrar los registros actualizados en la tabla dojos
SELECT * FROM dojos;

-- Insertar nuevos registros en la tabla dojos
INSERT INTO dojos (nombre, created_at, updated_at)
VALUES ('PUCV', NOW(), NOW());
INSERT INTO dojos (nombre, created_at, updated_at)
VALUES ('UV', NOW(), NOW());
INSERT INTO dojos (nombre, created_at, updated_at)
VALUES ('UDEC', NOW(), NOW());

-- Insertar nuevos registros en la tabla ninjas asociada al dojo 1
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (1, 'Miki', 'Koichikawa', 15, NOW(), NOW());
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (1, 'Yuu', 'Matsuda', 16, NOW(), NOW());
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (1, 'Meiko', 'Akizuki', 14, NOW(), NOW());

-- Insertar nuevos registros en la tabla ninjas asociada al dojo 2
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (2, 'Ginta', 'Suou', 15, NOW(), NOW());
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (2, 'Satoshi', 'Miwa', 17, NOW(), NOW());
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (2, 'Arimi', 'Akizuki', 15, NOW(), NOW());

-- Insertar nuevos registros en la tabla ninjas asociada al dojo 2
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (3, 'Shinichi', 'Namura', 30, NOW(), NOW());
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (3, 'Ryoko', 'Momoi', 29, NOW(), NOW());
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (3, 'Takuji', 'Kijima', 31, NOW(), NOW());

-- Mostrar los registros de la tabla dojos
SELECT * FROM dojos;

SELECT first_name
FROM ninjas
where dojo_id = 1;

SELECT first_name
FROM ninjas
where dojo_id = 3;

SELECT d.*
FROM dojos d
INNER JOIN (
  SELECT dojo_id
  FROM ninjas
  ORDER BY id DESC
  LIMIT 1
) n ON d.id = n.dojo_id;

