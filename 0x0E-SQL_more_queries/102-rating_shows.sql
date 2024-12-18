-- List all shows and their rating sum
-- sorted by rating sum in descending order

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating_sum
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
