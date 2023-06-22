SELECT category.name, film.title, language.name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN language ON film.language_id=language.language_id
JOIN category ON film_category.category_id = category.category_id
