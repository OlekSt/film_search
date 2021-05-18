from django.shortcuts import render
import sqlite3


def index(request):
    db = sqlite3.connect('films_actors_01.db')
    c = db.cursor()

    c.execute('''SELECT * from films''')
    films = c.fetchall()
    c.execute('''SELECT * from actors''')
    actors = c.fetchall()

    query = None

    searched_films = []
    for film in films:
        if request.GET:
            query = request.GET['q']
            if query.lower() in film[1].lower():
                searched_films.append(film)
                print(searched_films)

    searched_actors = []
    for actor in actors:
        if request.GET:
            query = request.GET['q']
            if query.lower() in actor[1].lower():
                searched_actors.append(actor)

    context = {
        'films': searched_films,
        'actors': searched_actors,
        'search_term': query,
    }

    return render(request, 'search/index.html', context)
