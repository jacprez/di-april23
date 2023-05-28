-- Exercise 2 : Dvdrental Database
-- 1.
-- SELECT * FROM customer

-- 2. 
-- SELECT (first_name, last_name) AS full_name FROM customer

-- 3. 
-- SELECT DISTINCT create_date FROM customer

-- 4. 
-- SELECT * FROM customer
-- ORDER BY first_name DESC

-- 5. 
-- SELECT film_id, title, description, release_year, rental_rate FROM film
-- ORDER BY rental_rate ASC

-- 6. 
-- SELECT address, phone FROM address
-- WHERE district = 'Texas'

-- 7. 
-- SELECT * FROM film
-- WHERE film_id = 15 OR film_id = 50

-- 8. 
-- SELECT film_id, title, description, length, rental_rate FROM film 
-- WHERE title = 'Shes the Man'

-- 9.
-- SELECT film_id, title, description, length, rental_rate FROM film 
-- WHERE title LIKE 'Sh%'

-- 10.
-- SELECT title, rental_rate FROM film
-- ORDER BY rental_rate ASC
-- LIMIT 10

-- 11.
-- SELECT title, rental_rate FROM film
-- ORDER BY rental_rate ASC
-- LIMIT 20 OFFSET 10


-- 12.
-- SELECT Customer.customer_id, Customer.first_name, Customer.last_name, Payment.amount FROM customer
-- LEFT JOIN payment ON Customer.customer_id = Payment.customer_id
-- ORDER BY Customer.customer_id ASC


-- 13.
-- SELECT * FROM inventory
-- WHERE inventory_id = NULL

-- 14.Write a query to find which city is in which country.
-- SELECT city.city, country.country FROM city
-- JOIN country ON city.country_id = country.country_id 


