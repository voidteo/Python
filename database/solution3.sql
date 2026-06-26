--ex 1: Select all films where rating IN ('PG', 'PG-13').

select * from film where rating in ('PG', 'PG-13');

--ex 2: Select all films where rental_rate IN (0.99, 2.99, 4.99).

select * from film where rental_rate in(0.99, 2.99, 4.99);

--ex 3: Select films whose length BETWEEN 90 AND 120 minutes.

select * from film where length between 90 and 120;

--ex 4: Select films with replacement_cost BETWEEN 15 AND 20.

select * from film where replacement_cost between 15 and 20;

--ex 5: Select films whose title LIKE 'A%'.

select * from film where title like 'A%';

--ex 6: Select films whose title LIKE '%Love%'.

select * from film where title like '%Love%';

--ex 7: Select films whose title LIKE '%Man%'.

select * from film where title like '%Man%';

--ex 8: Select films whose title LIKE '_A%'.

select * from film where title like '_A%';

--ex 9: Select films whose description ILIKE '%adventure%'.

select * from film where description ilike '%adventure%';

--ex 10: Select films whose description ILIKE '%police%' AND rating = 'R'.

select * from film where description ilike '%police%' and rating = 'R';

--ex 11: Select customers whose first_name LIKE 'A%'.

select * from customer where first_name like 'A%';

--ex 12: Select customers whose last_name LIKE '%son'.

select * from customer where last_name like '%son';

--ex 13: Select customers whose first_name ILIKE 'm%'.

select * from customer where first_name ilike 'm%';

--ex 14: Select customers whose email LIKE '%@sakilacustomer.org'.

select * from customer where email like '%@sakilacustomer.org';

--ex 15: Select customers whose create_date BETWEEN '2006-01-01' AND '2006-06-30'.

select * from customer where create_date between '2006-01-01' and '2006-06-30';

--ex 16: Select customers whose store_id IN (1, 2).

select * from customer where store_id in (1,2);

--ex 17: Select customers whose last_name ILIKE '%LL%'.

select * from customer where last_name ilike '%ll%';

--ex 18: Select customers whose first_name LIKE 'J%' AND active = 1.

select * from customer where first_name like '%J' and active = 1;

--ex 19: Select customers whose email ILIKE '%example%'.

select * from customer where email ilike '%example%';

--ex 20: Select customers whose first_name IN ('MARY', 'PATRICIA', 'LINDA').

select * from customer where first_name in('MARY', 'PATRICIA', 'LINDA');

--ex 21: Select payments whose amount BETWEEN 5 AND 8.

select * from payment where amount between 5 and 8;

--ex 22: Select payments whose payment_date BETWEEN '2005-07-01' AND '2005-07-15'.

select * from payment where payment_date between '2005-07-01' and '2005-07-15';

--ex 23: Select payments whose amount IN (0.99, 2.99, 4.99).

select * from payment where amount in(0.99, 2.99, 4.99);

--ex 24: Select payments where amount NOT IN (0.99, 2.99).

select * from payment where amount in(0.99, 2.99);

--ex 25: Select payments whose payment_date::text LIKE '2005-07%'.

select * from payment where payment_date::text like '2005-07%';

--ex 26: Select payments whose amount BETWEEN 8 AND 10 AND staff_id = 1.

select * from payment where amount between 8 and 10 and staff_id =1;

--ex 27: Select payments whose payment_date BETWEEN '2005-06-01' AND '2005-06-30' AND amount > 5.

select * from payment where payment_date between '2005-06-01' and '2005-06-30' and amount > 5;

--ex 28: Select payments where customer_id IN (1, 2, 3, 4, 5).

select * from payment where customer_id in(1,2,3,4,5);

--ex 29: Select payments whose amount BETWEEN 1 AND 3 OR amount BETWEEN 8 AND 10.

select * from payment where amount BETWEEN 1 and 3 or amount between 8 and 10;

--ex 30: Select payments whose payment_date::text ILIKE '%2005-07-3%'.

select * from payment where payment_date::text ilike '%2005-07-3%';

--ex 26: Retrieve all films with rental_rate > 2.99 and length < 90.

select * from film where rental_rate > 2.99 and length < 90;

--ex 27: Find all customers whose first name starts with 'M' or 'A'.

select * from customer where first_name like 'M%' or first_name like 'A%';

--ex 28: List all films that are not rated 'R'.

select title , rating from film where not rating = 'R';

--ex 30: Retrieve the top 10 most recently added films using ORDER BY film_id DESC LIMIT 10.

select * from film order by film_id desc limit 10;

--ex 31: List 5 actors whose first names end with 'a' using LIMIT.

select * from actor where first_name like '%a' order by first_name  limit 5;

--ex 32: Find all staff whose email contains '@sakilacustomer.org'.

select * from staff where email like '%@sakilacustomer.org%';

