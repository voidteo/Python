--ex 1: retrieve all data from film table
select * from film;

--ex 2: Retrieve the first_name and last_name from the customer table.

select first_name , last_name from customer;

--ex 3: Retrieve all unique rating values from the film table.

select DISTINCT rating from film;

--ex 3: Retrieve all films with a rental_rate greater than 4.00.

select * from film WHERE rental_rate > 4.00;

--ex 4: Retrieve the actors whose first_name is exactly 'PENELOPE'.

SELECT actor_id , first_name from actor where first_name = 'PENELOPE';

--ex 5: Insert a new actor with first_name 'LUCY' and last_name 'VAN PELT'.

INSERT INTO actor (first_name, last_name)
values ('LUCY', 'VAN PELT');

--ex 6: Retrieve the film with the title exactly 'ACADEMY DINOSAUR'.

select * from film where title = 'ACADEMY DINOSAUR';

--ex 7: Retrieve all actors whose last_name is 'NOLTE'.

select * from actor where last_name = 'NOLTE';

--ex 8: Retrieve all films with a replacement_cost less than 10.00.

select * from film where replacement_cost < 10;

--ex 9: Insert a new language named 'FINNISH'.

INSERT INTO LANGUAGE (name) values('FINNISH');

--ex 10: Retrieve the title and release_year of all films.

select title, release_year from film;

--ex 11: Retrieve all unique language_id values from the film table.

select  DISTINCT language_id from film;

--ex 11: Retrieve customers with customer_id equal to 50.

select * from customer where customer_id = 50;

--ex 12: Retrieve all films released in the year 2006.

select * from film where release_year = 2006;

--ex 13: Retrieve all actors whose first_name is exactly 'SANDRA'.

select * from actor where first_name = 'SANDRA';

--ex 14: Insert a new category with the name 'MYSTERY'.

insert into CATEGORY (name) values('MYSTERY');

--ex 15: Retrieve all films with a rental_duration equal to 6.

select * from film where rental_duration = 6;

--ex 16: Retrieve the customer_id, first_name, and email of all customers.

select customer_id, first_name, email from customer;

--ex 17: Retrieve all unique combinations of rating and rental_duration from the film table.

select DISTINCT rating , rental_duration from film;

--ex 18: Retrieve all actors whose first_name is 'WHOOPI'.

select * from actor where first_name = 'WHOOPI';

--ex 19: Insert a new film with the title 'THE GREAT ESCAPE' and language_id 1.

insert into film (title, language_id) values('THE GREAT ESCPAE', 1);

--ex 20: Retrieve all films with a rating of 'G', 'PG', or 'PG-13'.

select *  from film WHERE rating in ('G','PG', 'PG-13');

--ex 21: Retrieve all customers whose store_id is 1.

select * from customer where store_id = 1;

--ex 22: Retrieve all actors whose last_name is 'DEGENERES'.

select * from actor where last_name = 'DEGENERES';

--ex 23: Retrieve all films with a rental_rate between 1.00 and 3.00.

select film_id, title , rental_rate from film where rental_rate between 1 and 3;

--ex 24: Insert a new actor with first_name 'CHARLIE'.

insert into actor (first_name, last_name) values('CHARLIE', 'WONKA');

--ex 25: Retrieve all films with a replacement_cost between 12.00 and 18.00.

select * from film where replacement_cost between 12 and 18;

--ex 26: Retrieve all actors ordered by their last_name.

select * from actor order by last_name;

--ex 27: Retrieve all films ordered by their title in descending order.

select * from film order by title desc;

--ex 28: Retrieve all customers ordered by their first_name.

select * from customer order by first_name;

--ex 29: Insert two new actors: ('BILL', 'MURRAY'), ('SIGOURNEY', 'WEAVER').

insert into actor (first_name, last_name) values('SIGOURNEY', 'WEAVER');

--ex 30: Retrieve all films with a rating of 'R' ordered by title.

select * from film where rating = 'R' order by title;

--ex 31: Retrieve actors whose first_name is 'SUSAN' ordered by last_name descending

select * from actor where first_name = 'SUSAN' order by last_name desc;

--ex 32: Retrieve customers living in district 'Texas'.

--ex 33: Retrieve films with a rating of 'PG' AND a rental_rate less than 3.50.

select film_id, title, rental_rate from film where rating = 'PG' AND rental_rate < 3.50;

--ex 34: Insert a new language named 'SWEDISH'.

insert into language (name) values('SWEDISH');

--ex 35: Retrieve actors whose first_name is 'ED' OR last_name is 'GUINESS'.

select *  from actor where first_name = 'ED' or last_name = 'GUINESS';

--ex 36: Retrieve customers with store_id equal to 2 OR active equal to 0.

select * from customer where store_id = 2 or active = 0;

--ex 37: Retrieve films with a rating that is NOT 'NC-17'.

select * from film where not rating = 'NC-17';

