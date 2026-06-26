
--ex 1: List all film titles and their language names.
--(Join film and language)

select f.title , l.name from film as f
inner join language as l
on f.language_id = l.language_id;

--ex 2: Show the first and last names of all actors who acted in the film "ACADEMY DINOSAUR".
--(Join actor, film_actor, film)

select a.first_name, a.last_name from film as f 
inner join film_actor as fa 
on f.film_id = fa.film_id 
join actor as a 
on fa.actor_id = a.actor_id where f.title = 'ACADEMY DINOSAUR';

--ex 3: Display all customer names and their email addresses.
--(Join customer with no other table — warm-up)

select first_name, email from customer;

--ex 4: List customer full names and the names of the stores they registered at.
--(Join customer and store)

select c.first_name, c.last_name , s.store_id from customer as c 
inner join store as s 
on s.store_id = c.store_id;

--ex 5: Show all films and their categories.
--(Join film, film_category, category)

select f.title, c.name from film  as f
inner join film_category as fc 
on f.film_id = fc.film_id 
inner join category as c 
on c.category_id = fc.category_id;

--ex 6: List staff members and their respective store address.
--(Join staff, address)

select s.first_name, a.address_id from staff as s
inner join address as a 
on s.address_id = a.address_id;

--ex 7: Get the titles of all films rented by customer “MARY SMITH”.
--(Join customer, rental, inventory, film)

select c.first_name, c.last_name, f.title from customer as c 
inner join rental as r on c.customer_id = r.customer_id 
inner join inventory as i on i.inventory_id = r.inventory_id 
inner join film as f on f.film_id = i.film_id 
where c.first_name = 'MARY' and c.last_name = 'SMITH';

--ex 8: List the names of all customers who rented at least one film.
--(Join customer and rental with DISTINCT)

select DISTINCT c.first_name, c.last_name from customer as c 
inner join rental as r 
on c.customer_id = r.customer_id ;

--ex 9: Show all films that are in the 'Comedy' category.
--(Join film_category, category, film with filter on category name)

select f.title, c.name as category from film as f 
inner join film_category as fc 
on f.film_id = fc.film_id  
inner join category as c 
on c.category_id = fc.category_id 
where c.name = 'Comedy' 

--ex 10: List all payments along with the customer names who made them.
--(Join payment and customer)

select p.payment_id, p.amount, c.first_name, c.last_name from customer as c 
inner join payment as p 
on c.customer_id = p.customer_id;

--ex 11:Get the titles and rental rates of all films longer than 120 minutes.
--(Join film only — no join needed — easy confidence builder)

select title, rental_rate from film
where length > 120;

--ex 12: List the staff who processed each rental transaction.
--(Join rental and staff)


select s.first_name, s.last_name, r.rental_id from staff as s 
inner join rental as r 
on s.staff_id = r.staff_id;

--ex 13: Display all customers and the cities they live in.
--(Join customer, address, city)

select c.first_name, c.last_name, ci.city, a.address from city as ci 
inner join address as a 
on ci.city_id = a.city_id 
inner join customer as c 
ON c.address_id = a.address_id;

--ex 14: List all customers and the films they have rented, with the film title and rental date.
--(Join customer, rental, inventory, film)

select c.first_name, c.last_name, f.title, r.rental_date from customer as c
inner join rental as r 
on c.customer_id = r.rental_id 
inner join inventory as i 
on r.inventory_id = i.inventory_id
inner join film as f 
on i.film_id = f.film_id;

--ex 15: Show film titles, actor names, and categories.
--(Join film, film_actor, actor, film_category, category)

select f.title, a.first_name, a.last_name, c.name as category from actor as a
inner join film_actor as fa 
on a.actor_id = fa.actor_id 
inner join film as f 
on f.film_id = fa.film_id 
inner join film_category as fc 
on f.film_id = fc.film_id 
inner join category as c 
on c.category_id = fc.category_id ;

--ex 16: Find all rentals and include customer name, staff name, film title, and rental date.
--(Join rental, customer, staff, inventory, film)

select r.rental_id, c.first_name as customer_name, s.first_name as staff_name, f.title, r.rental_date from film as f
inner join inventory as i 
on f.film_id = i.film_id
inner join rental as r 
on i.inventory_id = r.inventory_id 
inner join customer as c 
on r.customer_id = c.customer_id 
inner join payment as p 
on p.customer_id = c.customer_id 
inner join staff as s 
on s.staff_id = p.staff_id;

