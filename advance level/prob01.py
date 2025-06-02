# - Polymorphism: Create a class `Shape` with method `area()`
# - Subclasses: `Triangle`, `Square`, `Rectangle` that implement `area()` differently
class Shapes:
    def area(self):
        raise NotImplementedError("subclass must be implement this method")
    
class Triangle:
    def __init__(self,lenght,height):
        self.length = lenght
        self.height = height
    def area(self):
        return 0.5 * self.length *self.height
    
class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side ** 2
    
class Rectangle:
    def __init__(self,length,breath):
        self.lenght =length
        self.breath = breath
    def area(self):
        return self.lenght * self.breath
    
# Create objects of each shape
Shapes = [
    Triangle(10, 5),
    Square(4),
    Rectangle(6, 3)
]

# Use polymorphism to call area() on each shape
for shape in Shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")
