# Encapsulation Example
# - Create a class `Person` with private attributes `_name`, `_age`
# - Use getter and setter methods to access them

class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    #use Getter
    def get_name(self):
        return self._name

    #use setter
    def set_name(self,name):
        self._name = name 

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative!")    

p1 = Person("Alice", 25)
    
print("Name:", p1.get_name())  # Output: Name: Alice
print("Age:", p1.get_age())    # Output: Age: 25            