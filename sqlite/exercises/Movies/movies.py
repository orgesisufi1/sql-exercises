import sqlite3 as sq
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'movies.db')

database_path = filename


con = sq.connect(database_path)
cur = con.cursor()

#Importing Create Table function from utilities
from utility import createTable


#Calling Create Table function
# createTable(database_path, 'Movies', 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL', 'title TEXT NOT NULL', 'duration INTEGER NOT NULL', 'release_date TEXT NOT NULL', 'genre_id INTEGER NOT NULL', 'FOREIGN KEY (genre_id) REFERENCES Genres(id)')

# createTable(database_path, 'Actors', 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL', 'name TEXT NOT NULL', 'date_of_birth TEXT NOT NULL', 'gender TEXT NOT NULL')

# createTable(database_path, 'Awards', 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL', 'title TEXT NOT NULL', 'date TEXT NOT NULL', 'category TEXT NOT NULL')

# createTable(database_path, 'MovieActors', 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL', 'movie_id INTEGER NOT NULL', 'actors_id INTEGER NOT NULL', 'FOREIGN KEY(movie_id) REFERENCES Movies(id)', 'FOREIGN KEY(actors_id) REFERENCES Actors(id)')

# createTable(database_path, 'ActorsAwards', 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL', 'actor_id INTEGER NOT NULL', 'award_id INTEGER NOT NULL', 'year INTEGER NOT NULL', 'FOREIGN KEY(actor_id) REFERENCES Actors(id)', 'FOREIGN KEY(award_id) REFERENCES Awards(id)')

# createTable(database_path, 'MoviesAward', 'id INTEGER PRIMARY KEY NOT NULL', 'movies_id INTEGER NOT NULL', 'award_id INTEGER NOT NULL','year INTEGER', 'FOREIGN KEY(movies_id) REFERENCES Movies(id)', 'FOREIGN KEY(award_id) REFERENCES Awards(id)')