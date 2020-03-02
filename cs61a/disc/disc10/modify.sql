CREATE TABLE dogs(name, age, phrase DEFAULT "woof");
INSERT INTO dogs(name, age) VALUES ("Fido", 1), ("Sparky", 2);
INSERT INTO dogs VALUES ("Lassie", 2, "I'll save you!"), ("Fllofy", 3, "Much doge!");
SELECT * FROM dogs;

UPDATE dogs SET age=age+1;
SELECT * FROM dogs;

UPDATE dogs SET phrase="bark" WHERE age=2;
SELECT * FROM dogs;

DELETE FROM dogs WHERE age=3;
SELECT * FROM dogs;

.schema
DROP TABLE dogs;


CREATE TABLE dogs(name, age, phrase DEFAULT "woof");
INSERT INTO dogs(name, age) VALUES ("Fido", 1), ("Sparky", 2);
INSERT INTO dogs VALUES ("Lassie", 2, "I'll save you!"), ("Fllofy", 3, "Much doge!");

INSERT INTO dogs(age, name) VALUES ("Rover", 3);
SELECT * FROM dogs;

UPDATE dogs SET name=age, age=name WHERE name=3;
SELECT * FROM dogs;

DELETE FROM dogs WHERE age<3;
SELECT * FROM dogs;
