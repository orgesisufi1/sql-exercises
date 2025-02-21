import sqlite3 as sq
import csv
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'world_data.db')
csv_file = os.path.join(dirname, 'world_data.csv')
database_path = filename


con = sq.connect(database_path)
cur = con.cursor()

#remove comments to upload data from .csv to .db file 
with open(csv_file, 'r') as data:
    data_content = csv.reader(data)
    header = next(data_content, None)

    records = """
    INSERT INTO world_data (
        id, Rank, CCA3, CountryTerritory, Capital, Continent, 
        "2022Population", "2020Population", "2015Population", "2010Population", 
        "2000Population", "1990Population", "1980Population", "1970Population", 
        Area, Density, GrowthRate, WorldPopulationPercentage
    ) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    cur.executemany(records, data_content)

con.commit()


con.close()


