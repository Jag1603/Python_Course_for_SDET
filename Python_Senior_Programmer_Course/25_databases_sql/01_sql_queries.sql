CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, role TEXT);
INSERT INTO users(name, role) VALUES ('Ada', 'admin');
SELECT * FROM users WHERE role = 'admin';