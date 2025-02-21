import sqlite3 as sq
from utility import insertValues
from data_values import *
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'inventory.db')


database_path = filename
con = sq.connect(database_path)
cur = con.cursor() 
#USING insertValues function
# insertValues(database_path, table_name, data)
# insertValues(database_path, 'Category', category_data)
# insertValues(database_path, 'Suppliers', suppliers_data)
# insertValues(database_path, 'Products', products_data)
# insertValues(database_path, 'Costumers', costumers_data)
# insertValues(database_path, 'Transactions', transactions_data)
# insertValues(database_path, 'Orders', orders_data)
# insertValues(database_path, 'Order_details', order_details_data)


