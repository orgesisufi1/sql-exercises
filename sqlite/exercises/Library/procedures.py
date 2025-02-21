import sqlite3 as sq
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'library.db')

database_path = filename


con = sq.connect(database_path)
cur = con.cursor()

def getLogs(member_id):
    query = f"SELECT * FROM BookLogs WHERE BookLogs.member_id = {member_id}"
    cur.execute(query)
    x = cur.fetchall()
    con.commit()
    print(x)

#Create procedure that implements a logic when a user returns a book
def bookLend(user_id, book_id):
    #members validation if a member_id does not exist
    members = f"SELECT id FROM Members"
    cur.execute(members)
    members_list =cur.fetchall()
    members_arr = []
    n=0
    for i in members_list:
        members_arr.append(members_list[n][0])
        n+=1
    if user_id not in members_arr:
        print("User does not exist")
    if user_id in members_arr:
        query = f"SELECT book_id, log_type FROM BookLogs WHERE book_id = {book_id}"
        cur.execute(query)
        book_info = cur.fetchone()
        if book_info is None:
            print("Book does not exist!")
        if book_info[1] == 'lend':
            print("Book is not available at this time")
        if book_info[1] == 'return':
            print(f"Book is available and lend by User with ID: {user_id}")
            cur.execute(f"UPDATE BookLogs SET log_type = 'lend', member_id = {user_id} WHERE book_id = {book_id}")
            con.commit()

#Implement a logic when user wants to return a book
def bookReturn(book_id):
    query = f"SELECT book_id, log_type FROM BookLogs WHERE book_id = {book_id}"
    cur.execute(query)
    book_info = cur.fetchone()
    if book_info is None:
        print("Book does not exist!")
    if book_info[1] == 'return':
        print("The book is already returned")
    if book_info[1] == 'lend':
        print(f"Book is returned")
        cur.execute(f"UPDATE BookLogs SET log_type = 'return' WHERE book_id = {book_id}")
        con.commit()