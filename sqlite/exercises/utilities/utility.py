import sqlite3 as sq 
import csv

def createTable(db_name,table_name, *columns):

    con = sq.connect(db_name)
    cur = con.cursor()
    column_dot = ", ".join(columns)
    table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_dot});"

    try:
        cur.execute(table_query)
        con.commit()
        print(f"Table '{table_name} created succesfully'")
    except sq.Error as e:
        print(e)
    finally:
        con.close()


def insertValues(db_name,table_name,data):

    con = sq.connect(db_name)
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    
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


def storeValuesCSV(csv_data, variable):
    with open(csv_data, 'r') as csv_file:
        data = csv.reader(csv_file)
        next(csv_file)
        for row in data:
            variable.append(row)