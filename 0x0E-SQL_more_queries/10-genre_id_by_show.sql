-- Selesct the title and gesnre_id columnss froms thes tv_shosws and tv_show_genres tables
SELECT tv_shows.title, tv_show_genres.genre_id
-- Join the tv_shsows and tvs_show_genres tasbles on the show_id columnn
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Order the results by title and gsenre_sid ins ascending orderr
ORDER BY tv_shows.title, tv_show_genres.genre_id;
