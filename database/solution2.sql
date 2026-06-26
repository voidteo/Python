--ex 1: Count the total number of films in the film table.

select count(film_id) from film;

--ex 2: What is the total number of customers?

select count(customer_id) from customer;

--ex 3: Find the average rental_rate of all films.

select round(avg(rental_rate),2) from film;

--ex 4: What is the maximum replacement_cost in the database?

select max(replacement_cost) from film;

--ex 5: Find the minimum length of a film.

select min(length) from film;

--ex 6: Calculate the total amount paid in the payment table.

select sum(amount) from payment;

--ex 7: Count the number of addresses in the address table.

select count(address_id) from address;

--ex 8: What is the average length of all films?

select round(avg(length), 2) from film;

--ex 9: Find the total number of distinct first_name values in the actor table.

select count(DISTINCT first_name) from actor;

--ex 10: Find the maximum rental_duration from the film table.

select max(rental_duration) from film;

--ex 11: Count how many rentals have been made in total.

select count(*) from rental;

--ex 12: Find the total number of cities in the city table.

select count(city_id) from city;

--ex 13: What is the average amount of a payment?

select round(avg(amount), 2) from payment;

--ex 14: Count the number of films that have a rating of 'G'.

select count(rating) from film where rating = 'G';

--ex 15: Find the total amount collected by staff member 1.

select sum(amount) from payment where staff_id = 1;

--ex 16: Find the maximum amount ever paid for a rental.

select max(amount) from payment;

--ex 17: Count how many films have the word 'Drama' in their description.

select count(film_id) from film where description like '%Drama%';

--ex 18: What is the average replacement_cost for all films?

select round(avg(replacement_cost), 2) from film;

--ex 19: Count the number of active customers (active = 1).

select count(*) from customer where active = 1;

--ex 20: Find the total sum of length for all films (total minutes of all movies).

select sum(length) from film;

--ex 21: Select films with a length between 60 and 90 minutes.

select * from film where length between 60 and 90;

--ex 22: Select payments made between '2007-02-15' and '2007-02-20'.

select * from payment where payment_date between '2007-02-15' and '2007-02-20';

--ex 23: Find all films with a rental_rate of 0.99, 2.99, or 4.99 (Use IN).

select * from film where rental_rate in (0.99, 2.99, 4.99);

--ex 24: Find actors whose actor_id is between 10 and 20.

select * from actor where actor_id between 10 and 20;

--ex 25: Retrieve films where the rating is 'G', 'PG', or 'R'.

select title , rating from film where rating in ('G', 'PG', 'R');

--ex 26: Find payments where the amount is between 2.99 and 5.99.

select * from payment where amount between 2.99 and 5.99;

--ex 27: Find rentals made by customers with IDs 1, 5, 10, and 15.

select * from rental where customer_id in (1,5,10, 15);