--ex 17: Display a list of customers, their email, and the store city they are associated with.
--(Join customer, store, address, city)

select c.first_name, c.last_name, c.email, s.store_id, a.address, ci.city from customer as c 
inner join store as s 
on c.store_id = s.store_id 
inner join address as a 
on a.address_id = s.address_id 
inner join city as ci 
on ci.city_id = a.city_id;

--ex 18: List the top 10 most rented films with the number of times each was rented.
--(Join rental, inventory, film + GROUP BY + COUNT)

select f.title, count(*) as rental_count from rental as r 
inner join inventory as i 
on i.inventory_id = r.inventory_id 
inner join film as f 
on f.film_id = i.film_id 
group by f.title ORDER BY rental_count desc limit 10;

--ex 19: List all films with their language names.

select f.title, l.name from film f
inner join language as l 
on f.language_id = l.language_id;

--ex 20: Show all actors with their film titles.

select a.first_name, a.last_name , f.title from actor as a 
inner join film_actor as fa 
on fa.actor_id = a.actor_id 
inner join film as f 
on f.film_id = fa.film_id;

--ex 21: Display customer names with their corresponding rental dates.

select c.first_name, c.last_name, r.rental_date from customer as c 
inner join rental as r 
on r.customer_id = r.customer_id;

--ex 22: Find all staff members and the addresses where they work.

select s.first_name, s.last_name,  a.address from staff as s 
inner join address as a 
on a.address_id = s.address_id;

--ex 23: List all payments with customer names who made them.

select c.first_name, c.last_name, p.payment_id from customer as c 
inner join payment as p 
on p.customer_id = c.customer_id;

--ex 24: Show film titles and their categories.

select f.title, c.name from film as f 
inner join film_category as fc 
on fc.film_id = f.film_id 
inner join category as c 
on c.category_id = fc.category_id;

--ex 25: Display actor names with the number of films they've appeared in.

select a.first_name, a.last_name, count(*) from actor as a 
inner join film_actor as fa 
on a.actor_id = fa.actor_id 
inner join film as f 
on f.film_id = fa.film_id 
group by a.actor_id ;

--ex 26: Find customers who rented films from a specific store (store_id = 1).

select c.first_name, c.last_name, s.store_id from customer as c 
inner join store as s 
on s.store_id = c.store_id 
where s.store_id = 1;

--ex 27: List all films rented in May 2005 with customer names.

select f.title, r.rental_date, c.first_name, c.last_name from customer as c 
inner join rental as r on c.customer_id = r.customer_id 
inner join inventory as i on i.inventory_id = r.inventory_id 
inner join film as f on f.film_id = i.film_id
where r.rental_date::text like '2005-05%';

--ex 28: Show staff members who processed payments over $5.00.

select DISTINCT s.first_name, s.last_name, p.amount from payment as p 
inner join staff as s on s.staff_id = p.staff_id 
where p.amount > 5;

--ex 29: Find films rented more than 10 times with their rental counts.

select f.title, count(*) as rental_count from rental as r 
inner join inventory as i 
on i.inventory_id = r.inventory_id 
inner join film as f 
on f.film_id = i.film_id 
group by f.title HAVING count(*) > 10;

--30: Display customers who rented films from multiple categories.

select c.first_name, c.last_name from customer as c 
inner join rental as r on r.customer_id = c.customer_id 
inner join inventory as i on r.inventory_id = i.inventory_id 
inner join film as f on f.film_id = i.film_id 
inner join film_category as fc on f.film_id = fc.film_id 
inner join category as ca on ca.category_id = fc.category_id 
group by c.customer_id  HAVING count(DISTINCT ca.category_id) > 1;

--ex 31: List actors who appeared in films from at least 3 different categories.

select a.first_name, a.last_name  from actor as a 
inner join film_actor as fa on fa.actor_id = a.actor_id 
inner join film as f on f.film_id = fa.film_id 
inner join film_category as fc on fc.film_id = f.film_id 
inner join category as c on c.category_id = fc.category_id 
group by a.actor_id HAVING count(DISTINCT c.category_id) >= 3;

--ex 32: Find films that were never rented but are in inventory.

select f.title from film as f 
left JOIN inventory as i on i.film_id = f.film_id 
LEFT JOIN rental as r on r.inventory_id = i.inventory_id
where rental_id is NULL;

--ex 33:Show customers who rented the same film more than once.