--ex 38: Retrieve actors whose first_name is NOT 'FRED'.

select * from actor where first_name != 'FRED';

--ex 39: Insert a new category named 'THRILLER'.

insert into category (name) values('THRILLER');

--ex 40: Retrieve customers who are NOT active.

select * from customer where active = 0;

--ex 41: Retrieve films with a rental_duration greater than 4 AND a replacement_cost less than 20.00.

select film_id, title, rental_duration, replacement_cost from film where replacement_cost < 20 and rental_duration > 4;

--ex 42: Retrieve actors whose last_name is 'WAHLBERG' OR first_name is 'JULIA'.

select * from actor where first_name = 'JULIA' or last_name = 'WAHLBERG';

--ex 43: Retrieve customers with store_id 1 AND (active is 1 OR first_name is 'JENNIFER').

select * from customer where store_id = 1 and (active = 1 or first_name = 'JENNIFER');

--ex 44: Insert a new film with title 'SPACE ODYSSEY' and language_id 1.

insert into film (title, language_id) values('SPACE ODYSSEY', 1);

--ex 45: Retrieve films that are NOT rated 'G' AND NOT rated 'PG-13'.

select * from film where rating not in ('G', 'PG-13');

--ex 46: Retrieve actors whose first_name is 'JENNIFER' OR (last_name is 'DAVIS' AND first_name is NOT 'WALTER').

select * from actor where first_name = 'JENNIFER' or (last_name = 'DAVIS' and first_name <> 'WALTER');

--ex 47: Retrieve films released in 2006 that have a 'PG' rating and a rental_rate less than 3.00.

select title, release_year, rating from film where release_year = 2006 and rating = 'PG' and rental_rate < 3;

--ex 48: Retrieve actors whose first_name is NOT 'CARY' AND (last_name is 'NOLTE' OR last_name is 'DEGENERES').

select * from actor where first_name <> 'CARY' AND (last_name = 'NOLTE' or last_name = 'DEGENERES');

--ex 49: Insert two new languages: ('DUTCH'), ('PORTUGUESE').

insert into language (name) values('DUTCH'), ('PORTUGUESE');

--ex 50: Retrieve the titles of all films that have the special feature exactly 'Trailers'.

select * from film where 'Trailers' = ANY(special_features);

--ex 51: Retrieve the first and last names of all actors who appeared in films with a rating equal to 'G'.

--ex 52: Retrieve the emails of all active customers.

select first_name, email, active  from customer where active = 1;

--ex 53: Retrieve the titles of all films that have a rental duration equal to 7.

select title, rental_duration from film where rental_duration = 7;

--ex 54: Insert three new categories: ('CRIME'), ('FANTASY'), ('MUSICAL').

insert into category (name) values('CRIME'), ('FANTASY'), ('MUSICAL');

--ex 55: Retrieve the first and last names of all actors whose last name is 'HARRIS'.

select first_name, last_name from actor where last_name = 'HARRIS';

--ex 56: Retrieve the titles of all films where the description is exactly 'A Epic Drama of a Feminist And a Mad Scientist who must Battle a Woman in A Jet Boat'.

select title from film where description = 'A Epic Drama of a Feminist And a Mad Scientist who must Battle a Woman in A Jet Boat';

--ex 57: Retrieve the customer IDs of all inactive customers whose email address is '[email address removed]'.

select customer_id, email from customer where active = 0 and email = '[email address removed]';

--ex 58: Retrieve the titles of all films that have the special feature 'Trailers' AND the special feature 'Commentaries'...

select title , special_features from film where 'Trailers' = any(special_features) and 'Commentaries' = any(special_features);

--ex 59: Insert a new actor with first_name 'WOODY'.

insert into actor (first_name, last_name) values('WOODY', 'SCOOBY');

--ex 60: Retrieve the first and last names of all actors whose first name is 'JOHNNY' and last name is 'CAGE'.

select * from actor where first_name = 'JOHNY' and last_name = 'CAGE';

--ex 61: Retrieve the titles of all films released in 2006 that have a 'R' rating and a replacement cost greater than 20.00.

select * from film where release_year = 2006 and rating = 'R' and replacement_cost > 20;

--ex 62: Retrieve all data from the language table.

select * from language;

--ex 63: Retrieve the names of all categories.

select name from category;

--ex 64: Retrieve all film_id and title from the film table where the rental_duration is greater than 5.

select film_id, title, rental_duration from film where rental_duration > 5;

--ex 65: Insert a new film with title 'THE INVISIBLE MAN', language_id 1, and rental_duration 5.

insert into film (title, language_id, rental_duration) values('THE INVISIBLE MAN', 1, 5);

--ex 66: Retrieve all actors whose actor_id is less than 10.

select * from actor where actor_id < 10;

--ex 67: Retrieve all customers whose address_id is greater than 300.

select * from customer where address_id > 300;

--ex 68: Retrieve all films that have a special feature of 'Behind the Scenes'.

