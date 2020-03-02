CREATE TABLE courses AS
SELECT "John DeNero" AS professor, "CS 61A" AS course,
       "Fa17" AS semester
UNION
SELECT "Paul Hilfinger",
       "CS 61A",
       "Fa17"
UNION
SELECT "Paul Hilfinger",
       "CS 61A",
       "Sp17"
UNION
SELECT "John DeNero",
       "Data 8",
       "Sp17"
UNION
SELECT "Josh Hug",
       "CS 61B",
       "Sp17"
UNION
SELECT "Satish Rao",
       "CS 70",
       "Sp17"
UNION
SELECT "Nicholas Weaver",
       "CS 61C",
       "Sp17"
UNION
SELECT "Gerald Friedland",
       "CS 61C",
       "Sp17"
UNION
SELECT "John DeNero",
       "CS 61A",
       "Fa16"
UNION
SELECT "Paul Hilfinger",
       "CS 61B",
       "Fa16";

CREATE TABLE num_taught as 
    SELECT "Gerald Friedland" AS professor, "CS 61C" as course, 1 as times UNION
    SELECT "John DeNero",  "CS 61A",  2 UNION
    SELECT "John DeNero", "Data 8",  1 UNION
    SELECT "Josh Hug", "CS 61B",  1 UNION
    SELECT "Nicholas Weaver", "CS 61C",  1 UNION
    SELECT "Paul Hilfinger",  "CS 61A",  2 UNION
    SELECT "Paul Hilfinger", "CS 61B",  1 UNION
    SELECT "Satish Rao", "CS 70",  1;

/* Q5.1 */
SELECT * FROM num_taught WHERE professor="Paul Hilfinger";

/* Q5.2 */
SELECT * FROM courses as c, num_taught as n
  WHERE c.professor=n.professor AND c.course=n.course AND n.times>1;

/* Q5.3 */
SELECT a.professor, b.professor, a.course, a.times 
  FROM num_taught as a, num_taught as b
  WHERE a.course=b.course AND a.professor<b.professor AND a.times=b.times;
