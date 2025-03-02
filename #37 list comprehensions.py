# List compherension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]


#traditional loop
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

#list compherension
doubles1 = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(squares)

#with strings
fruits = ["apple", "orange", "banana", "coconut"]
shop = [fruit.upper() for fruit in fruits]
print(shop)

#another option
fruits1 = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
print(fruits1)


fruits = ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)


#with conditions
numbers = [1, -2, 3, -4, 5, 6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(odd_nums)

#EXERCISE
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)


#remember for every value in your iterable optionally;
#you can check a condition
#you can write an expression to modify that value if you choose and return something
