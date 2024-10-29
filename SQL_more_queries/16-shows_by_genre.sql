-- Show all shows and their genres, ordered by show title and genre name.
SELECT 
    ts.title AS title, 
    tg.name AS name
FROM 
    tv_shows AS ts
LEFT JOIN 
    tv_show_genres AS tsg ON ts.id = tsg.show_id
LEFT JOIN 
    tv_genres AS tg ON tg.id = tsg.genre_id
ORDER BY 
    ts.title ASC, 
    tg.name ASC;
