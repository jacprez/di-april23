-- SELECT * FROM language

-- SELECT film.title, film.description, language.name FROM film
-- INNER JOIN language ON film.language_id=language.language_id

-- SELECT film.title, film.description, language.name FROM film
-- RIGHT JOIN language ON film.language_id=language.language_id


-- CREATE TABLE new_film(
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(100)
-- )

-- INSERT INTO new_film (name)
-- VALUES ('Harry Potter'), ('Shawshank Redemption'), ('WALL-E'), ('Inception')

-- SELECT * FROM new_film

-- CREATE TABLE customer_review (
-- 	review_id SERIAL PRIMARY KEY NOT NULL,
-- 	film_id INT NOT NULL,
-- 	language_id INT NOT NULL,
-- 	title VARCHAR(100) NOT NULL,
-- 	score INT NOT NULL,
-- 	review_text TEXT,
-- 	last_update TIMESTAMP DEFAULT current_timestamp,
-- 	CONSTRAINT score_value CHECK (score > 0 AND score <= 10),
-- 	CONSTRAINT fk_language_id FOREIGN KEY (language_id) REFERENCES language(language_id),
-- 	CONSTRAINT fk_film_id FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE

-- )


-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES
-- (1, 1, 'Cool film!', 10, 'I love the harry potter films. They are my favorite and i love that there are so many!' ),
-- (2, 1, 'It was okay', 6, 'Really long movie that was dragged out. Hard to watch.')

-- SELECT * FROM customer_review
-- DELETE FROM new_film 
-- WHERE (name='Harry Potter') RETURNING *


-- Exercise 2 : DVD Rental

-- 1.
-- SELECT * FROM film
-- INNER JOIN language ON film.language_id = language.language_id
-- WHERE title = 'Chamber Italian'

-- SELECT * FROM film
-- INNER JOIN language ON film.language_id = language.language_id
-- WHERE title = 'Academy Dinosaur'

-- UPDATE film 
-- SET language_id=2
-- WHERE (title='Chamber Italian')

-- UPDATE film 
-- SET language_id=2
-- WHERE (title='Academy Dinosaur')

-- SELECT * FROM customer 
-- INSERT INTO customer (first_name, last_name, store_id, address_id)
-- VALUES ('Jackie', 'Prez', 1, 1)

-- 2.
-- SELECT * FROM customer
-- WHERE first_name='Jackie'

-- 3.
-- DROP table customer_review

-- 4.
-- SELECT COUNT(*) FROM rental
-- WHERE return_date IS NULL

-- 5.
-- SELECT * FROM rental
-- INNER JOIN inventory on rental.inventory_id = inventory.inventory_id
-- LEFT JOIN film ON inventory.film_id = film.film_id
-- WHERE rental.return_date IS NULL
-- ORDER BY film.replacement_cost DESC
-- LIMIT 30

-- 6. - 1.
-- SELECT film.film_id, film.title, film.fulltext FROM film_actor
-- INNER JOIN film ON film.film_id=film_actor.film_id
-- WHERE actor_id=(
-- SELECT actor_id FROM actor WHERE (first_name = 'Penelope' AND last_name = 'Monroe') AND film.fulltext @@ to_tsquery('english', 'sumo')
-- )

-- 6. -2.
SELECT * FROM film 
INNER JOIN film_category ON
WHERE length<60 AND rating ='R'

-- Didn't finish

