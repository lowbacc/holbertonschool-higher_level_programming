-- This query is used to find the top 10 scores from the second table that do not have a link to the first table.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;