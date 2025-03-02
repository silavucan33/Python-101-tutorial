# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself



class Student:

#2.we will also create a class variable for this demonstration
    count = 0
    total_gpa = 0

#1.we'll need a constructor to construct some student object
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

#3.I will create an instance method (instance methods have self as the first parameter)
#we're referring to the object we're currently working with
    def get_info(self):
        return f"{self.name} {self.gpa}"

#4.to create an class method, we will declare a class method with a 'class method' decorator
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())

