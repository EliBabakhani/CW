SELECT title, length , (SELECT AVG(length) FROM film)
FROM film
WHERE length>(SELECT AVG(length) FROM film)

