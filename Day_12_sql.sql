select * from movies where id = 6

select * from movies where year between 2000 and 2010

select * from movies where year not between 2000 and 

Select * from movies limit 5; || select * from movies id <= 6

-- Find all the Toy Story movies
SELECT * FROM movies
where title like '%toy story%'

-- Find all the movies directed by John Lasseter
SELECT * FROM movies
where director like "john lasseter"

-- Find all the movies (and director) not directed by John Lassete
SELECT * FROM movies
where director not like "john lasseter"

-- Find all the WALL-* movies
SELECT * FROM movies
where title  like "Wall%"

-- List all directors of Pixar movies (alphabetically), without duplicates
SELECT DISTINCT director
from movies 
order by director asc
-- List the last four Pixar movies released (ordered from most recent to least
SELECT * from movies
order by year desc
limit 4;

--List the first five Pixar movies sorted alphabetically
SELECT * from movies
order by title 
limit 5;

--List the next five Pixar movies sorted alphabetically ✓
SELECT * from movies
order by title 
limit 5 offset 5;

-- List all the Canadian cities and their populations
SELECT * FROM north_american_cities
where country = "Canada"

-- Order all the cities in the United States by their latitude from north to south
SELECT * FROM north_american_cities
where country like "united States"
order by latitude desc

-- List all the cities west of Chicago, ordered from west to east
SELECT * FROM north_american_cities
where longitude < -87.629798
order by longitude  
-- to avoid hrd coding
SELECT * FROM north_american_cities
    where longitude < (SELECT Longitude FROM north_american_cities
    where City = "Chicago")
    order by longitude

-- List the two largest cities in Mexico (by population)
SELECT * FROM north_american_cities
where country like "mexico"
order by Population desc
limit 2;

-- List the third and fourth largest cities (by population) in the United States and their population
SELECT * FROM north_american_cities
where country like "united states"
order by Population desc
limit 2 offset 2;

--Find the domestic and international sales for each movie
SELECT * FROM Movies
inner join boxoffice
on movies.id = boxOffice.movie_id
--OR
SELECT * FROM Movies
inner join boxoffice
on id = movie_id

-- Show the sales numbers for each movie that did better internationally rather than domestically
SELECT * FROM Movies
inner join boxoffice
on movies.id = boxOffice.movie_id
where domestic_sales < international_sales

-- List all the movies by their ratings in descending order
SELECT * FROM Movies
inner join boxoffice
on movies.id = boxOffice.movie_id
order by rating desc

-- Find the list of all buildings that have employees
SELECT distinct Building
FROM employees;

-- Find the list of all buildings and their capacity
SELECT *
FROM Buildings;

-- List all buildings and the distinct employee roles in each building (including empty buildings)
SELECT  distinct Building_name,  role
FROM Buildings
left join employee
on Buildings.Building_name = emloyees.Building ;