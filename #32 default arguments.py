#default arguments = A default value for certain parameters
#                      default is used when that argument is omitted
#                      make your functions more flexible, reduces # of arguments
#                      1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

#def net_price(list_price, discount, tax):
#    return list_price * (1 - discount) * (1 + tax)


#print(net_price(500, 0, 0.05))
# now suppose that maybe 90% of the time when we're executing this function;
# most of the time discount is zero and our sales tax is almost always the same

#what we could do to make this function a little more flexible is;
# to set 'discount' and 'tax' parameters to have a default value.
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))

#the nice thing about using default arguments is that let's say that somebody has a discount
#well this function would also accept up to two additional arguments
#print(net_price(500, 0.1))

#CREATE A COUNT UP TIMER
import time
def count(start, end):
    for x in range(start, end+1):
#within the range function the second argument is exclusive, so im going to add 1 to the end
       print(x)
       time.sleep(1)
    print("DONE!")

count(0, 10)

#let's assume that most of the time a user would like to begin at zero
def count(end, start=0):
    for x in range(start, end+1):
#within the range function the second argument is exclusive, so im going to add 1 to the end
       print(x)
       time.sleep(1)
    print("DONE!")

count(10)
#BE SURE! so if you use any default arguments you'll want to be sure that;
#they're after any positional arguments

