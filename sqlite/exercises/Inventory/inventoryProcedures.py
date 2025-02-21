import sqlite3 as sq
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'inventory.db')


database_path = filename
con = sq.connect(database_path)
cur = con.cursor()


def showNumbersOfProducts(product_category_id):
    cur.execute(f"""
    SELECT
    Suppliers.id AS supplier_id,
    Suppliers.name AS supplier_name,
    Category.name AS category_name,
    COUNT(Products.name) AS number_of_products
    FROM Products
    INNER JOIN Suppliers ON Products.supplier_id = Suppliers.id
    INNER JOIN Category ON Products.category_id = Category.id
    WHERE Products.category_id = {product_category_id}
    GROUP BY Suppliers.id, Suppliers.name, Category.name
    ORDER BY number_of_products DESC;
""")
    
    x = cur.fetchall()
    print(x)


def itemsOfOrderPlacedWithinDateRange(start_date, end_date):
    cur.execute(f"""
        SELECT
        Products.id,
        Products.name,
        Order_details.quantity,
        Products.price * Order_details.quantity AS total_value_of_product,
        Orders.order_date,
        Orders.id AS order_id
        FROM Products
        INNER JOIN Order_details ON Products.id = Order_details.product_id
        INNER JOIN Orders ON Order_details.order_id = Orders.id
        WHERE date(Orders.order_date) BETWEEN '{start_date}' AND  '{end_date}'
        """
)
    x = cur.fetchall()
    print(x)


def inventoryTransaction(product_id):
    cur.execute(f"""
        SELECT 
        Transactions.id AS transactions_id,
        Products.id AS product_id,
        Products.name AS product_name,
        Transactions.additions,
        Transactions.removals,
        Transactions.date
        FROM Products
        INNER JOIN Transactions ON Transactions.product_id = Products.id
        WHERE Products.id = {product_id}
        ORDER BY Transactions.date ASC
        """
)
    
    x = cur.fetchall()
    print(x)


def productGroupedBySupplierID(supplier_id):
    cur.execute(f"""
        SELECT
        Products.id AS product_id,
        Suppliers.id AS supplier_id,
        Suppliers.name AS supplier_name,
        Products.name AS product_name,
        Products.stock
        FROM Products
        INNER JOIN Suppliers ON Products.supplier_id = Suppliers.id
        WHERE Suppliers.id = {supplier_id}
        """
)
    x = cur.fetchall()
    print(x)


showNumbersOfProducts(1)
