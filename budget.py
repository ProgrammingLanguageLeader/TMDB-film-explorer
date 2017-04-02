import tmdb_api
import sys
import urllib.error


if __name__ == "__main__":
    movie_id = 0
    try:
        movie_id = int(sys.argv[1])
    except (IndexError, ValueError):
        try:
            movie_id = int(input('Enter an ID of the movie: '))
        except ValueError:
            print('Incorrect value')
            exit(1)
    try:
        info = tmdb_api.fetch_movie_details_dict(film_id=movie_id)
        print('The budget of "', info['title'], '" is $', info['budget'], sep='')
    except urllib.error.URLError:
        print('Movie with this ID does not exist or bad Internet connection')
        exit(1)
