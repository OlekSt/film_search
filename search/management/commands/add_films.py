from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
import sqlite3


class Command(BaseCommand):
    help = 'Download info about top 300 films'

    def handle(self, *args, **kwargs):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                   AppleWebKit/537.36 (KHTML, like Gecko)\
                   Chrome/90.0.4430.212 Safari/537.36'}
        # webscraping films
        url_films = 'https://www.csfd.cz/zebricky/filmy/nejlepsi/?showMore=1'
        film_page = requests.get(url_films, headers=headers)
        film_content = BeautifulSoup(film_page.content, 'html.parser')
        articles = film_content.find(id='snippet--containerMain')
        films = articles.find_all('article', class_='article')
        # webscraping actors
        url_actors = 'https://www.csfd.cz/zebricky/herci-a-herecky/?showMoreLeft=1&showMoreRight=1'
        actors_page = requests.get(url_actors, headers=headers)
        actors_content = BeautifulSoup(actors_page.content, 'html.parser')
        actors = actors_content.find_all('a', class_='user-title-nick')
        # connecting to the DB
        db = sqlite3.connect('films_actors_01.db')
        c = db.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS films
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     title TEXT,
                     actors TEXT);
                     ''')
        c.execute('''CREATE TABLE IF NOT EXISTS actors
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT,
                     films TEXT);
                     ''')
        
        for film in films:
            title = film.find('a', class_='film-title-name')
            film_url = "https://www.csfd.cz" + title.attrs['href']
            title = title.text.strip()
            # scrape each film individual page for actors
            film_page = requests.get(film_url, headers=headers)
            film_page_content = BeautifulSoup(film_page.content, 'html.parser')
            actors_section = film_page_content.find('h4', string="Hrají: ")
            actors_div = actors_section.find_parent('div')
            film_actors = actors_div.find_all("a", href=lambda href:
                                              href and "tvurce" in href)
            film_actors_list = []
            for film_actor in film_actors:
                film_actor = film_actor.text.strip()
                film_actors_list.append(film_actor)
            film_actors_list = ', '.join(film_actors_list)
            # add films to DB
            c.execute('''INSERT INTO films(title, actors) VALUES(?,?)''',
                      (title, film_actors_list))

        for actor in actors:
            name = actor.text.strip()
            actor_url = "https://www.csfd.cz" + actor.attrs['href'] +\
                        "prehled/"
            actor_page = requests.get(actor_url, headers=headers)
            actor_page_content = BeautifulSoup(actor_page.content,
                                               'html.parser')
            actor_films_list = actor_page_content.find('th', string="Filmy")
            actor_div = actor_films_list.find_parent('tbody')
            actor_films = actor_div.find_all("a", href=lambda href:
                                             href and "film" in href)
            actor_films_list = []
            for actor_film in actor_films:
                actor_film = actor_film.text.strip()
                actor_films_list.append(actor_film)
            actor_films_list = ', '.join(actor_films_list)
            # add actors to DB
            c.execute('''INSERT INTO actors(name, films) VALUES(?,?)''',
                      (name, actor_films_list))

        db.commit()
        db.close()
