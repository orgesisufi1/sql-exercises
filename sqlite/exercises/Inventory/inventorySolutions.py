import sqlite3 as sq
from inventoryProcedures import *
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'inventory.db')


database_path = filename
con = sq.connect(database_path)
cur = con.cursor()

s1 = """
    SELECT 
    Products.id, 
    Products.name, 
    Products.description, 
    Products.stock,
    Category.name AS category_name
    FROM Products
    INNER JOIN Category ON Products.category_id = Category.id
"""

s2 = """
    SELECT 
    Suppliers.id,
    Suppliers.name AS supplier_name,
    Products.name AS product_name
    FROM Products
    INNER JOIN Suppliers ON Products.supplier_id = Suppliers.id
"""

s3 = """
    SELECT DISTINCT
    Costumers.id,
    Costumers.full_name AS costumer_name,
    Products.name AS ordered_product
    FROM Orders
    INNER JOIN Costumers ON Orders.costumer_id = Costumers.id
    INNER JOIN Order_details ON Orders.id = Order_details.order_id
    INNER JOIN Products ON Order_details.product_id = Products.id
"""

s4 = """
    SELECT
    Costumers.id,
    Costumers.full_name AS costumer_name,
    SUM(Orders.total_order_value) AS total_spending
    FROM Orders
    INNER JOIN Costumers ON Orders.costumer_id = Costumers.id
    GROUP BY Costumers.full_name
"""

s5 = """
    SELECT
    Category.name AS category_name,
    AVG(Products.price) AS average_price,
    SUM(Products.stock) AS total_stock
    FROM Products
    INNER JOIN Category ON Products.category_id = Category.id
    GROUP BY Category.name;
"""

s6 = """
    CREATE VIEW top_5_stocked_products AS
    SELECT Products.id, Products.name, Products.stock
    FROM Products
    ORDER BY Products.stock DESC
    LIMIT 5
"""

s7 = """
    CREATE VIEW top_5_costumers_by_order_value AS
    SELECT Costumers.id, Costumers.full_name, Orders.total_order_value
    FROM Costumers
    INNER JOIN Orders ON Costumers.id = Orders.costumer_id
    ORDER BY Orders.total_order_value DESC
    LIMIT 5
"""

# Show the suppliers that supply items based on product category
# showNumbersOfProducts(1)

#Create a procedure that will take a date range as parameters and show the orders placed within that range, including details of the products ordered and the total order value.
# itemsOfOrderPlacedWithinDateRange('2024-11-01', '2024-11-03')

#Create a procedure that will take a product ID as a parameter and show the inventory transactions for that product, sorted by date.
# inventoryTransaction(1)

# Create a procedure that will take a supplier ID as a parameter and show all the products supplied by that supplier along with their current stock levels.
# productGroupedBySupplierID(1)

cur.execute(s3)

x = cur.fetchall()
print(x)