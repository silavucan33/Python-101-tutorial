# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

#lists and tuples
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number, end=" - ")
print()

#sets (not reversible)
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)


#strings
name = "Bro Code"

for character in name:
    print(character, end=" ")
print()

#dictionaries
my_dictionary = {"A": 1, "B": 2, "C": 3}
# if you iterate over a dictionary, the dictionary is going to return all the keys
# but not the values

for key in my_dictionary:
    print(key)

# if you need the values of "my_dictionary", use the built-in values method
for value in my_dictionary.values():
    print(value)
# this will return all the values of your dictionary as an iterable

#if you need both the keys and the values, use the items method
for key, value in my_dictionary.items():
    print(key, value)
