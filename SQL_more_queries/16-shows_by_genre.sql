-- Show the title of each TV show and the genre that it belongs to, ordered by title and genre name.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;