select c.first_name, c.last_name, f.title, count(*) as rental_count from customer as c 
inner join rental as r on c.customer_id = r.customer_id 
inner join inventory as i on i.inventory_id = r.inventory_id
inner join film as f on f.film_id = i.film_id 
group by c.customer_id, f.film_id, f.title 
HAVING count(*) > 1 order by rental_count DESC;

--ex 33: Find the most popular film category based on rental count.

select c.name, count(*) as rental_count from rental as r 
inner join inventory as i on i.inventory_id = r.inventory_id 
inner join film as f on f.film_id = i.film_id 
inner join film_category as fc on fc.film_id = f.film_id 
inner join category as c on c.category_id = fc.category_id 
group by c.name order by rental_count desc limit 1;

--34: List all customers and the number of rentals they made.

select c.first_name, c.last_name, count(*) as rental_count from customer as c 
inner join rental as r on r.customer_id = c.customer_id
group by c.first_name, c.last_name;

--ex 35: Find the top 10 most rented films.

select f.title, count(*) as rental_count from rental as r 
inner join inventory as i on i.inventory_id = r.inventory_id 
inner join film as f on f.film_id = i.film_id 
group by f.title order by rental_count DESC limit 10;

--ex 36: Display each category and the number of films in that category.

select c.name, count(*) as film_count from film as f 
inner join film_category as fc on fc.film_id = f.film_id 
inner join category as c on c.category_id = fc.category_id 
group by c.name order by film_count

--ex 37: Find the total payment amount collected by each staff member.

select s.first_name, s.last_name, sum(amount) as total_amount from payment as p 
inner join staff as s on s.staff_id = p.staff_id 
group by s.first_name, s.last_name  order by total_amount;

--ex 38: List customers who made more than 20 rentals.

select c.first_name, c.last_name, count(*)  from customer as c 
inner join rental as r on r.customer_id = c.customer_id 
group by c.first_name, c.last_name HAVING count(rental_id) > 20;

--ex 39: Find film categories that contain more than 50 films.

select c.name, count(*) as film_count from film as f 
inner join film_category as fc on fc.film_id = f.film_id 
inner join category as c on c.category_id = fc.category_id 
group by c.name HAVING count(f.film_id) > 50;

--ex 40: Display customers whose total payments exceed $100.

select c.first_name, c.last_name, sum(p.amount) as total_amount from customer as c 
inner join payment as p 
on p.customer_id = c.customer_id 
group by c.first_name, c.last_name HAVING sum(p.amount) > 100;

--ex 41: Find actors who appeared in more than 20 films.

select a.first_name, a.last_name, count(*) as film_count from film as f 
inner join film_actor as fa on fa.film_id = f.film_id 
inner join actor as a on a.actor_id = fa.actor_id 
group by a.actor_id HAVING count(f.film_id) > 20;

--ex 42: List films that have been rented more than 15 times.

select f.title, count(*) as rental_count from rental as r 
inner join inventory as i on i.inventory_id = r.inventory_id 
inner join film as f on f.film_id = i.film_id 
GROUP BY f.film_id HAVING count(r.rental_id) > 15;

--ex 43: Show customers who rented films from more than 5 different categories.

select c.first_name, c.last_name, count(DISTINCT fc.category_id) as category_count from customer as c 
inner join rental as r on r.customer_id = c.customer_id 
inner join inventory as i on i.inventory_id = r.inventory_id 
inner join film as f on f.film_id = i.film_id 
inner join film_category as fc on fc.film_id = f.film_id
group by c.customer_id, c.first_name, c.last_name HAVING count(DISTINCT fc.category_id) > 5;

--ex 44: Find films whose rental rate is above the average rental rate.

select title from film where rental_rate > (select avg(rental_rate) from film);

--ex 45: Display customers who made more rentals than the average customer.

select c.first_name, c.last_name, count(r.rental_id) as rental_count from customer as c 
inner join rental as r on r.customer_id = c.customer_id 
group by c.first_name, c.last_name HAVING count(r.rental_id) > (
    select avg(customer_rental.total_rental) from (
        select count(r.rental_id ) as total_rental from rental
        group by customer_id
    ) as customer_rental
);

--ex 46: Find films with replacement costs higher than the average replacement cost.

select title, replacement_cost from film where replacement_cost > (select avg(replacement_cost) from film);

--ex 47: Find the category with the highest total rental count.



--ex 48:  Display customers who rented films from every rating available in the database.

