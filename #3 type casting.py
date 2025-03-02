#Typecasting = the process of converting a variable from one data type to another
#              str(), int(), float(), bool()

name = "John Smith"
age = 25
gpa = 3.2
is_student= True

# to learn the datatype use type function
print(type(name))

gpa = int(gpa)

age = str(age)
age += "1"

name = bool(name)

print(gpa)
print(age)
