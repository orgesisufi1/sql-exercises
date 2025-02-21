import sqlite3 as sq
from utility import insertValues, storeValuesCSV
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'employee.db')


database_path = filename
con = sq.connect(database_path)
cur = con.cursor()


address_data = [ ]
department_data = [ ]
employee_data = [ ]
leaves_data = [ ]
onboarding_data = [ ]
project_data = [ ]
test_data = [ ]

#Function from utility to store all CSV Values in variables to make them ready for the insertValues() function
# storeValuesCSV(r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/EmployeeManagementSystem/CSV Files/Address.csv', address_data)
# storeValuesCSV(r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/EmployeeManagementSystem/CSV Files/Department.csv', department_data)
# storeValuesCSV(r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/EmployeeManagementSystem/CSV Files/Employee.csv', employee_data)
# storeValuesCSV(r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/EmployeeManagementSystem/CSV Files/Project.csv', project_data)
# storeValuesCSV(r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/EmployeeManagementSystem/CSV Files/Onboarding.csv', onboarding_data)
# storeValuesCSV(r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/EmployeeManagementSystem/CSV Files/Leaves.csv', leaves_data)
# storeValuesCSV(r'/Users/orgesisufi/Desktop/Data/see-data-internship-sql/solutions/OrgesIsufi/EmployeeManagementSystem/CSV Files/Test.csv', test_data)

# insertValues(database_path,  table_name ,      data)
# insertValues(database_path, 'Onboarding', onboarding_data)
