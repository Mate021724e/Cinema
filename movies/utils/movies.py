from movies.models import Movie

def get_all_movies():
    """Функція для отримання та виведення всіх фільмів з бази даних."""
    movies = Movie.objects.all()

    # Перевіряємо, чи є фільми
    if movies.exists():
        movies_info = []
        for movie in movies:
            movie_data = {
                'Title': movie.title,
                'Director': movie.directors,
                'Genres': ', '.join([genre.name for genre in movie.genres.all()]),
                'Poster': movie.poster,
            }
            movies_info.append(movie_data)
        return movies_info
    else:
        return "No movies found in the database."