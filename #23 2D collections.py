
#          2dlist = [list1, list2, list3]
# it's really useful if you ever need a grid or Matrix of data
# kind of like an Excel spreadsheet

#fruits = ["apple", "orange", "banana", "coconut"]
#vegetables = ["celery", "carrots", "potatoes"]
#meats = ["chichken", "fish", "turkey"]

# each of these lists is a one-dimensional list

# to create a two-dimensional list
#groceries = [fruits, vegetables, meats]


# to access or change one of the elements.
#fruits[0] = "pineapple"
#print(fruits)

# with 2d lists it's diffrent
#print(groceries)
# If i were to print my 2D list of groceries, we would lay out the entire 2D list flat
# we have indivual lists seperated with a comma all enclosed within a set of square brackets


#fruits =     ["apple", "orange", "banana", "coconut"]
#vegetables = ["celery", "carrots", "potatoes"]
#meats =      ["chichken", "fish", "turkey"]
# each indivual lists resembles a row, each element resembles a column
#groceries = [fruits, vegetables, meats]

#print(groceries[0])  that would return an entire row

# for one of the elements found within one of the rows, you would need two indices
#print(groceries[2][1])

# when you declare 2d list you don't need to necessarily give each inner list a name

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chichken", "fish", "turkey"]]

#print(groceries[1][2])

# if you ever need to iterate over the elements of a 2d list
# you can use nested loops
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# using a single for loop would iterate over the rows but to also iterate over the elements found within each row
# we would use a nested loop

#TWO-DIMENSIONAL KEYPAD (on a phone)
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# if you ever need a grid or matrix of data, a 2d collection would work perfect

