-- lists all shows without genre linked
SELECT s.`title`, g.`genre_id`
FROM tv_shows AS s
	FULL JOIN tv_show_genres AS g
	ON s.`id` = g.`genre_id`
	WHERE g.`genre_id` = NULL
ORDER BY s.`title`, g.`genre_id`;
