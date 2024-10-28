-- Eliminamos los datos al inicio
delete from libreria_autor;
-- Ponemos el numero que se autoincrementa en 0
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='libreria_autor';
-- Insertamos los datos
-- Autores
INSERT INTO libreria_autor VALUES (1, 'Jason R. Weiss');
INSERT INTO libreria_autor VALUES (2, 'Peter Small');
INSERT INTO libreria_autor VALUES (3, 'Spencer Salazar');
INSERT INTO libreria_autor VALUES (4, 'Ahmed Sidky');
INSERT INTO libreria_autor VALUES (5, 'Jonathan Anstey');
INSERT INTO libreria_autor VALUES (6, 'Leo S. Hsu');
INSERT INTO libreria_autor VALUES (7, 'Dmitry Babenko');
INSERT INTO libreria_autor VALUES (8, 'Brandon Goodin');