#while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

if name == "":
    print("You did not enter your name!!")
else:
    print(f"Hello {name}")

#What if I contiunally prompt the user to type in their name?
#we can't continue until they type in something

name2 = input("Enter your name: ")


while name2 == "":
    print("You did not enter your name")
    name2 = input("Enter your name: ")
#while this condition remains true, execute this code potentially forever
#until this condition is no longer true
print(f"Hello {name2}")

#You want some way to escape out of the while loop otherwise you'll run into what's known as an infinite loop
#So we are stuck in an infinite loop we can't actually escape this loop
#We didn't give ourselves an exit strategy
#while name2 == "":
#    print("You did not enter your name")
#print(f"Hello {name2}")

#EXAMPLE2
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

#EXAMPLE3
food = input("Enter a food you like(q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like(q to quit): ")

print("bye")

#EXAMPLE4
num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")