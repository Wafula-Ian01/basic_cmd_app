import time
import manager

#runs a commandline that interfaces with the system
def cmd():
    while True:
        print('''
              Welcome to Employee Management Bureau\n
              Choose one of the numbers below to use the system\n
              \t1. Add Employee\n
              \t2. Delete Employee\n
              \t3. Update Employee\n
              \t4. View All Employees\n
              \t5. Search for Employees\n
              \t6. Exit\n
              ''')
        command = input("Enter a command: ")
        if command == "6":
            print("System Exiting...")
            time.sleep(3)
            break
        else:
            if command== "1":
                while True:
                    print(""" Add new Employee\n
                        \t1. Make single entry\n
                        \t2. Make batch entry\n
                        \t3. Back to main menu\n""")
                    subcommand = input("Enter a subcommand: ")
                    if subcommand == "3":
                        print("Returning to main menu...")
                        time.sleep(1)
                        break
                    else:
                        if subcommand == "1":
                            manager.Employee.addEmployee()
                        elif subcommand == "2":
                            manager.Employee.importData() 
            elif command== "2":
                id = int(input("Enter Employee ID of User you want to delete: "))
                manager.Employee.deleteEmployee(id)
            elif command== "3":
                id = int(input("Enter Employee ID of User you want to update: "))
                manager.Employee.updateEmployee(id)
            elif command== "4" :
                while True:
                    print(""" View all Users or Export\n
                        \t1. View Only\n
                        \t2. Extract users to csv file\n
                        \t3. Back to main menu\n""")
                    subcommand = input("Enter a subcommand: ")
                    if subcommand == "3":
                        print("Returning to main menu...")
                        time.sleep(1)
                        break
                    else:
                        if subcommand == "1":
                            manager.Employee.viewEmployees()
                        elif subcommand == "2":
                            manager.Employee.exportData() 
            elif command== "5":
                while True:
                    print(""" Choose search criterion\n
                        \t1. Search by Employee name\n
                        \t2. Search by Department\n
                        \t3. Filter by Salary range\n
                        \t4. Back to main menu\n""")
                    subcommand = input("Enter a subcommand: ")
                    if subcommand == "4":
                        print("Returning to main menu...")
                        time.sleep(1)
                        break
                    else:
                        if subcommand == "1":
                            manager.Employee.searchEmployee()
                        elif subcommand == "2":
                            manager.Employee.searchDepartment()  # Search for employees by department. You can add more search options here.
                        elif subcommand == "3":
                            manager.Employee.salaryFilter()  # Filter employees by salary range. You can add more filters here.
            else:
                print("Invalid Command! \nPlease choose an option on the menu thanks")
            