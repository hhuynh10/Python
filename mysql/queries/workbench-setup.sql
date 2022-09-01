SELECT * FROM users;
INSERT INTO users (first_name, last_name, email, age)
VALUES ('hung', 'huynh', 'hungpchuynh@gmail.com', 30);
UPDATE users 
SET first_name = 'van'
WHERE id = 1;
DELETE
FROM users
WHERE id = 1;