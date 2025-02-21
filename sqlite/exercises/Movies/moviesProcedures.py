import sqlite3 as sq
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'movies.db')

database_path = filename


con = sq.connect(database_path)
cur = con.cursor()

def actorsSortedByAwardsWon(genre_name):
    cur.execute(f"""
    SELECT 
        Actors.id, 
        Actors.name, 
        Genres.genre_name,
        COUNT(Awards.id) AS total_awards
    FROM Actors
    INNER JOIN MovieActors ON Actors.id = MovieActors.actors_id
    INNER JOIN Movies ON MovieActors.movie_id = Movies.id
    INNER JOIN Genres ON Movies.genre_id = Genres.id
    LEFT JOIN ActorsAwards ON Actors.id = ActorsAwards.actor_id  
    LEFT JOIN Awards ON ActorsAwards.award_id = Awards.id
    WHERE Genres.genre_name = {genre_name}
    GROUP BY Actors.id, Actors.name, Genres.genre_name
    ORDER BY total_awards DESC
    LIMIT 5;
""")
    x = cur.fetchall()
    print(x[0])


def findActorsBasedOnDurationAndGenre(duration, genre_id):
    cur.execute(f"""
    SELECT Actors.name, Movies.title, Genres.genre_name, Movies.duration
    FROM Movies
    JOIN MovieActors ON Movies.id = MovieActors.movie_id
    JOIN Actors ON MovieActors.actors_id = Actors.id
    JOIN Genres ON Movies.genre_id = Genres.id
    WHERE Movies.duration < {duration} AND Movies.genre_id = {genre_id};
""")
    
    x = cur.fetchall()
    print(x[0])