from script1 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script2")
    favorite_food("sushi")
    favorite_food("coffee")
    print('Goodbye!')
if __name__ == '__main__':
    main()
#so by adding this if statement, this script can be run as a standalone program
#or it can be imported





#we're running script2 but
#we're importing the functionality of the favorite food function from script1

#sometimes from another python script you want to borrow something
#but you don't want to run the main body of code directly