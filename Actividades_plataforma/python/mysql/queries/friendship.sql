use friendships_schema;

select * from users;

select * from friendships;


INSERT INTO users (first_name, last_name, created_at, updated_at)
value ('Amy','Giver',now(),now()), ('Eli','Byers',now(),now()), ('Marky','Mark',now(),now()), ('Big','Bird',now(),now()),   ('La rana','René',now(),now()),   ('Florencia','Bertotti',now(),now());

INSERT INTO friendships (created_at, updated_at, user_id, friend_id)
VALUE (now(),now(),1,2),(now(),now(),1,4),(now(),now(),1,6),
	  (now(),now(),2,1),(now(),now(),2,3),(now(),now(),2,5),
	  (now(),now(),3,2),(now(),now(),3,5),(now(),now(),4,3),
      (now(),now(),5,1),(now(),now(),5,6),(now(),now(),6,2),
      (now(),now(),5,3);

-- Consulta: muestra las relaciones creadas como se muestra en la imagen de arriba      
SELECT u1.first_name AS nombre, u1.last_name AS apellido, u2.first_name AS nombre2, u2.last_name AS apellido2
FROM friendships AS f
JOIN users AS u1 ON f.user_id = u1.id
JOIN users AS u2 ON f.friend_id = u2.id;

-- Consulta NINJA: Devuelve todos los usuarios que son amigos del primer usuario, asegúrate de que sus nombres se muestren en los resultados.
SELECT u1.first_name AS nombre, u1.last_name AS apellido, u2.first_name AS nombre2, u2.last_name AS apellido2
FROM friendships AS f
JOIN users AS u1 ON f.user_id = u1.id
JOIN users AS u2 ON f.friend_id = u2.id where u1.id = 1;

-- Consulta NINJA: averigua quién tiene más amigos y devuelve la cuenta de sus amigos.
SELECT u1.first_name, u1.last_name, COUNT(f.user_id) AS total_amigos
FROM users AS u1
LEFT JOIN friendships AS f ON f.user_id = u1.id
GROUP BY u1.id
ORDER BY total_amigos DESC
LIMIT 1;

-- Consulta NINJA: Devuelve los amigos del tercer usuario en orden alfabético

SELECT u2.first_name, u2.last_name
FROM friendships AS f
JOIN users AS u1 ON f.user_id = u1.id
JOIN users AS u2 ON f.friend_id = u2.id
WHERE u1.id = 3
ORDER BY u2.first_name ASC;
