# Working with TMBD API

## Prerequisites

Python 3 should be already installed.

This application requires for personal secret key to use TMDB API. 
Please, set an environment variable TMDB_API_KEY in your system to the 
value of your key. See instructions of getting access to the API on this 
[page](https://www.themoviedb.org/settings/api)

Setup of environment variables on Linux:
```bash
export TMDB_API_KEY=your secret key
```

After registration and configuring system environment you should 
download the database with lots of information about movies from TMDB
```bash
python3 tmdb_api.py number_of_movies
```

## How to use

Getting the budget of the movie by ID
```bash
python3 budget.py movie_id
```

Searching a movie by partial title
```bash
python3 search.py partial_title
```

Getting recommendations by exact title of the movie
```bash
python3 recommend.py title
```
