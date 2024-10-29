-- Count the number of shows for each genre, and display the genres in descending order of the number of shows.
SELECT 
    tg.name AS genre, 
    COUNT(tsg.show_id) AS number_of_shows
FROM 
    tv_genres AS tg
JOIN 
    tv_show_genres AS tsg ON tg.id = tsg.genre_id
GROUP BY 
    tg.name
HAVING 
    COUNT(tsg.show_id) > 0
ORDER BY 
    number_of_shows DESC;
