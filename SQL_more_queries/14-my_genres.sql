-- My Genres
SELECT 
    tg.name AS name
FROM 
    tv_genres AS tg
JOIN 
    tv_show_genres AS tsg ON tg.id = tsg.genre_id
JOIN 
    tv_shows AS ts ON ts.id = tsg.show_id
WHERE 
    ts.title = 'Dexter'
ORDER BY 
    tg.name ASC;
