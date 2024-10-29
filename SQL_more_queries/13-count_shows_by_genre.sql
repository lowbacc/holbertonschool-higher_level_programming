-- Count the number of shows for each genre. Order the result by the number of shows in descending order.
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;