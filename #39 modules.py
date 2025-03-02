# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable seperate files

#print(help("modules"))
#print(help("math"))

#to include a module, we would type 'import'
import math
print(math.pi)

#you can give your module a nickname
import math as m
print(m.pi)

from math import pi
print(pi)

#to create a module
import examplemodule

result = examplemodule.pi
result = examplemodule.square(3)
result = examplemodule.cube(3)
result = examplemodule.circumference(3)
result = examplemodule.area(3)

print(result)

#it can be useful at times to seperate your program into indivual files