--ex 33: Display all payments greater than 5.00 but less than 10.00.

select * from payment where amount between 5 and 10;

--ex 34: List the 10 shortest films that have 'ACTION' in their title.

select title, length from film where title like '%ACTION%' order by length asc limit 10;

--ex 35: Find all inactive customers (active = false).

select * from customer where active = 0;

--ex 36: Retrieve all rentals where the return date is still NULL.

select * from rental where return_date is NULL;

--ex 37: Display 10 addresses from countries not equal to 'United States'.

select * from country where country <> 'United States' order by country limit 10;

-- task related to group by 

--ex 1: Count total number of payments.

select count(*) from payment;

--ex 2: Find total amount paid (sum of all amounts).

select sum(amount) as total_payment from payment;

--ex 3: Calculate average payment amount.

select avg(amount) as average_payment from payment;

--ex 4: Find the smallest and largest payment amounts.

select min(amount) as smallest, max(amount) as largest from payment;

--ex 5: Count how many payments each customer made.

select customer_id, count(*) from payment group by customer_id;

--ex 6: Total amount paid by each customer.

select customer_id, sum(amount) from payment group by customer_id;

--ex 7: Average payment amount per customer.

select customer_id, round(avg(amount), 2) from payment group by customer_id;

--ex 8: Customers who made more than 10 payments.

select customer_id from payment group by customer_id HAVING count(*) > 10;

-- ex 9: Customers whose total payments exceed 150.

select customer_id from payment group by customer_id having sum(amount) > 150;

--ex 10: Customers whose average payment exceeds 5.

select customer_id from payment group by customer_id HAVING avg(amount) > 5;

--ex 11: Count of payments per staff member.

select staff_id, count(*) from payment group by staff_id ;

--ex 12: Total amount collected by each staff.

select staff_id, sum(amount) from payment group by staff_id;

--ex 13: Staff who collected more than 1000 in total.

select staff_id from payment group by staff_id HAVING sum(amount) > 1000;

--ex 14: Average payment per staff.

select staff_id,avg(amount) from payment group by staff_id;

--ex 15: Number of payments made on each date.

select payment_date, count(*) from payment group by payment_date;

--ex 16: Count total rentals.

select count(*) from rental;

--ex 17: Find the earliest and latest rental dates.

select min(rental_date), max(rental_date) from rental;

--ex 18: Count how many rentals each customer made.

select customer_id, count(*) from rental group by customer_id;

--ex 19: Customers with more than 20 rentals.

select customer_id from rental group by customer_id HAVING count(*) > 20;

--ex 20: Average number of rentals per day (using GROUP BY rental_date::date).

select rental_date, avg(rental_id) from rental group by rental_date::text ;

--ex 21: Count how many times each staff processed a rental.

select staff_id, count(*) from rental group by staff_id ;

--ex 22: Staff with more than 100 rentals handled.

select staff_id from rental group by staff_id HAVING count(*) > 100;

--ex 23: Count of rentals per return_date (group by return_date).

select date(return_date), count(*) from rental group by date(return_date);

--ex 24: Days where more than 50 rentals occurred.


select date(rental_date) from rental group by date(rental_date) HAVING count(*) > 50;

--ex 25: Average rental_id per staff (nonsensical mathematically, but forces use of aggregate).

select staff_id, round(avg(rental_id), 2) from rental group by staff_id;

--ex 26: Count total customers.

select count(*) from customer;

--ex 27: Count customers by active status.

select active, count(*) from customer group by active;

--ex 28:  Count customers by store_id.

select store_id, count(*) from customer group by store_id;

--ex 29:  Stores having more than 300 customers.

select store_id from customer group by store_id HAVING count(*) > 300;

--ex 30: Average customer ID per store (training grouping only).

select store_id, avg(customer_id) from customer group by store_id ;

--ex 31: Count customers by create_date (group by date).

select date(create_date), count(*) from customer group by date(create_date);

--ex 32: Count how many customers were added per day.

select date(create_date), count(*) from customer group by date(create_date);

--ex 33: Days where more than 5 customers were added.

select date(create_date) from customer group by date(create_date) HAVING count(*) > 5;

--ex 34: Count how many films exist per rating.

select rating, count(*) from film group by rating;

--ex 35: Ratings that have more than 200 films.

select rating from film group by rating HAVING count(*) > 200;

--ex 36: Average rental rate per rating.

select rating, avg(rental_rate) from film group by rating;

--ex 37: Average length per rating.

select rating, round(avg(length), 2) from film group by rating;

--ex 38: Ratings with average rental rate above 3.0.

select rating from film group by rating HAVING avg(rental_rate) > 3.0;

--ex 39: Count how many films have the same replacement cost.

select replacement_cost, count(*) from film group by replacement_cost;

--ex 40: Replacement cost values that appear in more than 10 films.

select replacement_cost from film group by replacement_cost HAVING count(*) > 10;

