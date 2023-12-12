-- lists record with secore >= 10 in the table.
SELECT `score`, `name`
FROM `second_table`
WHERE `secore` >= 10
ORDER BY `score` DESC;