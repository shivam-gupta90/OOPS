# - Create a class `Rectangle`
# - Attributes: length and width
# - Methods: `area()` and `perimeter()`

class Rectangle:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width

    def Area(self):
        return self.lenght * self.width

    def Perimeter(self):
        return  2 * self.lenght *self.width

find = Rectangle(3,5)
print(find.Area()) 
print(find.Perimeter())        