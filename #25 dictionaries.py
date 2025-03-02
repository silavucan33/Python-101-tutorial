#dictionary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))

# FEW METHODS
print(capitals.get("India"))

#you can also check with that if a key is within our dictionary. get method
if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist!")

#using the update method we can insert a new key value pair or update an existing key value
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})

#to remove a key value pair
capitals.pop("China")
#to remove the latest key value pair
capitals.popitem()
#capitals.clear()


#to get all of the keys within the dictionary, but not the values
keys = capitals.keys()

print(capitals)
print(keys)

#to itarate over every key that is returned from the keys method of your dictionary
for key in capitals.keys():
    print(key)

#to get all of the values within your dictionary
values = capitals.values()
print(values)

#let's iterate and print over every value within our dictionary
#for value in capitals.values():
#    print(value)

#items return a dictionary object which resembles a 2d list of tuples
# items = [(), (), ()]
items = capitals.items()
#how might this be useful?
for key, value in capitals.items():
    print(f"{key}: {value}")


