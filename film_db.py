import tmdb_api
import json
import urllib.error
import logging
import sys


def load_database_from_file(address: str) -> dict:
    try:
        with open(address, 'r') as f:
            s = "\n".join(f.readlines())
            return json.loads(s)
    except IOError:
        raise


def save_database_in_file(address: str, db: dict):
    with open(address, 'w') as f:
        f.write(json.dumps(db))


def load_movies_id_from_file(address: str) -> list:
    try:
        with open(address, 'r') as f:
            return list(map(int, f.read().split(' ')))
    except (IOError, ValueError):
        raise


def save_movies_id_list_in_file(address: str, id_list: list):
    with open(address, 'w') as f:
        f.write(' '.join([str(e) for e in id_list]))


def fetch_movies_id_list(number: int) -> list:
    id_list = []
    results_on_page = 20
    pages_required = number // results_on_page + (1 if number % results_on_page != 0 else 0)
    for current_page in range(1, pages_required + 1):
        try:
            info = tmdb_api.fetch_movies_page_dict(page=current_page, sort_by='popularity.desc')
            for order in range(0, 20):
                id_list.append(int(info['results'][order]['id']))
                if len(id_list) == number:
                    break
        except urllib.error.URLError:
            raise
        except ValueError:
            raise
    return id_list


def fetch_details(id_list: list) -> dict:
    details_dict = {}
    for movie_id in id_list:
        try:
            details_dict[movie_id] = tmdb_api.fetch_movie_details_dict(movie_id)
        except urllib.error.URLError:
            raise
    return details_dict


def fetch_lists(id_list: list) -> dict:
    lists_dict = {}
    for movie_id in id_list:
        try:
            lists_dict[movie_id] = tmdb_api.fetch_movie_lists_dict(movie_id)
        except urllib.error.URLError:
            raise
    return lists_dict


def fetch_keywords(id_list: list) -> dict:
    keywords_dict = {}
    for movie_id in id_list:
        try:
            keywords_dict[movie_id] = tmdb_api.fetch_movie_keywords_dict(movie_id)
        except urllib.error.URLError:
            raise
    return keywords_dict


def obtain_movies_data(
        films_number: int,
        movies_id_list_address: str,
        details_database_address: str = None,
        lists_database_address: str = None,
        keywords_database_address: str = None
) -> tuple:
    """
    Obtain movies data and returns a tuple in this order: movies_id, details, keywords, lists
    """
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    movies_id_list = []
    try:
        logging.info('Try to load data from %s' % movies_id_list_address)
        movies_id_list = load_movies_id_from_file(address=movies_id_list_address)
        logging.info('Successful')
    except (IOError, ValueError):
        try:
            logging.info('Failed')
            logging.info('Getting IDs of the most popular films...')
            movies_id_list = fetch_movies_id_list(number=films_number)
            save_movies_id_list_in_file(address=movies_id_list_address, id_list=movies_id_list)
            logging.info('Saved')
        except urllib.error.URLError:
            logging.error('Bad Internet connection or incorrect query')
            exit(1)

    details_dict = {}
    if details_database_address:
        try:
            logging.info('Try to load data from %s' % details_database_address)
            details_dict = load_database_from_file(address=details_database_address)
            logging.info('Successful')

        except IOError:
            try:
                logging.info('Failed')
                logging.info('Getting films details database...')
                details_dict = fetch_details(id_list=movies_id_list)
                save_database_in_file(address=details_database_address, db=details_dict)
                logging.info('Saved')
            except urllib.error.URLError:
                logging.error('Bad Internet connection or incorrect query')
                exit(1)

    lists_dict = {}
    if lists_database_address:
        try:
            logging.info('Try to load data from %s' % lists_database_address)
            lists_dict = load_database_from_file(address=lists_database_address)
            logging.info('Successful')
        except IOError:
            try:
                logging.info('Failed')
                logging.info('Getting films lists database...')
                lists_dict = fetch_lists(id_list=movies_id_list)
                save_database_in_file(address=lists_database_address, db=lists_dict)
                logging.info('Saved')
            except urllib.error.URLError:
                logging.error('Bad Internet connection or incorrect query')
                exit(1)

    keywords_dict = {}
    if keywords_database_address:
        try:
            logging.info('Try to load data from %s' % keywords_database_address)
            keywords_dict = load_database_from_file(address=keywords_database_address)
            logging.info('Successful')
        except IOError:
            try:
                logging.info('Failed')
                logging.info('Getting films lists database...')
                keywords_dict = fetch_keywords(id_list=movies_id_list)
                save_database_in_file(address=keywords_database_address, db=keywords_dict)
                logging.info('Saved')
            except urllib.error.URLError:
                logging.error('Bad Internet connection or incorrect query')
                exit(1)
    return movies_id_list, details_dict, lists_dict, keywords_dict
