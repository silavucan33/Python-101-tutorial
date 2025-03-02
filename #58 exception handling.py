# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#              1.try, 2.except, 3.finally

#ZeroDivisionError
# 1 / 0

#TypeError
# 1 + "1"

#ValueError
# int("pizza")


#any code that's dangerous where it could cause an error you'll place with a try block
#for example anytime we accept user that is considered dangerous code, because a user can type in anything

try:
    number = int(input("Enter a number: "))
    print(1 / number)
#if we run into one of these exceptions we can execute some alternative code
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter only numbers please!")

#now what you may see some people do is they will just catch all exceptions
except Exception:
    print("Something went wrong!")

finally: #it always executes, regardless if there's an exception or not.
    print("Do some cleanup here")


#if there's an exception that occurs it's not a zero division error and it's not a value error than we can add that 'catch all', where we catch any unseen exceptions


#there are many diffrent types of exceptions. you can always look under the official pyhton documentation for an extensive list
