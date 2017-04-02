import film_db
import film_searching
import sys


if __name__ == '__main__':
    movies_id, details, lists, keywords = film_db.obtain_movies_data(
        films_number=1000,
        movies_id_list_address='movies_id.txt',
        details_database_address='db_details.json',
        lists_database_address='db_lists.json',
        keywords_database_address='db_keywords.json'
    )

    title = ''
    try:
        title = sys.argv[1]
    except IndexError:
        title = str(input('Enter a film title: '))
    found = film_searching.search_film_in_details_db(data=title, details=details, clarified=True)
    if len(found) == 0:
        print('Clarify the title')
        exit()
    else:
        recommended = set()
        film_id = film_searching.get_film_id_by_title(title=title, details=details)
        # recommendations by keywords
        keywords_found = set([x['name'] for x in keywords[film_id]['keywords']])
        for movie_id in keywords:
            if film_id != movie_id:
                current_keywords = set([x['name'] for x in keywords[movie_id]['keywords']])
                if len(keywords_found & current_keywords) > 0:
                    recommended.add(details[movie_id]['title'])
        # recommendations by lists
        lists_found = set([x['name'] for x in lists[film_id]['results']])
        for movie_id in lists:
            if film_id != movie_id:
                current_lists = set([x['name'] for x in lists[movie_id]['results']])
                if len(lists_found & current_lists) > 16:
                    recommended.add(details[movie_id]['title'])
        print('Films recommended to watch:', *recommended, sep='\n')

