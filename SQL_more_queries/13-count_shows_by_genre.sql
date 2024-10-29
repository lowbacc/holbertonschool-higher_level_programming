-- Count the number of shows for each genre.
SELECT 
    g.name AS genre, 
    COUNT(sg.show_id) AS number_of_shows
FROM 
    genres AS g
JOIN 
    shows_genres AS sg ON g.id = sg.genre_id
GROUP BY 
    g.name
HAVING 
    COUNT(sg.show_id) > 0
ORDER BY 
    number_of_shows DESC;
