INSERT INTO users (first_name, last_name, email)
VALUES ('Hung', 'Huynh', 'hhuynh@gmail.com');
INSERT INTO users (first_name, last_name, email)
VALUES ('Julian', 'Auza', 'jauza@gmail.com');
INSERT INTO users (first_name, last_name, email)
VALUES ('Michael', 'Cahill', 'mcahill@gmail.com');
SELECT * from users;
SELECT email 
FROM users
WHERE id = 1;
SELECT * FROM users
WHERE id = 3;
UPDATE users
SET last_name = 'Pancakes'
WHERE id = 3;
DELETE FROM users
WHERE id = 2;
SELECT first_name
FROM users;
SELECT * FROM users
ORDER BY first_name DESC;