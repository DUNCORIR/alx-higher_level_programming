-- Script that lists all Comedy shows in the database hbtn_0d_tvshows
-- sorted by title in ascending order.

SELECT
	tv_shows.title
FROM
	tv_shows
INNER JOIN
	tv_shows_genres
ON
	tv_shows.id = tv_shows_genres.show_id
INNER JOIN
	tv_genres
ON
	tv_show_genres.genre_id = tv_genres.id
WHERE
	tv_genres.name = 'Comedy'
ORDER BY
	tv_shows.title ASC;
