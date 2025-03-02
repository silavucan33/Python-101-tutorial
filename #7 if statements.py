# if = Do some code only IF some condition is True
#      Else do something else

# It's a basic form of decision making

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
#elif age >= 100:
#   print("You are too old to sign up")
#well it states "You are now signed up!". The reason we didn't reach this part of our else if statement.
#because the first(if age >= 18) condition is still technically true.
#you do need to pay attention to your order of if and else if statements

else:
    print("You must be +18 to sign up")

# We can check more than one condition before reaching te else statement.
# We can add an else if statement which we just shorten to elif (meaning else if)

#SECOND EXAMPLE
response = input("Would you like food? (Y/N): ")

# the doubles equal sign is the comparison operator. it will check to see if two values are equal
# you don't want one equals because that's the assigment operator
if response == "Y":
    print("Have some food!")
elif response == "y":
    print("Have some food!")
else:
    print("No food for you!")

#THİRD EXAMPLE
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

#FOURTH EXAMPLE (THE USE OF BOOELANS WİTH İF STATEMENTS)
for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

#FIFTH EXAMPLE
online = True

if online:
    print("The user is online")
else:
    print("The user is offline")