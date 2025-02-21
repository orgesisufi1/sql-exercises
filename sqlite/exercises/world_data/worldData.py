import sqlite3 as sq
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'world_data.db')

database_path = filename


con = sq.connect(database_path)
cur = con.cursor()
table = """
CREATE TABLE IF NOT EXISTS world_data(
    id INTEGER PRIMARY KEY,
    Rank INTEGER,
    CCA3 TEXT,
    CountryTerritory INTEGER,
    Capital TEXT,
    Continent TEXT,
    "2022Population" INTEGER,
    "2020Population" INTEGER,
    "2015Population" INTEGER,
    "2010Population" INTEGER,
    "2000Population" INTEGER,
    "1990Population" INTEGER,
    "1980Population" INTEGER,
    "1970Population" INTEGER,
    Area INTEGER,
    Density REAL,
    GrowthRate REAL,
    WorldPopulationPercentage REAL)
"""

cur.execute(table)

con.commit()
con.close()
