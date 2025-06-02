# Create a class `Student`
# - Attributes: name, age, grade
# - Method: `display_info()` that prints all the details.

class student:
    def __init__(self,name,age,grade):      
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("The name of stuedent is :",self.name)
        print("The age of student is :",self.age)
        print("The grade of student is :",self.grade)    

std1= student("kapil",28,"A+")
print(std1.name)
print(std1.age)
print(std1.grade)        