from argparse import ArgumentParser

from tmdb_db import load_movies_data_from_file


def get_movie_by_title(title, movies_data):
    for movie_data in movies_data:
        if movie_data['title'].lower() == title.lower():
            return movie_data


def get_recommendations(source_movie, movies_data):
    common_keywords_to_recommend = 4
    common_lists_to_recommend = 8

    recommendations = set()
    for movie in movies_data:
        if movie == source_movie:
            continue
        movie_lists = set([
            result['name'] for result in movie['lists']['results']
        ])
        source_movie_lists = set([
            result['name'] for result in source_movie['lists']['results']
        ])
        common_lists = movie_lists & source_movie_lists
        if len(common_lists) > common_lists_to_recommend:
            recommendations.add(movie['title'])

        movie_keywords = set([
            keyword['name'] for keyword in movie['keywords']['keywords']
        ])
        source_movie_keywords = set([
            keyword['name'] for keyword in source_movie['keywords']['keywords']
        ])
        common_keywords = movie_keywords & source_movie_keywords
        if len(common_keywords) > common_keywords_to_recommend:
            recommendations.add(movie['title'])
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
