-- Script to list all TV shows without a genre linked
-- Results: tv_shows.title - tv_show_genres.genre_id
-- Sorted by tv_shows.title and tv_show_genres.genre_id

USE hbtn_0d_tvshows;

SELECT
	tv_shows.title,
	tv_show_genres.genre_id
FROM
	tv_shows
LEFT JOIN
	tv_show_genres
ON
	tv_shows.id = tv_show_genres.show_id
WHERE
	tv_show_genres.genre_id IS NULL
ORDER BY
	tv_shows.title ASC,
	tv_show_genres.genre_id ASC;
