# Create a class `Employee`
# - Use `__init__`, `__str__` methods
# - Add a class variable `count` to keep track of number of employees
class Employee:
    count =0       # Class variable to track number of employees

    def __init__(self,name,emp_id):
        self.name =name
        self.emp_id =emp_id
        Employee.count+=1

    def __str__(self):
        return f"Employee Name :{self.name}  ID :{self.emp_id}"   

emp1 = Employee("Alice",101)
emp2 = Employee("Bob", 102)    
print(emp1)
print(emp2)
print(f"Total employee :{Employee.count}")