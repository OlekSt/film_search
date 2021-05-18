from django.shortcuts import render
import sqlite3


def film(request):
    db = sqlite3.connect('films_actors_01.db')
    c = db.cursor()
    c.execute('''SELECT * FROM films WHERE title="The Matrix" ''')
    film = c.fetchone()
    title = film[1]
    actor_list = film[2]
    actor_list = actor_list.split(", ")

    context = {
        'title': title,
        'list': actor_list,
    }

    return render(request, 'details/details.html', context)


def actor(request):
    db = sqlite3.connect('films_actors_01.db')
    c = db.cursor()
    c.execute('''SELECT * FROM actors WHERE name="Matt Damon"''')
    actor = c.fetchone()
    
    name = actor[1]
    film_list = actor[2]
    film_list = film_list.split(", ")

    context = {
        'title': name,
        'list': film_list,
    }

    return render(request, 'details/details.html', context)
