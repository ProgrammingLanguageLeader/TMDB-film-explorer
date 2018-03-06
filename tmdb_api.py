import urllib.request
import urllib.parse
import urllib.error
import json
import os


TMBD_API_KEY = os.environ['TMDB_API_KEY']


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'en-US',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


def fetch_movie_details(movie_id):
    extra_params = {
        'append_to_response': 'keywords,lists'
    }
    return make_tmdb_api_request(
        method='/movie/%d' % movie_id,
        api_key=TMBD_API_KEY,
        extra_params=extra_params
    )


def fetch_page_with_movies(page_index, sort_by):
    extra_params = {
        'page': page_index,
        'sort_by': sort_by
    }
    return make_tmdb_api_request(
        method='/discover/movie',
        api_key=TMBD_API_KEY,
        extra_params=extra_params
    )
