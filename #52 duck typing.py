# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck."


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

#what if we add a class that has nothing to do with animals?
#class Car:
#    def horn(self):
#        print("HONK!")

#Our car object doesn't have the minimum necessary attributes and methods.
#When iterating through this list of animals we're calling each animal speak method, which our car object doesn't have.

class Car:

#if I add the attribute
    alive = False

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

#My car meets the minimum necessary requirements to be considered an animal.

#as long as an object has the minimum necessary attributes and methods, you could treate it as a diffrent type of object.

