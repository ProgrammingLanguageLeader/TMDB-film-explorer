# TMDB film explorer

The first home assignment of a Python course published here - http://melevir.com/things/python_styleru/

## Getting Started

These instructions will get you a copy of the project up and running on your local 
machine for development and testing purposes

### Prerequisites

1. You need Python 3 on your machine to use this project. See instructions about 
installing of Python on this page - https://wiki.python.org/moin/BeginnersGuide/Download
2. This application requires for personal secret key to use TMDB API. Please, set an environment
 variable TMDB_API_KEY in your system to the value of your key. See instructions of getting access
  to API on this page - https://www.themoviedb.org/settings/api

### Installing

Download the repository from GitHub.com page or if you use git just type following commands in console

```
git clone https://github.com/ProgrammingLanguageLeader/film_explorer
```

## Structure of the project

#### _**tmdb_api.py**_
This is a module for work with TMDB API (see https://www.themoviedb.org/documentation/api)

#### **_budget.py_**
A Python script asks for a film's ID and shows its budget if the ID is valid.
The program takes one parameter - id of the film.
Example of usage
```
python budget.py 215
The budget of "Пила 2" is $4000000
```

#### **_film_db.py_**
This is a module for work with JSON files which contain information about films. 

#### **_film_searching.py_**
A Python program asks for a film's title and searches for it.
The program takes one parameter - title of the film. 
Example of usage
```
python film_searching.py Пила
2017-04-03 01:55:27,946 - INFO - Try to load data from movies_id.txt
2017-04-03 01:55:27,946 - INFO - Successful
2017-04-03 01:55:27,946 - INFO - Try to load data from db_details.json
2017-04-03 01:55:28,015 - INFO - Successful
Films found:
Пила 2
Пила. Игра на выживание
```

#### **_film_recommendations.py_**
A Python script asks for an exact film's title and suggest recommendations for user.
It takes one parameter - title of the film.
Example of usage
```
python film_recommendations.py "Красавица и чудовище"
2017-04-03 02:06:57,631 - INFO - Try to load data from movies_id.txt
2017-04-03 02:06:57,631 - INFO - Successful
2017-04-03 02:06:57,632 - INFO - Try to load data from db_details.json
2017-04-03 02:06:57,703 - INFO - Successful
2017-04-03 02:06:57,704 - INFO - Try to load data from db_lists.json
2017-04-03 02:06:57,766 - INFO - Successful
2017-04-03 02:06:57,766 - INFO - Try to load data from db_keywords.json
2017-04-03 02:06:57,778 - INFO - Successful
Films recommended to watch:
Амадей
Унесённые призраками
Гарри Поттер и философский камень
Труп невесты
Мулан
Она
Белоснежка и охотник
Белоснежка и Охотник 2
Шрэк
...
Настоящая девчонка
Отверженные
```