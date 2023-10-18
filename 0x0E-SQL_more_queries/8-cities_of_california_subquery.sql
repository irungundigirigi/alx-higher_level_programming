-- Lists all cities of California in db hbtn_0d_usa
-- Order ascending
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN 
	(SELECT `id`
	FROM `states`
	WHERE `name` = "California")
	ORDER BY `id`;
