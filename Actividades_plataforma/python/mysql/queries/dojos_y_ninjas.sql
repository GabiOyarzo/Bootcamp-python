use esquema_dojos_y_ninjas;

SELECT * FROM dojos;

INSERT INTO dojos (nombre,created_at,updated_at)
VALUES('ECM - Altamirano',now(),now());
INSERT INTO dojos (nombre,created_at,updated_at)
VALUES('ECM - Curauma',now(),now());
INSERT INTO dojos (nombre,created_at,updated_at)
VALUES('ECM - Huinay',now(),now());

delete from dojos;
SELECT * FROM dojos;

INSERT INTO dojos (nombre,created_at,updated_at)
VALUES('PUCV',now(),now());
INSERT INTO dojos (nombre,created_at,updated_at)
VALUES('UV',now(),now());
INSERT INTO dojos (nombre,created_at,updated_at)
VALUES('UDEC',now(),now());

INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (1, 'Gabriela', 'Oyarzo', 27, NOW(), NOW());

SELECT * FROM ninjas;
