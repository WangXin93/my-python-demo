/* (a) */
CREATE TABLE cats(name, weight DEFAULT 1, notes DEFAULT "meow");

INSERT INTO cats(name) VALUES ("Tom"), ("Whiskers");
SELECT * FROM cats;

INSERT INTO cats VALUES
    ("Mittens", 2, "Actually like shoes"),
    ("Rascal", 4, "Prefers to associate with dogs"),
    ("Magic", 2, "Expert at card games");
SELECT * FROM cats ORDER BY weight, name;

UPDATE cats SET notes="A cat" WHERE notes="meow";
SELECT name FROM cats WHERE notes="A cat";

/* (b) */
CREATE TABLE food AS
    SELECT 1 AS cat_weight, 0.5 AS amount UNION
    SELECT 2 , 2.5 UNION
    SELECT 3 , 4.0 UNION
    SELECT 4 , 4.5;
SELECT SUM(b.amount) FROM cats as a, food as b
    WHERE a.weight=b.cat_weight;
