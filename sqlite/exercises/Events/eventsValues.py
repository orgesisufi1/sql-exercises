from utility import insertValues
from data_values import *
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'events.db')
print(filename)

database_path = filename

# insertValues(database_path, 'Venues', venues_data)
# insertValues(database_path, 'Attendees', attendees_data)
# insertValues(database_path, 'Performers', performers_data)
# insertValues(database_path, 'Events', events_data)
# insertValues(database_path, 'event_attendees', event_ateendes)
# insertValues(database_path, 'event_performers', event_performers)