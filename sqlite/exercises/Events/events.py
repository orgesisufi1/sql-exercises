from utility import createTable


import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'events.db')

database_path = filename

# createTable(database_path, 
#             'Events',
#             '''
#             event_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             date TEXT NOT NULL,
#             venue_id INTEGER NOT NULL,
#             description TEXT
#             '''
# )

# createTable(
#     database_path,
#     'Attendees',
#     '''
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL,
#     phone_number TEXT NOT NULL
# '''
# )

# createTable(
#     database_path,
#     'Performers',
#     '''
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL
# '''
# )

# createTable(
#     database_path,
#     'Venues',
#     '''
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     address TEXT NOT NULL,
#     capacity INTEGER NOT NULL CHECK (capacity >= 0)
# '''
# )

# createTable(
#     database_path,
#     'event_attendees',
#     '''
#     event_id INTEGER,
#     attendee_id INTEGER,
#     PRIMARY KEY (event_id, attendee_id),
#     FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE,
#     FOREIGN KEY (attendee_id) REFERENCES Attendees(id) ON DELETE CASCADE
# '''
# )

# createTable(
#     database_path,
#     'event_performers',
#     '''
#     event_id INTEGER,
#     performer_id INTEGER,
#     PRIMARY KEY (event_id, performer_id),
#     FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE,
#     FOREIGN KEY (performer_id) REFERENCES Performers(id) ON DELETE CASCADE
# '''
# )