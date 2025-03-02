#object = A "bundle" of related attributes (variables) and methods (functions)
#         Ex. phone, cup, book
#         You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

#for better organization you can place them within a new pyhton file
#class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

#so from our main pyhton file we're going to import our car file, our car module

from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

#the memory address of this car object. where it's located
print(car1)

#instead of printing the object itself we're going to access one of the attributes found within this car
#we will follow the name of the car with a DOT
#this dot, it's known as the attribute access operator
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

#METHODS
#methods are actions that our objects can perform

car1.drive()
car2.drive()
car3.drive()

car1.stop()
car2.stop()
car3.stop()

car1.describe()
car2.describe()
car3.describe()