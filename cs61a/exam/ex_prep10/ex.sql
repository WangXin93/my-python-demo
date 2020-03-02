/* Q4 */
create table X as select 20 as X;
with ints(n) as (select 1 union select n+1 from ints, X where n<X)
  select a.n, count(a.n) from ints as a, ints as b 
  where a.n*b.n<=20 and b.n>1
  group by a.n having count(a.n)>=3;

/* Q5 */
create table reviews as
select "Albert" as user, 4 as stars, "Used to like it" as review UNION
select "Robert",         5, "BOGO! BOGO!" UNION
select "Albert",         5, "My favorite!" UNION
select "Albert",         2, "When I'm desperate" UNION
select "Albert",         5, "I love truffle fries!";

select a.stars as "stars", count(a.stars) as "numbew of reviews" from reviews as a
  where a.user="Albert"
  group by a.stars
  having stars >= 4;

/* Q7 */
CREATE TABLE anagrams AS
  WITH word(letter, position) AS (
    SELECT 'c', 1 UNION
    SELECT 'a', 10 UNION
    SELECT 't', 100 UNION
    SELECT 's', 1000
  )
  SELECT a.letter||b.letter||c.letter||d.letter
  FROM word as a, word as b, word as c, word as d
  WHERE a.position+b.position+c.position+d.position=1111;

SELECT COUNT(*) FROM anagrams;
