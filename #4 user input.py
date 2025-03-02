# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

# input("What is your name?: ")
name = input("What is your name?: ")

# age = int(age) what we could instead
age = int(input("How old are you?: "))
age = age + 1

print(f"Hello {name}!")
print("HAPPY BİRTHDAY!")
print(f"You are {age} years old")

#EXERCİSES
# Exercise 1 Rectangle Area Calc

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

# to add a superscript  Windows: NumLock + Alt + 0178
print(f"The area is: {area}cm²")


# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")