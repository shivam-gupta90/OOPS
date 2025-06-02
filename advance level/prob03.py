# - Multiple Inheritance
# - Class `Person`, `Employee`, and `Manager`
# - Show how `Manager` inherits from both `Person` and `Employee

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self,emp_id,emp_salary):
        self.emp_id =emp_id
        self.emp_salary = emp_salary

class Manager(Person,Employee):
    def __init__(self,name,age,emp_id,emp_salary,dept_name):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, emp_salary)
        self.dept_name = dept_name

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Employee ID: {self.emp_id}, Salary: {self.emp_salary}")
        print(f"Department: {self.dept_name}")

mgr = Manager("Anita", 35, "E102", 85000, "AI & ML")
mgr.display()
