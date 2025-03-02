#Membership operators = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")


#what i would like to do is check to see if my letter is found in my word

# 'in' is going to return a Booelan value of true, if that letter is found or false if it's not
if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

#or for the inverse, you could say
#if letter not in word:
#    print(f"{letter} was not found")
#else:
#    print(f"There is a {letter}"

#searching for a value or a variable within a;
#STRING

#let's try a set (lists, tuples and sets are going to behave similarly)
students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")
if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

#DICTIONARİES
grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")


#EXAMPLE

email = "BroCode@gmail.com"

if "a" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
