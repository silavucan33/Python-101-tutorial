# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

# Functions can't see inside of other functions

# but they can see inside of their own function
# that's why we sometimes pass arguments to functions;
# def happy_birthday(name, age):

def func3():
    x = 1

    def func4():
        x = 7
        print(x)
    func4()
func3()
# there's an order of operations use any local variables first, then enclosed variables
# since x wasn't found within the local scope, we would use x within the enclosed scope


#Let's move on to the global scope
#(global meaning outside of any function)

def func5():
    print(x)

def func6():
    print(x)

x = 3
#If there's no local version as well as no enclosed version
# we would move on to the global version; where x equals 3

func5()
func6()


#BUILT-IN
from math import e

def func1():
    print(e)

e = 3
#If I was to set "e" to be a different value, what we're doing technically is;
#creating to different versions of "e"
#variables can share the same name as long as they're within a different scope
#we have a built-in version of "e" and a global version of "e"

func1()
