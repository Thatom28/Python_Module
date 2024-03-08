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

--Lesson 8
--Find the name and role of all employees who have not been assigned to a building
SELECT name, role
from employees
where building is  null

--Find the names of the buildings that hold no employees
SELECT distinct building_name
FROM buildings 
 left employees
on building_name = building
where role is null;

-- List all movies and their combined sales in millions of dollars 
SELECT title, (domestic_sales + International_sales)/100000 as sum FROM movies
left join BoxOffice
on id = movie_id;
-- List all movies and their ratings in percent
SELECT title, rating * 10 as percentage FROM movies
left join BoxOffice
on id = movie_id;
-- List all movies that were released on even number years 
SELECT * FROM movies
where year%2 = 0;

-- Find the longest time that an employee has been at the studio
SELECT name, max(Years_employed) as longest_in_studio 
FROM employees;

-- For each role, find the average number of years employed by employees in that role
SELECT role, avg(Years_employed) 
FROM employees
group by role;

-- Find the total number of employee years worked in each building
SELECT building, sum(Years_employed) as population FROM employees
group by building;

-- Find the number of Artists in the studio (without a HAVING clause)
SELECT role, count(role) as number_of_artists FROM employees
where role="Artist";

-- Find the number of Employees of each role in the studio
SELECT role, count(role) as number_of_artists
FROM employees
group by role;

-- filtering using having
SELECT role, count(role) as number_of_artists
FROM employees
group by role
having number_of_artists > 4;

-- Find the total number of years employed by all Engineers 
SELECT role, sum(years_employed) as sum_of_years_employed
FROM employees
where role = "Engineer"

-- Find the number of movies each director has directed
SELECT director, count(title) FROM movies
group by director;

-- Find the total domestic and international sales that can be attributed to each director
SELECT director, sum(Domestic_sales + international_sales) as total_sales FROM movies
join Boxoffice
on id = movie_id
group by director;

---------------SQL SYNTAX--------------------------------
-- SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
-- FROM mytable
--     JOIN another_table
--       ON mytable.column = another_table.column
--     WHERE constraint_expression
--     GROUP BY column
--     HAVING constraint_expression
--     ORDER BY column ASC/DESC
--     LIMIT count OFFSET COUNT;

-- Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)
insert into movies
values (4, "Toy Story 4", "John Lasseter", 2024, 90);

-- Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.
insert into Boxoffice
values(4, 8.7, 3400000,2700000)

-- The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
update Movies
set director = "John Lasseter"
where title = "A Bug's Life"

-- The year that Toy Story 2 was released is incorrect, it was actually released in 1999
update Movies
set year = 1999
where title = "Toy Story 2"

-- Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich
update Movies
set title = "Toy Story 3",
    director = "Lee Unkrich"
where title = "Toy Story 8";

-- This database is getting too big, lets remove all movies that were released before 2005.
SELECT * FROM movies
where year<2005;

delete from movies
where year < 2005;
-- Andrew Stanton has also left the studio, so please remove all movies directed by him.
select * from movies
where director ="Andrew Stanton"

delete from movies 
where director ="Andrew Stanton"

-- Create a new table named Database with the following columns:
-- – Name A string (text) describing the name of the database
-- – Version A number (floating point) of the latest version of this database
-- – Download_count An integer count of the number of times this database was downloaded
-- This table has no constraints. 
Create table database(
name text,
Version Integer,
Download_count Integer
)

-- Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in
Alter table movies
Add Aspect_ratio FLOAT

-- Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.
Alter table movies
Add Language TEXT
  default "English"

-- We've sadly reached the end of our lessons, lets clean up by removing the Movies table
drop table movies
drop table if exists movies