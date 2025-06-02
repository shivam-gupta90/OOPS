# - Implement Inheritance
# - Class `Animal` with method `speak()`
# - Subclasses: `Dog`, `Cat` that override `speak()

#note : override means like child his parents inheritance

class Animal:
    def speak(self):
        print(" some generic animal sound")

class Dog:
    def speak(self):
        print("The dog is bark")  

class Cat:
    def speak(self):
       print("The cat make sound of meow")

animal = Animal()
animal.speak()
dog = Dog()
dog.speak()
cat = Cat()
cat.speak()


#note : when we are using the print .so if we want ti access the variable use above written method



# when we are using the return method 


# Base Class
class Animal:
    def speak(self):
        return "Some generic animal sound"

# Subclass Dog
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Subclass Cat
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example Usage
if __name__ == "__main__":
    animal = Animal()
    dog = Dog()
    cat = Cat()

    print("Animal says:", animal.speak())  # Output: Some generic animal sound
    print("Dog says:", dog.speak())        # Output: Woof!
    print("Cat says:", cat.speak())        # Output: Meow!


