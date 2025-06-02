# - Define a class `Car`
# - Initialize make, model, year
# - Method to display car 

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def Display_car(self):
        print(f"car :{self.make} {self.model} in {self.year} ")

car1 = Car("Toyota","hybride",2024)
print(car1.Display_car())