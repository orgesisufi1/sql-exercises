import sqlite3 as sq
from utility import *
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'inventory.db')


database_path = filename
con = sq.connect(database_path)
cur = con.cursor()
# createTable(
#     database_path,
#     'Products',
#     '''id INTEGER PRIMARY KEY, 
#     name TEXT NOT NULL,
#     description TEXT,
#     price REAL NOT NULL CHECK (price >= 0),
#     stock INTEGER DEFAULT 0 CHECK (stock >= 0),
#     category_id INTEGER NOT NULL,
#     supplier_id INTEGER NOT NULL,
#     supplier_price REAL CHECK (supplier_price >= 0),
#     FOREIGN KEY (category_id) REFERENCES Category(id) ON DELETE SET NULL ON UPDATE CASCADE,
#     FOREIGN KEY (supplier_id) REFERENCES Suppliers(id) ON DELETE SET NULL ON UPDATE CASCADE,
#     UNIQUE (name, supplier_id)'''
# )

# createTable(
#     database_path,
#     'Category',
#     '''id INTEGER PRIMARY KEY, name TEXT NOT NULL'''
# )

# createTable(
#     database_path,
#     'Suppliers',
#     '''
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     no_product INTEGER NOT NULL,
#     email TEXT NOT NULL
#     '''
# )

# createTable(
#     database_path,
#     'Orders',
#     '''
#     id INTEGER PRIMARY KEY,
#     costumer_id INTEGER NOT NULL,
#     order_date DATE NOT NULL,
#     total_order_value REAL CHECK (total_order_value >= 0),
#     FOREIGN KEY (costumer_id) REFERENCES Costumers(id) ON DELETE SET NULL ON UPDATE CASCADE
#     '''
# )

# createTable(
#     database_path,
#     'Order_details',
#     '''
#     id INTEGER PRIMARY KEY,
#     order_id INTEGER NOT NULL,
#     product_id INTEGER NOT NULL,
#     quantity INTEGER NOT NULL CHECK (quantity > 0),
#     FOREIGN KEY (order_id) REFERENCES Orders(id) ON DELETE CASCADE ON UPDATE CASCADE,
#     FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE ON UPDATE CASCADE
#     '''
# )

# createTable(
#     database_path,
#     'Transactions',
#     '''
#     id INTEGER PRIMARY KEY,
#     product_id INTEGER NOT NULL,
#     additions INTEGER CHECK (additions >= 0), -- Must be non-negative
#     removals INTEGER CHECK (removals >= 0), -- Must be non-negative
#     adjustments INTEGER CHECK (adjustments >= 0), -- Must be non-negative
#     date DATE NOT NULL,
#     FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE ON UPDATE CASCADE
#     '''
# )

# createTable(
#     database_path,
#     'Costumers',
#     '''
#     id INTEGER PRIMARY KEY,
#     full_name TEXT NOT NULL,
#     address TEXT
#     '''
# )
