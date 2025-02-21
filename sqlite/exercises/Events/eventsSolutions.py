import sqlite3 as sq
from eventsProcedures import *
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'events.db')
print(filename)

database_path = filename
con = sq.connect(database_path)
cur = con.cursor()


#Create a query that will display important information about each event and its details.
s1 = """
    SELECT 
    Events.event_id,
    Events.name AS event_name,
    Events.description,
    Venues.name AS venue_name ,
    Events.date
    FROM Events
    INNER JOIN Venues ON Events.event_id = Venues.id
"""

#Create a query that will display information about attendees and the events they are registered for.
s2 = """
    SELECT
    Attendees.id AS attendee_id,
    Attendees.name AS attendee_name,
    Attendees.email AS attendee_email,
    Events.name AS event_name
    FROM Attendees
    INNER JOIN event_attendees ON Attendees.id = event_attendees.attendee_id
    INNER JOIN Events ON event_attendees.event_id = Events.event_id
"""

#Create a query that will display information about performers and the events they are performing at.
s3 = """
    SELECT
    Performers.id,
    Performers.name AS performer_name,
    Events.name AS event_name,
    Venues.name AS venue_name,
    Venues.address AS venue_address
    FROM Performers
    INNER JOIN event_performers ON Performers.id = event_performers.performer_id
    INNER JOIN Events ON event_performers.event_id = Events.event_id
    INNER JOIN Venues ON Events.venue_id = Venues.id
"""

#Create a query that will group events by venue and display the total number of events and average attendees per event.
s4 = """
    SELECT
    Venues.id,
    Venues.name AS venue_name,
    COUNT(DISTINCT Events.event_id) AS event_count,
    COUNT(event_attendees.attendee_id) AS total_attendees,
    CAST(COUNT(event_attendees.attendee_id) AS FLOAT) / NULLIF(COUNT(DISTINCT Events.event_id), 0) AS avg_attendees_per_event
    FROM Venues
    INNER JOIN Events ON Venues.id = Events.venue_id
    LEFT JOIN event_attendees ON Events.event_id = event_attendees.event_id
    GROUP BY Venues.id, Venues.name;
"""

# Create a view that will display the top 5 events with the highest number of attendees.
s5 = """
    CREATE VIEW top_5_events_highest_attendance AS
    SELECT
    Events.event_id,
    Events.name AS event_name,
    COUNT(event_attendees.attendee_id) AS attendance
    FROM Events
    INNER JOIN event_attendees ON Events.event_id = event_attendees.event_id
    GROUP BY Events.event_id, Events.name
    ORDER BY attendance DESC;
"""

cur.execute(s5)

fetch_data = cur.fetchall()
print(fetch_data)

#Create a procedure that will take a date range as a parameter and show all events within that range along with their details.
# getEventByDateRange('2024-11-19', '2024-11-26')

#Create a procedure that will take a venue ID as a parameter and show all events at that venue along with their details.
# eventsOnVenue(1)