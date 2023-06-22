SELECT category.name, COUNT(*) AS number_of_films
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
GROUP BY category.name
HAVING COUNT(category.name)>60 AND COUNT(category.name)<68;