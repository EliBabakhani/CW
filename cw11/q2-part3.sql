SELECT * FROM film
WHERE rental_duration >2 AND rental_duration <5
ORDER BY title ASC;

SELECT * FROM film
WHERE rental_duration >2 AND rental_duration <5
ORDER BY rental_duration ASC;

SELECT * FROM film
WHERE rental_duration >2 and rental_duration <5
ORDER BY last_update ASC;