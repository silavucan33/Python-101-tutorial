# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

#Instance methods = Best for operations on instances of the class (objects)
#Static methods = Best for utility functions that do not need access to class data

#INSTANCE METHOD
# (they are methods that belong to indivual objects created from that class)
#def get_info(self):
#    return f"{self.name} = {self.position}"

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    #'get_info' is an instance method. each object that we create from this class will have their own 'info' method to return the information on that object


#STATIC METHOD
# static methods don't have 'self' as the first argument. we are not working with any objects created from this class.

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


#to use a static method, we will use the name of the class. rather than any object that we create from this class
#employee1 = Employee()   such as this. we don't need to do that
print(Employee.is_valid_position("Rocket Scientist"))
print(Employee.is_valid_position("Cashier"))
#this is a static method. it belongs to the class not any object created from that class

employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

#to call an instance method we have to access one of the instances of the class in order to use it.
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

#for an instance method you access an object then call the instance method
#with the static method you only need to access that class. you don't even need to create any objects from that class. it's a general utility method
