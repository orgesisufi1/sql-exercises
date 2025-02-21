import sqlite3 as sq
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'library.db')

database_path = filename


con = sq.connect(database_path)
cur = con.cursor()


cur.execute("PRAGMA foreign_keys = ON")

authors = [ (1, 'Jane Austen', '1775-12-16', 'United Kingdom'),
    (2, 'Mark Twain', '1835-11-30', 'United States'),
    (3, 'Leo Tolstoy', '1828-09-09', 'Russia'),
    (4, 'Charles Dickens', '1812-02-07', 'United Kingdom'),
    (5, 'Fyodor Dostoevsky', '1821-11-11', 'Russia'),
    (6, 'George Orwell', '1903-06-25', 'United Kingdom'),
    (7, 'Virginia Woolf', '1882-01-25', 'United Kingdom'),
    (8, 'Ernest Hemingway', '1899-07-21', 'United States'),
    (9, 'Gabriel García Márquez', '1927-03-06', 'Colombia'),
    (10, 'J.K. Rowling', '1965-07-31', 'United Kingdom') ]

genres = [
    (1, 'Fiction'), (2, 'Mystery'), (3, 'Fantasy'), (4, 'Science Fiction'),
    (5, 'Romance'), (6, 'Horror'), (7, 'Historical'), (8, 'Thriller'),
    (9, 'Adventure'), (10, 'Non-Fiction')
]

books = [
    (1, 'Pride and Prejudice', 1813, 5, 1, 5),
    (2, 'Adventures of Huckleberry Finn', 1884, 3, 2, 9),
    (3, 'War and Peace', 1869, 4, 3, 7),
    (4, 'A Tale of Two Cities', 1859, 6, 4, 7),
    (5, 'Crime and Punishment', 1866, 2, 5, 2),
    (6, '1984', 1949, 8, 6, 4),
    (7, 'To the Lighthouse', 1927, 5, 7, 1),
    (8, 'The Old Man and the Sea', 1952, 4, 8, 1),
    (9, 'One Hundred Years of Solitude', 1967, 7, 9, 1),
    (10, 'Harry Potter and the Sorcerer''s Stone', 1997, 10, 10, 3)
]

members_data = [
    (1, 'Alice Johnson', 'New York', '123 Maple St', 'alice@gmail.com', 34, '555-1234', 1, 1, 1),
    (2, 'Bob Smith', 'Los Angeles', '456 Oak St', 'bob@gmail.com', 42, '555-5678', 1, 0, None),
    (3, 'Charlie Brown', 'Chicago', '789 Pine St', 'charlie@gmail.com', 29, '555-8765', 0, 1, 3),
    (4, 'Diane Green', 'Miami', '321 Cedar St', 'diane@gmail.com', 22, '555-4321', 1, 1, 2),
    (5, 'Eve White', 'Boston', '654 Spruce St', 'eve@gmail.com', 45, '555-9988', 1, 0, None),
    (6, 'Frank Black', 'Houston', '123 Birch St', 'frank@gmail.com', 36, '555-3344', 1, 1, 4),
    (7, 'Grace Silver', 'Seattle', '789 Willow St', 'grace@gmail.com', 31, '555-6677', 0, 0, None),
    (8, 'Henry Gold', 'Denver', '246 Elm St', 'henry@gmail.com', 40, '555-2211', 1, 1, 5),
    (9, 'Ivy Blue', 'Phoenix', '357 Aspen St', 'ivy@gmail.com', 28, '555-7788', 1, 0, None),
    (10, 'Jack White', 'Philadelphia', '135 Hickory St', 'jack@gmail.com', 50, '555-9900', 1, 1, 6)
]

book_logs= [
    (1, 1, 1, 'lend'),
    (2, 3, 3, 'lend'),
    (3, 2, 4, 'lend'),
    (4, 4, 6, 'lend'),
    (5, 5, 8, 'lend'),
    (6, 6, 10, 'lend'),
    (7, 3, 3, 'return'),
    (8, 1, 1, 'return'),
    (9, 2, 4, 'return'),
    (10, 4, 6, 'return')
]

# cur.executemany("INSERT INTO Authors VALUES (?,?,?,?)", authors)
# cur.executemany("INSERT INTO Genres VALUES (?,?)", genres)
# cur.executemany("INSERT INTO Authors VALUES (?,?,?,?,?,?)", books)
# cur.executemany("INSERT INTO Authors VALUES (?,?,?,?)", members_data)
# cur.executemany("INSERT INTO Authors VALUES (?,?,?,?,?,?,?,?,?,?)", book_logs)


#Inserting values through the function
def insertValues(table_name,data):

    cur.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cur.fetchall()]
    column_names = ', '.join(columns)

    values = ''
    for i in data[1]:
        values += '?,'
    values = values[:-1]

    qurery = f"INSERT OR IGNORE INTO {table_name} ({column_names}) VALUES ({values})"

    for row in data:
        cur.execute(qurery, row)

    con.commit()



#Calling the functions for each table to insert the data
# insertValues('Authors', authors)
# insertValues('Genres', genres)
# insertValues('Books', books)
# insertValues('Members', members_data)
# insertValues('BookLogs', book_logs)
