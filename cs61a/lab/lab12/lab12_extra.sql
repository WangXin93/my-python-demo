.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number FROM students as a, fa17students as b WHERE a.date=b.date AND a.color=b.color AND a.pet=b.pet AND a.time>b.time;

-- Q6
CREATE TABLE sevens AS
    select b.seven from checkboxes as a, students as b where a.time=b.time AND b.number=7 AND a.'7'='True';

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, COUNT(*) as count FROM fa17students GROUP BY number ORDER BY count DESC LIMIT 1;


CREATE TABLE fa17favpets AS
  SELECT pet, COUNT(*) as count FROM fa17students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE sp18favpets AS
  SELECT pet, COUNT(*) as count FROM students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE sp18dog AS
  SELECT pet, COUNT(*) as count FROM students WHERE pet='dog';


CREATE TABLE sp18alldogs AS
  SELECT pet, COUNT(*) as count FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*) as count FROM students WHERE seven='7' GROUP BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) as count FROM students GROUP BY smallest ORDER BY smallest;
