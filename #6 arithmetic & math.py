#arithmetic operators, math functions, and then a few exercises

friends = 10

#friends = friends + 1
#  we can also shorten this line of code
#friends += 1
#  this is known as an augmented assignment operator
#friends = friends - 2
#friends -= 2
#friends = friends * 3
#friends *= 3
#friends = friends / 2
#friends /= 2
#friends = friends ** 2
#friends **= 2
remainder = friends % 3
#modulus operator.
#it's fairly popular to use this operator to find if a number is even or odd, by dividing number 2.

print(remainder)



x = 3.14
y = 4
z = 5

#result = round(x)    sayıyı yuvarlamak
#result = abs(y)      distance away from zero as a whole number
#result = pow(4, 3)   you can raise a base to a given power
#result = max(x, y, z)  find the maximum value of various values
#result = min(x, y, z)  otherwise there's min

#print(result)

#VERY USEFUL CONSTANTS AND FUNCTİONS FROM THE MATH CLASS

import math

x = 9.9

print(math.pi)
print(math.e)
#result = math.sqrt(x)
# to find the square root of a number
#result = math.ceil(x)
# to round a floating point number up
result = math.floor(x)
# to round a number down

print(result)


#EXERCİCE1, calculate the circumference of a circle
import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")

#EXERCİSE2, calculate the area of a circle
import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

#print(f"The area of the circle is: {area}cm^2")
print(f"The area of the circle is: {round(area, 2)}cm^2")


#Only a part of this TOPIC. NOT ALL!!