--ex 28: Find films released in 2006 (using BETWEEN logic even if it's one year).

select title, release_year from film where release_year between 2006 and 2006

--ex 29: Find films where the replacement_cost is NOT between 10 and 20.

select title, replacement_cost from film where not replacement_cost between 10 and 20;

--ex 30: Retrieve addresses in districts: 'California', 'Texas', or 'Taipei'.

select * from address where district in ('California', 'Texas', 'Taipei');

--ex 31: Find films with rental_duration between 3 and 5 days.

select title, rental_duration from film where rental_duration between 3 and 5;

--ex 32: Find customers with customer_id between 300 and 350.

select * from customer where customer_id between 300 and 350;

--ex 33: Find films whose language_id is 1, 3, or 5.

select title, language_id from film where language_id in (1, 3, 5);

--ex 34: Find all staff members with staff_id IN (1, 2).

select * from staff where staff_id in(1,2);

--ex 35: Select films where length is between 120 and 180 minutes.

select title, length from film where length between 120 and 180;

--ex 36: Find categories with category_id between 5 and 10.

select * from category where category_id between 5 and 10;

--ex 37: Find rentals where return_date is between '2005-05-25' and '2005-05-26'.

select * from rental where return_date between '2005-05-25' and '2005-05-26';

--ex 38: Find films where the rating is NOT 'NC-17' or 'R'.

select * from film where not rating in ('NC-17', 'R');

--ex 39: Find payments with an amount greater than 10.00 using BETWEEN logic (e.g., 10 and 100).

select * from payment where amount between 10 and 100;

--ex 40: Select cities in countries with IDs 44, 50, and 60.

select * from city where country_id in (44, 50, 60);

--ex 41: Group films by rating and count how many films are in each rating.

select rating, count(*) from film group by rating;

--ex 42: Group payments by customer_id and find the total amount spent by each.

select customer_id, sum(amount) from payment group by customer_id;

--ex 43: Group films by rental_duration and find the average length for each group.

select rental_duration, avg(length) from film group by rental_duration;

--ex 44: Count the number of actors for each first_name.

select first_name, count(*) from actor group by first_name;

--ex 45: Group rentals by staff_id to see who processed how many rentals.

select staff_id, count(*) from rental group by staff_id;

--ex 46: Find the maximum rental_rate for each rating.

select rental_rate, max(rental_rate) from film group by rental_rate;

--ex 47: Group films by language_id and find the average replacement_cost.

select language_id , avg(replacement_cost) from film group by language_id;

--ex 48: Group payments by staff_id and find the total amount collected by each.

select staff_id, sum(amount) from payment group by staff_id;

--ex 49: Find the minimum length of film for each rating.

select rating, min(length) from film group by rating;

--ex 50: Group customers by store_id and count them.

select store_id, count(*) from customer group by store_id;

--ex 51: Group addresses by district and count how many addresses are in each.

select district, count(address) from address group by district;

--ex 52: Find the average amount of payment for each customer_id.

select customer_id, round(avg(amount), 2) from payment group by customer_id;

--ex 53: Group films by release_year and count them.

select release_year, count(*) from film group by release_year;

--ex 54: Group rentals by customer_id and count how many rentals each customer made.

select customer_id, count(rental_id) from rental group by customer_id;

--ex 55: Find the sum of length of films for each language_id.

select language_id, sum(length) from film group by LANGUAGE_id;

--ex 56: Group payments by the date (using CAST(payment_date AS DATE)) and find total daily revenue.

select payment_date, sum(amount) from payment group by payment_date;

--ex 57: Group films by special_features and count them.

select special_features, count(*) from film group by special_features;

--ex 58: Group actors by last_name and count how many actors share the same last name.

select last_name, count(last_name) from actor group by last_name;

--ex 59: Group stores by manager_staff_id and count them.

select manager_staff_id, count(*) from store group by manager_staff_id;

--ex 60: Group cities by country_id and find how many cities are in each country.

select country_id, count(city) from city group by country_id;

--ex 61: List ratings that have more than 200 films.

select rating from film group by rating having count(*) > 200;

--ex 62: Find customers who have spent more than $150 in total.

select customer_id from payment group by customer_id having sum(amount) > 150;

63: Show rental_duration groups where the average film length is greater than 115.

select rental_duration from film group by rental_duration having avg(length) > 115;

64: Find districts in the address table that have more than 5 addresses.

select district from address group by district having count(address) > 5;

--ex 65: List customer_ids that have made more than 40 rentals.

select customer_id from rental group by customer_id having count(*) > 40;

--ex 66: Find ratings where the average rental_rate is above 3.00.

select rating from film group by rating having avg(rental_rate) > 3.00;

--ex 67: Show staff_ids that have processed more than 8000 payments.

select staff_id from payment group by staff_id having count(payment_id) > 8000;

--ex 68: Find countries that have more than 10 cities in the city table.

select country_id from city group by country_id having count(*) > 10;

--ex 69: List replacement_cost values that are shared by more than 50 films.

select replacement_cost from film group by replacement_cost having count(*) > 50;

--ex 70: Find customers whose average payment amount is greater than 5.00

select customer_id from payment group by customer_id having avg(amount) > 5.00;

--ex 71: Show language_ids that have more than 500 films.

select language_id from film group by language_id HAVING count(*) > 500;

--ex 72: Find rental_ids in payment that have multiple entries (if any).

select rental_id from payment group by rental_id HAVING count(*) > 1;

--ex 73: List store_ids that have more than 300 customers.

select store_id from customer group by store_id HAVING count(*) > 300;

--ex 74: Find actors whose first_name appears more than 3 times in the actor table.

select first_name from actor group by first_name HAVING count(*) > 3;

--ex 75: Show ratings where the minimum length of a film is greater than 45.

select rating from film group by rating HAVING min(length) > 45;

--ex 76: Find the amount values in payment that have been paid more than 1000 times.

select amount from payment group by amount HAVING count(*) > 1000;

--ex 77: List staff_ids whose average payment processed is less than 4.50.

select staff_id from payment group by staff_id HAVING avg(amount) < 4.50;

--ex 78: Find customer_ids that have spent between $100 and $150 (Use HAVING and BETWEEN).

select customer_id from payment group by customer_id HAVING sum(amount) BETWEEN 100 and 150;

--ex 79: List rental_duration groups where the max replacement_cost is exactly 29.99.

select rental_duration from film group by rental_duration HAVING max(replacement_cost) = 29.99;

--ex 80: Find films with rating 'G' that have an average length over 100 (Hint: WHERE + GROUP BY + HAVING).

select rating from film group by rating HAVING avg(length) > 100;

--ex 81: Select films with a rental_rate higher than the overall average rental_rate.

select * from film where rental_rate > (select avg(rental_rate) from film);

--ex 82: Find all films with the same length as the film 'Academy Dinosaur'.

select * from film where length = (select length from film where title = 'Academy Dinosaur');

--ex 83: Select customers who have paid more than the average total payment of all customers.

select customer_id , sum(amount) from payment group by customer_id HAVING sum(amount) > 
(select avg(total) from (select customer_id, sum(amount) as total from payment group by customer_id) as customer_totals);

--ex 84: Find films that have a replacement_cost equal to the maximum replacement_cost.

select * from film where replacement_cost = (select max(replacement_cost) from film);

--ex 85: Select actors who have appeared in more films than actor ID 1 (Subquery in HAVING).

select actor_id from film_actor group by actor_id HAVING count(film_id) > 
(select count(film_id) from film_actor where actor_id = 1);

--ex 86: Find films whose rental_rate is lower than the average rental_rate of 'PG' films.

select title from film where rental_rate < (select avg(rental_rate) from film where rating = 'PG')

--ex 87: Select all payments where the amount is greater than the average amount of payments made to staff 2.

select * from payment where amount > (select avg(amount) from payment where staff_id = 2);

--ex 88: Find the titles of films that are in the same category as 'Film_id 1'.

select title from film where film_id in (select film_id from film_category where category_id = (select category_id from film_category where film_id = 1));

--ex 89: Find customers who live in the same city as customer ID 5.

select customer_id from customer where address_id in
(select address_id from address where city_id = (select city_id from address where address_id = (select address_id from customer where customer_id = 5)));

--ex 90: Select films that were rented more than the average number of rentals per film.

select avg(rental_count) from (
    select film_id , count(*) as rental_count from inventory
    where inventory_id in (
        select inventory_id from rental
    ) group by film_id
) as film_rentals;

--ex 91: Find the total amount spent by the customer who has the highest customer_id.

select sum(amount) from payment where customer_id = (select max(customer_id) from customer);

--ex 92: List ratings and their film counts, but only for ratings that have films longer than the average film length.

select rating, count(*) from film group by rating HAVING max(length) > (select avg(length) from film);

--ex 93: Find the average length of films for each rating, but only for films that cost more than $2.99.

select rating, avg(length) from film where rental_rate > 2.99 group by rating ;

--ex 94: Select films that have the same rating and rental_duration as 'Adaptation Holes'.

select film_id, title from film where (rating, rental_duration) = (select rating, rental_duration from film where title = 'ANGELS LIFE');

--ex 95: Find the customer who made the very first payment (Minimum payment_date).

select customer_id from payment where payment_date = (select min(payment_date) from payment);

--ex 96: Count how many films have a length between the average length and the maximum length.

select count(*) from film where length BETWEEN (select avg(length) from film) and (select max(length) from film);

--ex 97: Find the total number of rentals for films that have a replacement_cost between 15 and 20.

select count(*) from rental where inventory_id in (select inventory_id from inventory where film_id 
in (select film_id from film where replacement_cost between 15 and 20));

--98: Show the customer_id and their total spent, only if they spent more than the average spending of all customers.

select customer_id, sum(amount)
from payment
group by customer_id
having sum(amount) > (
    select avg(total)
    from (
        select customer_id, sum(amount) as total
        from payment
        group by customer_id
    ) t
);

--ex 99: List all films that have a length greater than the average length of 'R' rated movies.

select * from film where length > (
    select avg(length) from film where rating = 'R'
);

--ex 100: Find the staff member who processed the most payments (use LIMIT 1 with GROUP BY).

select staff_id, count(*) from payment group by staff_id order by count(*) desc limit 1;