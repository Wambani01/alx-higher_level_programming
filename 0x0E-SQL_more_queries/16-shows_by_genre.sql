-- nested inner left
select tv_shows.title, tv_genres.name from tv_shows left join tv_show_genres on tv_shows.id = tv_show_genres.show_id left join tv_genres on tv_show_genres.genre_id = tv_genres.id;
