
# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A


class Animal:

    def __init__ (self, name): #constructor
        self.name = name
#now with these other classes if you're not assigning any attributes
#or if you don't need any other initialization logic, you don't need a constructor

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
fish.hunt()
fish.sleep()

#rabbit.hunt()  but they do not have a 'hunt' method because they're not 'predator'

#children classes can inherit from more than one parent