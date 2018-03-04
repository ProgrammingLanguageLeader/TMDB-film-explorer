from argparse import ArgumentParser

from tmdb_db import load_movies_data_from_file
from search import get_movie_by_title


def get_recommendations(source_movie, movies_data):
    recommendations = set()
    for movie in movies_data.values():
        if movie == source_movie:
            continue
        movie_lists = set([
            result['name'] for result in movie['lists']['results']
        ])
        source_movie_lists = set([
            result['name'] for result in source_movie['lists']['results']
        ])
        if len(movie_lists & source_movie_lists) > 8:
            recommendations.add(movie['details']['title'])

        movie_keywords = set([
            keyword['name'] for keyword in movie['keywords']['keywords']
        ])
        source_movie_keywords = set([
            keyword['name'] for keyword in source_movie['keywords']['keywords']
        ])
        if len(movie_keywords & source_movie_keywords) > 3:
            recommendations.add(movie['details']['title'])
    return recommendations


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        'title',
        help='a title of the movie to get recommendations'
    )
    parser.add_argument(
        '-p',
        '--db_path',
        default='db.json',
        help='a path to the json file which will be used as a database'
    )
    args = parser.parse_args()
    title = args.title
    db_path = args.db_path

    movies = load_movies_data_from_file(db_path)
    source_movie = get_movie_by_title(title, movies)
    if not source_movie:
        print('Clarify the title')
        exit()

    recommendations = get_recommendations(source_movie, movies)
    if not recommendations:
        print('Can\'t recommend something on this request')
        exit()
    output = 'Movies recommended to watch:'
    for title in recommendations:
        output += '\n\t{}'.format(title)
    print(output)
