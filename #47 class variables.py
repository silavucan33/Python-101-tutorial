# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

#EXAMPLE
#class Car:

#    wheels = 4    CLASS VARİABLES

#    def __init__(self, model, year):
#        self.model = model
#        self.year = year     INSTANCE VARİABLES

class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
#if we're going to be modifying a class variable, in place of 'self' we'll use the name of the class
        Student.num_students += 1


student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(f"My graduating class of {Student.class_year} has {Student.num_students}")

print(student1.name)
print(student1.age)

#since we're accessing class year we'll access this class variable by the name of the class of 'Student'
print(student1.class_year)
print(Student.class_year)

print(Student.num_students)

