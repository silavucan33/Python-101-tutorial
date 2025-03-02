
#print(dir())
#('dir' meaning directory) pyhton has all of these built-in attributes

from script2 import *

# "*" means everything

#so by adding this if statement of "if __name__ == '__main__':
#we can check to see which file is being run directly

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")


if __name__ == '__main__':
    main()