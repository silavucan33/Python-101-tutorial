# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBİTRARY

def add(a, b):
    return a + b

print(add(1, 2))

#what if i would like to pass in three parameters this time
def add(*args):
    print(type(args))

add(1, 2, 3)
#the arguments that we pass into this function
#we will pack them all into a tupple

def add2(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))
#with my parameter args you can change this name to something else

def add3(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add3(1))

#EXAMPLE
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")


#KWARGS
def print_address(**kwargs):
    pass

print_address(street="123 Fake St.",
              city="Detroit",
              state="MI",
              zip="54321")
#when i pass in these keyword arguments, we will pack them into a dictionary
#within this function you can treat kwargs as if it's a dictionary
def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

print_address(street="123 Fake St.",
              city="Detroit",
              state="MI",
              zip="54321")

#here are the keys
def print_address3(**kwargs):
    for key in kwargs.keys():
        print(key)

print_address3(street="123 Fake St.",
              city="Detroit",
              state="MI",
              zip="54321")

#for both
def print_address4(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address4(street="123 Fake St.",
              city="Detroit",
              state="MI",
              zip="54321")

#EXERCİSE, cover both args and kwargs together
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

#   for value in kwargs.values():
#        print(value, end=" ")

#let's add our "street" on one line then the "city", "state" and the "zip code" on the next line


    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    #with this get method, you'll probably need to place them within single quotes
    #because if you use double quotes python gets confused as to where this "f string" ends
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321")
#when we invoke this function we have a mix of arbitrary positional arguments and arbitrary keyword arguments
#this "shipping label" function is designed to accept both. you need args first followed by kwargs



#what if our print statement is set up to display a street and an apartment but the user doesn't have an apartment?
#this would display none
def shipping_label1(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label1("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               city="Detroit",
               state="MI",
               zip="54321")

#CHALLENGE ROUND, what if is a user has a "po box"
def shipping_label1(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label1("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               pobox= "PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")
