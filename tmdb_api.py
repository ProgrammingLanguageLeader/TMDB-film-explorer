import urllib.request
import urllib.parse
import urllib.error
import json
import os


app_api_key = ""
try:
    app_api_key = os.environ['TMDB_API_KEY']
except KeyError:
    print('Please, set a TMDB_API_KEY variable')
    exit(1)


def load_json_data_from_url(base_url, url_params) -> dict:
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    try:
        response = urllib.request.urlopen(url).read().decode('utf-8')
        return json.loads(response)
    except urllib.error.URLError:
        raise


def make_tmdb_api_request(method, api_key, extra_params=None) -> dict:
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


def fetch_movie_details_dict(film_id: int) -> dict:
    return make_tmdb_api_request(method='/movie/%d' % film_id, api_key=app_api_key)


def fetch_movie_lists_dict(film_id: int):
    return make_tmdb_api_request(method='/movie/%d/lists' % film_id, api_key=app_api_key)


def fetch_movie_keywords_dict(film_id: int) -> dict:
    return make_tmdb_api_request(method='/movie/%d/keywords' % film_id, api_key=app_api_key)


def fetch_movies_page_dict(page: int, sort_by: str) -> dict:
    extra_params = {
        'page': page,
        'sort_by': sort_by
    }
    return make_tmdb_api_request(method='/discover/movie', api_key=app_api_key, extra_params=extra_params)
