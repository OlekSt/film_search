from django.shortcuts import render
import sqlite3


def film(request):
    db = sqlite3.connect('films_actors_01.db')
    c = db.cursor()
    c.execute('''SELECT * FROM films WHERE title="The Matrix" ''')
    film = c.fetchone()
    title = film[1]
    actor_list = film[2]
    print(actor_list)
    actor_list = actor_list.split(", ")

    context = {
        'title': title,
        'actor_list': actor_list,
    }

    return render(request, 'details/details.html', context)


def actor(request):
    db = sqlite3.connect('films_actors_01.db')
    c = db.cursor()
    c.execute('''SELECT * FROM films WHERE title="item"''')
    films = c.fetchall()
    # c.execute('''SELECT * from actors ''')
    # actor = c.fetchall()
    for film in films:
        title = film[0]
        actor_list = film[1]
        actor_list = actor_list.split(", ")
    context = {
        'title': title,
        'actor_list': actor_list,
    }

    return render(request, 'details/details.html', context)
