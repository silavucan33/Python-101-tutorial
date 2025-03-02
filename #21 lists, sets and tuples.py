#collection = single 'variable' used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#LİST
fruits = ["apple", "orange", "banana", "coconut", "banana"]
# each value in a collection is also known as an element

# to access one of these elements found within your list
#print(fruit[2])
#print(fruits[::2])
#print(fruits[::-1])



# length of how many elements are within a collection
print(len(fruits))

# to find if a value is wihtin a collection
print("apple" in fruits)
# "in" operator will return a Booelan
print("pineapple" in fruits)

# to change one of the values after we create our list
#fruits[0] = ("pineapple")

for fruit in fruits:
    print(fruit)

#SOME METHODS

# to add an element to the end of a list
#fruits.append("pineapple")

# to remove an element
#fruits.remove("apple")

# we can insert a value at a given index
#fruits.insert(0, "pineapple")

# to sort a list. they are all in alphabetical order now
#fruits.sort()

# to reverse a list
#fruits.reverse()
# however these are not in reverse alphabetical order these elements are
# reversed based on the order in which we placed them

# to reverse alphabetical order
fruits.sort()
fruits.reverse()

# to clear a list
#fruits.clear()

# to return the index of a value
print(fruits.index("apple"))

# you could count the amount of times that a value is found within a list
print(fruits.count("banana"))

print(fruits)

#SET
fruits2 = {"apple", "orange", "banana", "coconut", "coconut"}
# we still only have one coconut
print(len(fruits2))
print("pineapple" in fruits2)

# we're not able to use indexing on a set because they're unordered

fruits2.add("pineapple")
fruits2.remove("apple")

# the pop method will remove whatever element is first. but it's going to be random though
#fruits2.pop()

# to clear
#fruits2.clear

print(fruits2)

# Sets may work well if you're working with constants, maybe colors for example.

#TUPLE
fruits3 = ("apple", "orange", "banana", "coconut", "coconut")
print(len(fruits3))
print("pineapple" in fruits3)

#there is only two methods we have access to (index and count)
print(fruits3.index("apple"))
print(fruits3.count("coconut"))

#with any of these collections, they're iterable. so so you can iterate over them using a for loop
for fruit3 in fruits3:
    print(fruit3)


# to list the diffrent methods that are available to a collection
#print(dir(fruits))
# for description of each methods
#print(help(fruits))
