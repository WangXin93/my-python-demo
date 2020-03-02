CREATE TABLE records AS
  SELECT "Ben Bitdiddle" AS name , "Computer" AS division, "Wizard" AS title, 60000 AS salary, "Oliver Warbucks" AS supervisor UNION
  SELECT "Alyssa P Hacker"       , "Computer"            , "Programmer"     , 40000          , "Ben Bitdiddle"                 UNION
  SELECT "Cy D Fect"             , "Computer"            , "Programmer"     , 35000          , "Ben Bitdiddle"                 UNION
  SELECT "Lem E Tweakit"         , "Computer"            , "Technician"     , 25000          , "Ben Bitdiddle"                 UNION
  SELECT "Louis Reasoner"        , "Computer"            , "Programmer Trainee", 30000       , "Alyssa P Hacker"               UNION
  SELECT "Oliver Warbucks"       , "Administration"      , "Big Wheel"      , 150000         , "Oliver Warbucks"               UNION
  SELECT "Eben Scrooge"          , "Accounting"          , "Chief Accountant", 75000         , "Oliver Warbucks"               UNION
  SELECT "Robert Cratchet"       , "Accounting"          , "Scrivener"      , 18000          , "Eben Scrooge";

/* Q2.1 */
SELECT name FROM records WHERE supervisor="Oliver Warbucks";

/* Q2.2 */
SELECT * FROM records WHERE records.name = records.supervisor;

/* Q2.3 */
SELECT name FROM records WHERE salary > 50000 ORDER BY name DESC;
