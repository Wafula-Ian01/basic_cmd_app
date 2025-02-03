import manager
import prompt

# Initialize the database
manager.Employee.initDB()

# Run the application
def main():
    prompt.cmd()

# Start the application
if __name__ == "__main__":
    main()
    
#RUN THIS IN COMMAND PROMPT: python3 -u "/Path/To/Python task/main.py"