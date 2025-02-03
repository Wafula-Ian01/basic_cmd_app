import sqlite3
import prompt
import csv

class Employee:
    def __init__(self, id,name, age, department, salary):
        self.id = id  # unique id for each employee
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        
    #database initiation and connectivity
    @staticmethod
    def initDB():
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS employee
                   (
                       id INTEGER PRIMARY KEY, 
                       name TEXT NOT NULL, 
                       age INTEGER NOT NULL, 
                       department TEXT NOT NULL, 
                       salary REAL NOT NULL)''')
        conn.commit()
        conn.close()
        
    #CRUD operations
    @staticmethod
    def addEmployee():
        name = input("Enter Employee Name: ").strip()
        if not name:
            print("Name cannot be empty. Enter correct value to proceed!")
            return name
        try:
            age= int(input("Enter Employee Age: "))
            if age <=0:
                raise ValueError("The age can only be a positive integer")
        except ValueError as e:
            print("Invalid age: {e}!")
            return age
        department= input("Enter Employee Department: ").strip()
        if not department:
            print("Department cannot be empty!")
            return department
        
        try:
            salary= float(input("Enter Employee Salary: "))
            if salary<=0:
                raise ValueError("Salary must be a positive number")
        except ValueError as e:
            print("Salary must be a positive value: {e}!")
            return salary
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        #checking for duplicate value
        c.execute("SELECT * FROM employee WHERE name=?", (name,))
        if c.fetchone():
            print("Employee with this name already exists!")
            conn.close()
            return
        
        c.execute("INSERT INTO employee (name, age, department, salary) VALUES (?, ?, ?, ?)", 
                  (name, age, department, salary))
        conn.commit()
        conn.close()
        print("Employee added successfully!")
        
    #return all employees in the database   
    def viewEmployees():
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM employee")
        row = c.fetchall()
        if row:
            print("Employee Details:")
            for row in row:
                print("ID:", row[0])
                print("Name:", row[1])
                print("Age:", row[2])
                print("Department:", row[3])
                print("Salary:", row[4])
                print("-------------------------")
        else:
            print("Employees not found!")
    
    @staticmethod
    def updateEmployee(id):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM employee WHERE id=?", (id,))
        row = c.fetchone()
        if not row: 
        # Check if employee doesn't exists
            print("Employee ID not found!")
            conn.close()
            return
        name = input("Enter Employee Name (Leave blank to keep old value): ").strip() or row[1]
        age = input("Enter Employee Age (Leave blank to keep old value): ")
        department = input("Enter Employee Department (Leave blank to keep old value): ").strip() or row[3]
        salary = input("Enter Employee Salary (Leave blank to keep old value): ")
        
        try:
            age=int(age) if age else row[2]
            salary=float(salary) if salary else row[4]
        except ValueError:
            print("Invalid age or salary! Values must be numeric!")
            conn.close()
            return
        c.execute("UPDATE employee SET name=?, age=?, department=?, salary=? WHERE id=?", (name, age, department, salary, id))
        conn.commit()
        conn.close()
        print("Employee updated successfully!")
    
    @staticmethod
    def deleteEmployee(id):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM employee WHERE id=?", (id,))
        if not c.fetchone():
            print("Employee ID not found!")
            conn.close()
            return
        c.execute("DELETE FROM employee WHERE id=?", (id,))
        conn.commit()
        conn.close()
        print("Employee deleted successfully!")
            
    def searchEmployee():
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        search_name = input("Enter Employee Name to Search: ")
        c.execute("SELECT * FROM employee WHERE name=?", (search_name,))
        row = c.fetchone()
        if row:
            print("Employee Details:")
            print("ID:", row[0])
            print("Name:", row[1])
            print("Age:", row[2])
            print("Department:", row[3])
            print("Salary:", row[4])
        else:
            print("Employee not found!")
            
    def searchDepartment():
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        search_department = input("Enter Department to Search: ")
        c.execute("SELECT * FROM employee WHERE department=?", (search_department,))
        row = c.fetchall()
        if row:
            print("Employees in the", search_department, "department:")
            for row in row:
                print("ID:", row[0])
                print("Name:", row[1])
                print("Age:", row[2])
                print("Department:", row[3])
                print("Salary:", row[4])
                print("-------------------------")
        else:
            print("No employees found in the", search_department, "department!")
            
    def exportData():
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM employee")
        employees = c.fetchall()
        
        if employees:
            csv_file = "employees.csv"
            with open(csv_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Age", "Department", "Salary"])
                writer.writerows(employees)
            
            print(f"Employee data successfully exported to {csv_file}!")
        else:
            print("No employee records found.")

        conn.close()
        
    def importData():
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        
        try:
            with open("newEmployees.csv", mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    if len(row) == 4:  # Ensure correct number of columns
                        name, age, department, salary = row
                        c.execute("INSERT INTO employee (name, age, department, salary) VALUES (?, ?, ?, ?)", 
                                (name, age, department, salary))
                    else:
                        print(f"Skipping invalid row: {row}")

            conn.commit()
            print("Employees imported successfully!")

        except FileNotFoundError:
            print("Error: 'newEmployees.csv' file not found!")

        conn.close()
        
    def salaryFilter():
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        upper_limit = float(input("Enter Upper limit: "))
        lower_limit = float(input("Enter Lower limit: "))
        c.execute("SELECT * FROM employee WHERE salary<=? AND salary>=?", (upper_limit,lower_limit))
        row = c.fetchall()
        if row:
            print("Employees earning in the ", lower_limit,"-", upper_limit, " limits:")
            for row in row:
                print("ID:", row[0])
                print("Name:", row[1])
                print("Age:", row[2])
                print("Department:", row[3])
                print("Salary:", row[4])
                print("-------------------------")
        else:
            print("No employees found earning in the ", lower_limit,"-", upper_limit, " limits:")