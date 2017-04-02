import film_db
import sys


def search_film_in_details_db(details: dict, data: str, clarified=False) -> list:
    if not clarified:
        result = []
        for x in details.values():
            s = str(x['title']).lower()
            if s.find(data.lower()) >= 0:
                result.append(x['title'])
        return result
    else:
        for x in details.values():
            s = str(x['title'])
            if s == data:
                return [x['title']]
        return []


def get_film_id_by_title(details: dict, title: str) -> int:
    for movie_id in details.keys():
        if details[movie_id]['title'] == title:
            return movie_id
    return -1


if __name__ == '__main__':
    movies_id, details, keywords, lists = film_db.obtain_movies_data(
        films_number=1000,
        movies_id_list_address='movies_id.txt',
        details_database_address='db_details.json'
    )
    title = ''
    try:
        title = sys.argv[1]
    except IndexError:
        title = str(input('Enter a title of the film: '))
    found = search_film_in_details_db(data=title, details=details)
    if len(found) == 0:
        print('Not found')
    else:
        print('Films found:\n', '\n'.join(found), sep='')
