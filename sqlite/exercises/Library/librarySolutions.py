import sqlite3 as sq
from procedures import getLogs, bookLend, bookReturn
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'library.db')

database_path = filename


con = sq.connect(database_path)
cur = con.cursor()

#Books published before 2010
s1 = """SELECT title FROM Books WHERE year_publisher < 2010"""

#Books published before 2000 and quantity is less or equal than 5
s2 = "SELECT title FROM Books WHERE year_publisher < 2000 AND quantity<=5"

#Join the books with genres and sort them by quantity
s3 = "SELECT Books.title, Books.quantity, Genres.genre_name FROM Books LEFT JOIN Genres ON  Books.genre_id = Genres.idORDER BY quantity ASC "

#Create a Select query that will join the the members that have borrowed a book, and will join the books with genres and authors (Decide which columns to show)
s5="""
    SELECT Members.id, Members.full_name as member_name, Members.age, Books.title AS book_title, Authors.full_name AS author_name,  Genres.genre_name 
    FROM Members 
    INNER JOIN Books ON Members.book_id = Books.id 
    INNER JOIN Authors ON Books.author_id = Authors.id 
    INNER JOIN Genres ON Books.genre_id = Genres.id WHERE Members.has_a_book_lend = 1;"""

#Change emails to 'example@kinandcarta.com' where there is 'gmaßil.com' in the emaik
s6="""
    UPDATE Members 
    SET email  = "example@kinandcarta.com" 
    WHERE email LIKE "%gmail.com"
"""

#Create a delete query that will delete the aithors that are not associated with a book
s7 = """
    DELETE FROM Authors
    WHERE author_id NOT IN(SELECT author_id FROM Books)
"""

#Display all the members who have lent a book but havent paid
s8="""
    SELECT full_name FROM Members
    WHERE Members.has_a_book_lend = 1 AND Members.has_paid = 0
"""

#Display all the adults who lent a book that is from the genre Adult or Action but are under 18
s9 = """
    SELECT full_name 
    FROM Members
    INNER JOIN Books ON Members.book_id = Books.id
    INNER JOIN Genres ON Books.genre_id = Genres.id
    WHERE Members.age < 18 AND (Genres.genre_name ="Action" OR Genres.genre_name = "Adult")
"""
#Display all logs from specific Member
# getLogs(1)

#Create procedure that implements a logic when a user returns a book - 
# bookLend has 2 parameters: bookLend(user_id, book_id) 
# Parameters are used to validate the data
# bookLend(6,7)

#Create procedure that implements a logic when a user returns a book
#bookReturn has 1 parameters: bookReturn( book_id) 
#Parameter is used to validate the data
# bookReturn(7)

cur.execute(s2)
x = print(cur.fetchall())
print(x)