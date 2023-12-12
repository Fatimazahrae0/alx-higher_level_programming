-- Lists all records of the table.
SELECT `score`, `name`
FROM `score_table`
WHERE `name` != ""
ORDER BY `score` DESC