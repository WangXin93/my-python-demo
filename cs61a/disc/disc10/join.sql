/* https://inst.eecs.berkeley.edu/~cs61a/sp18/disc/disc10.pdf */
.read ex.sql

CREATE TABLE meetings AS
  SELECT "Accounting" AS division, "Monday" AS day, "9am" AS time UNION
  SELECT "Computer"              , "Wednesday"    , "4pm"         UNION
  SELECT "Administration"         , "Monday"       , "11am"        UNION
  SELECT "Administration"         , "Thursday"     , "1pm";

/* Q3.1 */
SELECT a.name AS employee, a.salary AS salary, a.supervisor AS supervisor, b.salary AS "supervisor salary" 
  FROM records AS a, records AS b
  WHERE a.supervisor=b.name AND b.salary > 2*a.salary;

/* Q3.2 */
SELECT a.name AS employee, a.salary AS salary, a.supervisor AS supervisor, b.salary AS "supervisor salary" 
  FROM records AS a, records AS b
  WHERE a.supervisor=b.name AND a.division != b.division;

/* Q3.3 */
SELECT b.day, b.time 
  FROM records AS a, meetings AS b
  WHERE a.division=b.division AND a.supervisor="Oliver Warbucks";

/* Q3.4-3.5 */
SELECT a.name, b.name, c.name
  FROM records AS a, records AS b, records as c
  WHERE a.supervisor=b.name AND b.supervisor=c.name;

SELECT b.name
  FROM records AS a, records AS b, records as c
  WHERE a.supervisor=b.name AND b.supervisor=c.name
  GROUP BY b.name;

/* Q3.6 */
SELECT a.name, b.time, c.name, d.time
  FROM records as a, meetings as b, records as c, meetings as d
  WHERE a.division=b.division AND a.supervisor=c.name AND c.division=d.division AND b.time=d.time;
