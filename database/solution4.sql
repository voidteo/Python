--ex 1: Select all customers whose email IS NULL.

select * from customer where email is NULL;

--ex 2: Select all customers whose email IS NOT NULL.

select * from customer where email is not NULL;

--ex 3: Count how many films have a release_year IS NULL.

select count(*) from film where release_year is NULL;

--ex 4: Select all rentals where return_date IS NULL (i.e., not returned).

select * from rental where return_date is NULL;

--ex 5: Count rentals where return_date IS NOT NULL.

select count(*) from rental where return_date is not NULL;

--ex 6: Select all staff records where picture IS NULL.

select * from staff where picture is NULL;

--ex 7: Select all payments where amount IS NULL (should return none — tests understanding).

select * from payment where amount is NULL;

--ex 8: Find all addresses where address2 IS NULL.

select * from address where address is NULL;

--ex 9: Count how many addresses have address2 filled (IS NOT NULL).

select count(*) from address where address2 is NOT NULL;

--ex 10: Select all films where special_features IS NULL (to confirm if column allows NULL).

select * from film where special_features is NULL;

--ex 11: View structure of customer table using \d customer; identify the primary key.

--ex 12: View structure of film table; list all NOT NULL columns.

--ex 13: View structure of rental table; identify which columns form the primary key.

--ex 14: Attempt to insert a duplicate value into a primary key column (should fail).

insert into language(language_id, name) values(1, 'Uzbek');

--ex 15: Attempt to insert a record missing a NOT NULL column (should fail).

insert into actor(actor_id, first_name) values(99, 'Anivar');

--ex 16: Identify which columns in customer table have DEFAULT values.

--ex 17: View which column(s) in rental table are foreign keys (read only, not use them).

--ex 18: Check if payment_id column in payment table is marked as PRIMARY KEY.

--ex 19: Find which columns in film table have CHECK or DEFAULT constraints (e.g., rental_rate, rating).

--ex 20: Inspect store table; identify its primary key and any unique constraints.

