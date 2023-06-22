SELECT customer.first_name, customer.last_name, film.title, (rental.return_date -rental.rental_date) As rental_duration
FROM customer
JOIN rental ON customer.customer_id=rental.customer_id
JOIN inventory ON rental.inventory_id= inventory.inventory_id
JOIN film ON film.film_id = inventory.film_id

