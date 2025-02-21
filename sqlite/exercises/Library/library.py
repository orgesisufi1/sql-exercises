import sqlite3 as sq 
import os
from utility import *
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'library.db')

database_path = filename


con = sq.connect(database_path)
cur = con.cursor()


cur.execute("PRAGMA foreign_keys = ON;")

createTable(database_path, 'Test',
            'log_id INTEGER PRIMARY KEY AUTOINCREMENT', 
            'book_id INTEGER','member_id INTEGER', 
            'log_type TEXT CHECK(log_type IN ("lend", "return"))', 'FOREIGN KEY (book_id) REFERENCES Books(id) ON DELETE CASCADE', 
            'FOREIGN KEY (member_id) REFERENCES Members(id) ON DELETE CASCADE'
)
