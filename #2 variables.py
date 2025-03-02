# Comments is used for notes for yourself or for other people reading this code
print ("Hello World!")
print ("What's going on?")

# Variable = A container for a value (string, integer, float, boolean)
#        A variable behaves as if it was the value it contains

# Strings
first_name =  "Hüseyin"
food = "lahmacun"
email =  "huseyinbalik123@fake.com"

print(first_name)

# f string
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# Integers   An integer is a hole number
age = 25
quantity =  3.5
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float  A float is a number but it contains a decimal portion
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is {price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")

#  Boolean  A boolean is either true or false (first letter is capital)

is_student = False
for_sale = True
is_online = False

print(f"Are you a student?: {is_student}")
#  with boolean values we really don't output them directly. you are most likely to see them used internally within a program such as when working with if statements

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

if is_online:
    print("You are online")
else:
    print("You are offline")

