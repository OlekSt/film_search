## FILM - ACTOR search app

The purpose of the app is to download a list of TOP 300 films from CSFD.cz, and create an app which can search through the list of films and actors, display search results as a list of links to films and/or actors.
Each link should open a screen with details about a film/actor.
The app is built using Python/Django with SQLite2 DB.

### Database model

SQLITe will be used as a Database.
The database will have two tables:
- films
- actors

##### Films
| **Name** | **Database Key** | **Validation** | **Field Type** | 
--- | --- | --- | --- 
 Title | title | ** | CharField
 Actors | actors | ** | CharField

 ##### Actors
| **Name** | **Database Key** | **Validation** | **Field Type** | 
--- | --- | --- | --- 
 Name | name | ** | CharField
 Films | films | ** | CharField


### RUN the project locally

- You can clone the repository, open it in an IDE of your choice.
- Run 'pip3 install -r requirement.txt' to install all necessesary connections.
- If you need to create 'films_actors.db' again, you need to run 'python3 manage.py add_films', and a new db will be donwloaded. 
