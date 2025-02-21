import sqlite3 as sq
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'movies.db')

database_path = filename


con = sq.connect(database_path)
cur = con.cursor()

s1 = """
    SELECT Movies.id, Movies.title, Genres.genre_name
    FROM Movies
    INNER JOIN Genres on Movies.genre_id = Genres.id
"""

s2 = """
    SELECT Actors.id, Actors.name, Genres.genre_name
    FROM Actors
    INNER JOIN MovieActors ON Actors.id = MovieActors.actors_id
    INNER JOIN Movies ON MovieActors.movie_id = Movies.id
    INNER JOIN Genres ON Movies.genre_id = Genres.id
"""

s3 = """
    SELECT Genres.genre_name, 
    Count(Movies.id) AS total_movies, 
    Avg(Movies.duration) AS average_duration 
    FROM Movies
    INNER JOIN Genres ON Movies.genre_id = Genres.id
    GROUP BY Genres.genre_name
"""

s4="""
    CREATE VIEW top5award_winners AS
    SELECT 
        Actors.id,
        Actors.name,
        COUNT(Awards.id) AS total_awards
    FROM Actors
    INNER JOIN  ActorsAwards ON Actors.id = ActorsAwards.actor_id
    INNER JOIN Awards ON ActorsAwards.award_id = Awards.id
    GROUP BY Actors.id, Actors.name
    ORDER BY total_awards DESC
    LIMIT 5;

    SELECT * FROM top5award_winners
"""

cur.execute(s2)
x = cur.fetchall()
print(x)

#Imported from procedures file
# actorsSortedByAwardsWon(2)
# findActorsBasedOnDurationAndGenre(117,8)