select * from film where 'Behind the Scenes' = any(special_features);

--ex 69: Insert a new actor with first_name 'OLIVIA' and last_name 'NEWTON-JOHN'.

insert into actor (first_name, last_name) values('OLIVIA', 'NEWTON-JOHN');

--ex 70: Retrieve the title of all films that have a rating of 'PG-13' and a rental_rate less than 3.00.

select title, rating, rental_rate from film where rating = 'PG-13' and rental_rate  < 3;

--ex 71: Retrieve the first_name and last_name of all actors whose last name is 'SWAYZE'.

select first_name, last_name from actor where last_name = 'SWAYZE';

--ex 72: Retrieve all films where the replacement_cost is greater than twice the rental_rate.

select * from film where replacement_cost > rental_rate * 2;

--ex 73: Insert a new language named 'JAPANESE'.

insert into language(name) values('JAPANESE');

--ex 74: Retrieve all customers whose first_name is 'KEVIN'.

select * from customer where first_name = 'KEVIN';

--ex 75: Retrieve all films that were released in 2006 and have a rental_duration equal to 7.

select * from film where release_year = 2006 and rental_duration = 7;

--ex 76: Retrieve the first_name of all actors whose last_name is 'TEMPLE'.

select first_name , last_name from actor where last_name = 'TEMPLE';

--ex 77: Retrieve all films with a rating of 'G' and a replacement_cost less than 12.00.

select * from film where rating = 'G' and replacement_cost < 12.00;

--ex 78: Insert a new category named 'ADVENTURE'.

insert into category(name) values('ADVENTURE');

--ex 79: Retrieve all customers whose email address is '[email address removed]'.

select * from customer where email = '[email address removed]';

--ex 80: Retrieve the title and rating of all films ordered by rating in ascending order.

select title , rating from film order by rating asc;

--81 Retrieve the first_name and last_name of all actors ordered by first_name descending.

select first_name, last_name from actor order by first_name desc;

--ex 82: Retrieve all films with a rental_rate greater than (SELECT AVG(rental_rate) FROM film).

select * from film where rental_rate > (select avg(rental_rate) from film);

--ex 83: Insert a new film with title 'TIME TRAVELERS', language_id 1, and replacement_cost 25.99.

insert into film(title, LANGUAGE_id, replacement_cost) values('TIME TRAVELERS', 1, 25.99);

--ex 84; Retrieve all actors whose first_name is 'CARY' OR first_name is 'AUDREY'.

select * from actor where first_name = 'CARY' or first_name = 'AUDREY';

--ex 85: Retrieve all customers who are active AND whose last_name is 'WILLIAMS'.

select * from customer where active = 1 and last_name = 'WILLIAMS';

--ex 86: Retrieve all films that have the special feature 'Commentaries' AND a rental_rate less than 3.50.

select * from film where 'Commentaries' = any(special_features) and rental_rate < 3.50;

--ex 87: Insert a new actor with first_name 'CLINT'.

insert into actor(first_name, last_name) values('CLINT', 'BARTON');

--88: Retrieve the title of all films that have a replacement_cost greater than 15.00 AND a rating of 'R'.

select title, replacement_cost, rating from film where replacement_cost > 15.00 and rating = 'R';

--ex 89: Retrieve the customer_id and first_name of all customers whose address_id is less than 100.

select customer_id, first_name, address_id from customer where address_id < 100;

--ex 90: Retrieve all films where the special features are NULL.

select * from film where special_features is NULL;

--ex 91: Insert a new language named 'KOREAN'.

insert into language(name) values('KOREAN');

--ex 92: Retrieve all actors whose last_name is 'NOLTE'.

select * from actor where last_name = 'NOLTE';

--ex 93: Retrieve all films with a rental_duration greater than or equal to 4 AND a rental_duration less than or equal to 6 AND a rating equal to 'PG'.

select * from film where rental_duration >= 4 and rental_duration <= 6 and rating = 'PG';

--ex 94: Insert a new category named 'ANIMATION'.

insert into category (name) values('ANIMATION');

--ex 95: Retrieve all customers whose email address is '[email address removed]'.

select * from customer where email = '[email address removed]';

--ex 96: Retrieve the title of all films where the description is exactly
-- 'A Fast-Paced Documentary of a Pastry Chef And a Dentist who must лицевой бой a Dentist in A Jet Boat'.

select * from film where description = 'A Fast-Paced Documentary of a Pastry Chef And a Dentist who must лицевой бой a Dentist in A Jet Boat';

--ex 97: Insert a new actor with first_name 'GRACE' and last_name 'KELLY'.

insert into actor (first_name, last_name) values('GRACE', 'KELLY');

--EX 98: Retrieve all films released in 2006 that have a replacement_cost greater than (SELECT AVG(replacement_cost) FROM film).

select * from film where release_year = 2006 and replacement_cost > (select avg(replacement_cost) from film);