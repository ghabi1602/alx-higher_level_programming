-- lists all shows without genre linked
SELECT s.`title`, g.`genre_id`
FROM tv_shows AS s
	FULL JOIN tv_show_genres AS g
	WHERE g.`genre_id` = NULL
ORDER BY s.`title`, g.`genre_id`;
