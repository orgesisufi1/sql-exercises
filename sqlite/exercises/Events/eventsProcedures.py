import sqlite3 as sq
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'events.db')
print(filename)

database_path = filename

con = sq.connect(database_path)
cur = con.cursor()

def getEventByDateRange(start_date, end_date):
    cur.execute(f"""
        SELECT 
        Events.event_id,
        Events.name,
        Venues.name,
        Events.date
        FROM Events
        INNER JOIN Venues ON Events.venue_id = Venues.id
        WHERE Events.date BETWEEN '{start_date}' AND '{end_date}'
        """
)
    
    x = cur.fetchall()
    print(x)

def eventsOnVenue(venue_id):
    cur.execute(f"""
        SELECT
        Events.event_id AS event_id,
        Events.name AS event_name,
        Venues.name AS venue_name
        FROM Events
        INNER JOIN Venues ON Events.venue_id = Venues.id
        WHERE Events.venue_id = {venue_id}
        """
)
    x = cur.fetchall()
    print(x)
