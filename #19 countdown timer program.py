#import time
#my_time = int(input("Enter the time in seconds: ")

#for x in range(0, my_time):
#    print(x)
#    time.sleep(1)

#print("TIME'S UP!)


#i would like to count backwards. what we could do is enclose
#our range function within the reverse function
#   for x in reverse(range(0, my_time)):

#but another technique that we can use is by using a step
#   for x in range(my_time, 0, -1):

import time
#we'll need to import the time module. there's a pretty cool function within the time module
#that is the sleep function

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
# % returns the remainder of division

    minutes = int(x / 60) % 60
#modulus 60. we would not like {minutes:02} this field of minutes to go above 60

    hours = int(x / 3600)
#the reason i didn't add modulus 24. i don't have days within my fstring
#we can display any amount of hours

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
# i would like to add some zero padding and we can do that with a format specifier
# after seconds i will add colon. i need to display to digits then zero pad those digits

#within the set of parenthesis our program will essentially sleep for a given amount of seconds
    time.sleep(1)

print("TIME'S UP!")
