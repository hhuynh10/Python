INSERT INTO dojos (name)
VALUES ('Chicago'), ('Los Angeles'), ('Seatle');
DELETE FROM dojos
WHERE id = 1 and id = 2 and id = 3;
INSERT INTO dojos (name)
VALUES ('Chicago'), ('Los Angeles'), ('Seatle');
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Mike', 'Cahill', 27, 4), ('Hung','Huynh', 29, 4), ('Julian','Auza', 30, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Don', 'Henningan', 24, 5), ('Julia','Vo', 31, 5), ('Franzlei','Luson', 30, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Van', 'Manalo', 32, 6), ('Dan','Kim', 29, 6), ('Shannon','Mullaney', 34, 6);
SELECT * FROM ninjas 
LEFT JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 4;
SELECT * FROM ninjas 
LEFT JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 6;
SELECT * FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);