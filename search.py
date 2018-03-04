from tmdb_db import load_movies_data_from_file
from argparse import ArgumentParser


def get_movie_by_title(title, movies_data):
    for movie_data in movies_data.values():
        if movie_data['details']['title'].lower() == title.lower():
            return movie_data


def get_movies_with_similar_title(requested_title, movies_data):
    result = []
    for movie_data in movies_data.values():
        movie_title = movie_data['details']['title']
        if movie_title.lower().find(requested_title.lower()) >= 0:
            result.append(movie_title)
    return result


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        'search_string',
        help='string to search in titles'
    )
    parser.add_argument(
        '-p',
        '--db_path',
        default='db.json',
        help='a path to the json file which will be used as a database'
    )
    args = parser.parse_args()
    search_string = args.search_string
    db_path = args.db_path

    movies = load_movies_data_from_file(db_path)
    found = get_movies_with_similar_title(search_string, movies)

    if not found:
        print('Not found')
        exit()
    output = 'Movies found:'
    for title in found:
        output += '\n\t{}'.format(title)
    print(output)
