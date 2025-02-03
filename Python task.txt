### **Python & SQL Intermediate Task: Employee Management System**  

#### **Objective:**  
Build a simple **Employee Management System** using Python and SQLite. The system should allow users to **add, view, update, delete, and search** employee records in an SQLite database.  

---

### **Task Requirements:**  

1. **Database Setup:**  done
   - Create an SQLite database (`employees.db`).  
   - Create a table called `employees` with the following columns:  
     - `id` (INTEGER PRIMARY KEY, AUTOINCREMENT)  
     - `name` (TEXT, NOT NULL)  
     - `age` (INTEGER)  
     - `department` (TEXT)  
     - `salary` (REAL)  

2. **Perform CRUD Operations:**  
   - **Add a new employee** to the database.  done
   - **View all employees** in the database.  done
   - **Update an employee's details** (e.g., change department or salary).  done
   - **Delete an employee record** by ID.  done

3. **Search Functionality:**  
   - Allow users to search for employees by **name** or **department**.  done

4. **Implement User Interaction:**  
   - Create a **command-line menu** allowing users to select actions (Add, View, Update, Delete, Search, Exit).  done

---

 **Bonus Challenges (Optional for Extra Learning):**  
✅ **Data Validation:** Ensure only valid inputs are accepted (e.g., age must be a number). done 
✅ **Exception Handling:** Handle errors (e.g., if a user tries to update a non-existent employee).  done
✅ **Sorting & Filtering:** Allow users to view employees sorted by salary or filter by department.  done
✅ **Export Data:** Save employee records as a CSV file.  done

---

