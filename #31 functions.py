#function = A block of resuable code
#           place () after the function name to invoke it


#to repeat this song 3 three times, there is a better way than repeating our code or using loops

# to define a function; def + unique function name
# any code belongs to the function; indent underneath
#def happy_birthday():
#   print("Happy birthday to you!")
#    print("You are old!")
#   print("Happy birthday to you!")
#   print()

#i will add one parameter to my happy birthday function;
#  i will name this data name
#a parameter is kind of like a temporary variable that's used within a function
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

#when you invoke a function you can pass in some data those are known as arguments but you'll need a matching set of parameters
#the order does matter

#to invoke this function
#happy_birthday()

#with functions you are able to send data directly to a function
#using what are known as arguments you can send values or variables directly to a function

#any data you send a function known as arguments
#but you need a matching set of parameters, that are in order
#happy_birthday("Joe")
#happy_birthday("Steve")
#              first name

#when you invoke a function you can send more than one argument
happy_birthday("John", 20)
happy_birthday("Steve", 34)


#EXAMPLE
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

#to invoke this function, we will type the function's name, add a set of parantheses; a username, an amount and a due date
display_invoice("Huso25", 42.50, "01/01")

#ANOTHER EXAMPLE
#return = statement used to end a function
#         and send a result back to the caller

#we'll invoke a function to add two numbers together
#when we invoke a function we can send some data back
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

#after we resolve this function a value is returned
#just imagine that after we finish this function;
#  this function becomes whatever is returned
#EXAMPLE
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("eda", "demirci")
#using the return statement you can return some data back to the place in which you call a function

print(full_name)



