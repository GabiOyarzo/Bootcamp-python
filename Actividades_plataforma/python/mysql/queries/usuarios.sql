use esquema_usuarios;
select * from users;
INSERT INTO users (first_name,last_name,email,password,created_at,updated_at)
VALUES('Gabriela','Oyarzo','gabioyarzoe@gmail.com','contraseña1',now(),now());

INSERT INTO users (first_name,last_name,email,password,created_at,updated_at)
VALUES('Fernanda','Escudero','rocalia2@gmail.com','contraseña1',now(),now());

INSERT INTO users (first_name,last_name,email,password,created_at,updated_at)
VALUES('Alexandrium','Catenella','alexandrium@zooplankton.com','contraseña1',now(),now());

select first_name 
from users
where email = 'gabioyarzoe@gmail.com';

select first_name 
from users
where id = (SELECT MAX(id) FROM users);

UPDATE users
SET last_name = 'Panqueques'
WHERE id = 3;

delete from users where id = 2;
select * from users;

select * 
from users
order by first_name;

select * 
from users
order by first_name DESC;