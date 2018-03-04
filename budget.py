from tmdb_api import fetch_movie_details
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        'movie_id',
        type=int,
        help='an ID of the movie',

    )
    args = parser.parse_args()
    movie_id = args.movie_id
    info = fetch_movie_details(movie_id)
    print(
        'The budget of "{}" is ${}'.format(
            info['title'], info['budget']
        )
    )
