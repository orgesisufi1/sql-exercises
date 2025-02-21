import sqlite3 as sq
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'employee.db')


database_path = filename
con = sq.connect(database_path)
cur = con.cursor()



s1 = """
    SELECT Employee.id, 
    Employee.name, 
    Address.street_name, 
    Address.city, 
    Address.country,
    Department.department_name
    FROM Employee
    INNER JOIN Address ON Employee.address_id = Address.id
    INNER JOIN Department ON Employee.department_id = Department.id
"""

s2 = """
    SELECT 
    Employee.department_id,
    Department.department_name,
    AVG(Employee.salary) AS average_salary
    FROM Employee
    INNER JOIN Department ON Employee.department_id = Department.id
    GROUP BY Employee.department_id, Department.department_name;
"""

s3 = """
    SELECT 
    Leaves.employee_id,
    SUM(JULIANDAY(end_date) - JULIANDAY(start_date)) AS total_off_days
    FROM Leaves
    GROUP BY Leaves.employee_id
"""

s4 = """
    SELECT 
    Employee.name,
    Employee.surname,
    Project.project_name,
    MIN(Employee.salary) AS minimum_salary
    FROM Employee
    INNER JOIN Onboarding ON Employee.id = Onboarding.employee_id
    INNER JOIN Project ON Onboarding.project_id = Project.id
    GROUP BY Employee.name, Employee.surname, Project.project_name
    ORDER BY minimum_salary ASC;
"""

s5 = """
    SELECT 
    Department.department_name,
    SUM(Employee.salary)
    FROM Employee
    INNER JOIN Department ON Employee.department_id = Department.id
    GROUP BY Department.department_name
"""

s6 = """
    UPDATE Leaves
    SET approval_status = "Approved"
    WHERE Leaves.employee_id IN(
    SELECT employee_id
    FROM Leaves
    GROUP BY Leaves.employee_id
    HAVING SUM(JULIANDAY(end_date) - JULIANDAY(start_date)) > 10
    )
    AND JULIANDAY(start_date) > JULIANDAY('now');
"""

s7 = """
    UPDATE Onboarding
    SET start_date = DATE(start_date, '+5 day')
    WHERE JULIANDAY(start_date) > JULIANDAY('now', '+30 day');
"""

s8 = """
    DELETE FROM Employee 
    WHERE Employee.id NOT IN (
    SELECT employee_id FROM Onboarding
    )
"""

s9 = """
CREATE TRIGGER 
omboarding_start_date_to_leave_end_date 
AFTER 
INSERT ON Leaves 
FOR EACH ROW BEGIN 
UPDATE Onboarding 
SET start_date = NEW.end_date 
WHERE employee_id = NEW.employee_id AND start_date BETWEEN NEW.start_date AND NEW.end_date; 
END
"""

cur.execute(s4)
x = cur.fetchall()
print(x)