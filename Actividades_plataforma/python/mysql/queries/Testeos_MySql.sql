USE esquema_libros;

-- select * from libros;
-- INSERT INTO libros (título, num_páginas,created_at,updated_at)
-- VALUES('Estoy guatón, tengo que adelgazar', 179,now(),now());

-- UPDATE libros 
-- SET título = 'Geometría plana y en el espacio', num_páginas = 500,updated_at=now()
-- where id = 2 ;

select * from libros;
delete from libros where id > 5;

select * from libros;
