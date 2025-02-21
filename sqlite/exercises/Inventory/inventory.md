## 1. How to set up the database.

After importing the necessary libraries and modules, particularly the `createTable()` function, which takes three parameters: `database_path`, `table_name`, and `columns`, we can proceed to call the function. When doing so, we specify the database path (indicating either a specific folder to create it in or an existing database), the table name (keeping in mind that a single database can contain multiple tables, so we may need to call the function multiple times with different parameters), and finally, `columns`, where we define each column’s name, data type, and any constraints.After importing the necessary libraries and modules, particularly the `createTable()` function, which takes three parameters: `database_path`, `table_name`, and `columns`, we can proceed to call the function. When doing so, we specify the database path (indicating either a specific folder to create it in or an existing database), the table name (keeping in mind that a single database can contain multiple tables, so we may need to call the function multiple times with different parameters), and finally, `columns`, where we define each column’s name, data type, and any constraints.

## 2. Inserting Values.

To insert values into the table, we need to call the `insertValues()` function from the utility module, which also takes three parameters: `database_path`, `table_name`, and `data`. If all information is correct and usable, the function iterates through data and sends all the information to the database with the help of `cursor.execute()`

## 3. Running the queries.

Some queries can be run with basic sqlite syntax, so it can all be found in the `inventorySolutions.py` where each query is stored in a variable and can be ran through by using `cur.execute(variable_name)`, and then `cur.fetchall()` is used to fetch all the data received by the database, stored in a variable `x`, after that we print `x` and all the information is printed in the terminal.

## 4. Procedures.

Even though `CREATE PROCEDURE` is not supported by SQLite, you can run the assigned queries from functions through `inventoryProcedures.py`. In this file you can find 4 functions, each one with a procedure logic behind it. In the `inventorySolutions.py`, you can find all the 4 functions commented with the function description on top of them