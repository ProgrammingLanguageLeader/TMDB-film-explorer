from tmdb_api import fetch_movie_details, fetch_page_with_movies
from argparse import ArgumentParser
import json


def fetch_movies_ids(movies_number):
    sort_by = 'popularity.desc'

    ids = []
    current_page = 1
    while len(ids) < movies_number:
        page = fetch_page_with_movies(
            page_index=current_page,
            sort_by=sort_by
        )
        for result in page['results']:
            ids.append(int(result['id']))
            if len(ids) == movies_number:
                break
        current_page += 1
    return ids


def load_movies_data_from_file(db_path):
    with open(db_path, 'r') as file:
        return json.load(file)


def fetch_movies_data(movies_number):
    movies_ids = fetch_movies_ids(movies_number)

    movies_data = [
        fetch_movie_details(movie_id) for movie_id in movies_ids
    ]
    return movies_data


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        'movies_number',
        type=int,
        help='movies number to fetch'
    )
    parser.add_argument(
        '-p',
        '--db_path',
        default='db.json',
        help='a path to the json file which will be used as a database'
    )
    args = parser.parse_args()
    db_path = args.db_path
    movies_number = args.movies_number
    with open(db_path, 'w') as file:
        db = fetch_movies_data(movies_number)
        json.dump(db, file)
