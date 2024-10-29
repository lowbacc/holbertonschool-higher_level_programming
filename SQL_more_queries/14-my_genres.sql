-- Use the tv_shows database
SELECT genres.name
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')
ORDER BY genres.name ASC;