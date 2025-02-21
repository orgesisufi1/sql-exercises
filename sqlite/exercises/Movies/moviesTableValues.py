import sqlite3 as sq
from utility import insertValues


movies_data = [
    (1, 'The Silent Forest', 135, '2019-10-04', 3),
    (2, 'Beyond the Horizon', 145, '2021-05-21', 1),
    (3, 'Laughing Out Loud', 98, '2022-03-15', 2),
    (4, 'Shadows in the Dark', 112, '2020-07-11', 4),
    (5, 'Future World', 121, '2023-04-25', 5),
    (6, 'Endless Love', 109, '2021-02-14', 6),
    (7, 'The Last Kingdom', 130, '2018-11-28', 10),
    (8, 'Animated Wonders', 95, '2022-09-18', 7),
    (9, 'Wild at Heart', 115, '2020-06-10', 8),
    (10, 'The Documentary', 105, '2021-12-02', 9)
]


actors_data = [
    (1, 'James Roberts', '1986-04-12', 'Male'),
    (2, 'Emily Carter', '1990-07-24', 'Female'),
    (3, 'Michael Dawson', '1978-11-22', 'Male'),
    (4, 'Sophia Lee', '1992-03-08', 'Female'),
    (5, 'Chris Parker', '1984-09-16', 'Male'),
    (6, 'Olivia Brown', '1989-05-10', 'Female'),
    (7, 'Liam Smith', '1995-02-17', 'Male'),
    (8, 'Emma Wilson', '1993-12-03', 'Female'),
    (9, 'Daniel Hughes', '1987-01-25', 'Male'),
    (10, 'Grace Thompson', '1991-10-13', 'Female')
]



awards_data = [
    (1, 'Best Actor in a Leading Role', '2021-12-10', 'Acting'),
    (2, 'Best Picture', '2022-11-15', 'Film'),
    (3, 'Best Director', '2022-03-01', 'Directing'),
    (4, 'Best Screenplay', '2021-06-05', 'Writing'),
    (5, 'Best Cinematography', '2023-01-20', 'Cinematography'),
    (6, 'Best Original Score', '2022-12-05', 'Music'),
    (7, 'Best Actress in a Leading Role', '2022-08-25', 'Acting'),
    (8, 'Best Visual Effects', '2023-02-10', 'Visual Effects'),
    (9, 'Best Animated Feature', '2020-10-12', 'Animation'),
    (10, 'Best Supporting Actor', '2022-05-18', 'Supporting Role')
]



genres_data = [
    (1, 'Action'),
    (2, 'Comedy'),
    (3, 'Drama'),
    (4, 'Horror'),
    (5, 'Science Fiction'),
    (6, 'Romance'),
    (7, 'Animation'),
    (8, 'Thriller'),
    (9, 'Documentary'),
    (10, 'Fantasy')
]



actor_award_data = [
    (1, 1, 1, 2021),
    (2, 2, 7, 2022),
    (3, 3, 10, 2022),
    (4, 4, 1, 2021),
    (5, 5, 5, 2023),
    (6, 6, 6, 2022),
    (7, 7, 3, 2022),
    (8, 8, 7, 2023),
    (9, 9, 4, 2020),
    (10, 10, 2, 2022)
]


movies_award_data = [
    (1, 1, 2, 2020),
    (2, 2, 3, 2021),
    (3, 3, 4, 2022),
    (4, 4, 5, 2021),
    (5, 5, 6, 2023),
    (6, 6, 7, 2021),
    (7, 7, 8, 2022),
    (8, 8, 9, 2020),
    (9, 9, 10, 2021),
    (10, 10, 1, 2022)
]

movie_actors_data = [
    (1, 1, 1),
    (2, 1, 2),
    (3, 2, 3),
    (4, 3, 4),
    (5, 4, 5),
    (6, 5, 6),
    (7, 6, 7),
    (8, 7, 8),
    (9, 8, 8),
    (10, 9, 10)
]


# insertValues(
#     r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/Movies/movies.db', 
#     'Genres', 
#     genres_data
# )

# insertValues(
#     r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/Movies/movies.db', 
#     'Movies', 
#     movies_data    
# )

# insertValues(
#     r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/Movies/movies.db', 
#     'Actors', 
#     actors_data
# )

# insertValues(
#     r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/Movies/movies.db', 
#     'Awards', 
#     awards_data
# )

# insertValues(
#     r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/Movies/movies.db', 
#     'MovieActors', 
#     movie_actors_data
# )

# insertValues(
#     r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/Movies/movies.db', 
#     'ActorAwards', 
#     actor_award_data
# )

# insertValues(
#     r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/Movies/movies.db', 
#     'MoviesAward', 
#     movies_award_data
# )



