import sqlite3 as sq
from utility import *
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'employee.db')


database_path = filename
con = sq.connect(database_path)
cur = con.cursor()

# createTable(database_path, 
#             'Employee', 
#             'id INTEGER PRIMARY KEY AUTOINCREMENT', 
#             'name TEXT NOT NULL', 
#             'surname TEXT NOT NULL', 
#             'salary REAL NOT NULL', 
#             'department_id INTEGER NOT NULL', 
#             'address_id INTEGER NOT NULL', 
#             'FOREIGN KEY (department_id) REFERENCES Department(id)', 
#             'FOREIGN KEY (address_id) REFERENCES Address(id)'
#             )

# createTable(database_path, 
#             'Address', 
#             'id INTEGER PRIMARY KEY AUTOINCREMENT', 
#             'street_name TEXT NOT NULL', 
#             'country TEXT NOT NULL', 
#             'city TEXT NOT NULL'
#             )

# createTable(database_path, 
#             'Department', 
#             'id INTEGER PRIMARY KEY AUTOINCREMENT', 
#             'department_name TEXT NOT NULL'
#             )

# createTable(database_path, 
#             'Project', 
#             'id INTEGER PRIMARY KEY AUTOINCREMENT', 
#             'project_name TEXT NOT NULL', 
#             'manager_id INTEGER NOT NULL', 
#             'FOREIGN KEY (manager_id) REFERENCES Employee(id)'
#             )


# createTable(database_path, 
#             'Onboarding',
#             'employee_id INTEGER NOT NULL', 
#             'project_id INTEGER NOT NULL', 
#             'start_date TEXT NOT NULL', 
#             'end_date TEXT NOT NULL',
#             'FOREIGN KEY (employee_id) REFERENCES Employee(id)'
#             'FOREIGN KEY (project_id) REFERENCES Project(id)',
#             'CHECK(end_date > start_date)'
#             )


# createTable(database_path, 
#             'Leaves',
#             'leave_id INTEGER NOT NULL', 
#             'employee_id INTEGER NOT NULL',
#             'leave_type TEXT NOT NULL', 
#             'start_date TEXT NOT NULL', 
#             'end_date TEXT NOT NULL',
#             'approval_status TEXT NOT NULL',
#             'approver_id INTEGER NOT NULL',
#             'FOREIGN KEY (approver_id) REFERENCES Employee(id)',
#             'PRIMARY KEY (leave_id, employee_id)',
#             'CHECK(end_date > start_date)'
#             )
