SELECT title, release_year, category.name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name='Comedy' OR category.name='Action' OR category.name='Family';