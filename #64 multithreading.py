#multithreading = Used to perform multiple tasks concurrently (multitasking)
#                 Good for I/O bound tasks like reading files or fetching data from APIs
#                 threading.Thread(target=my_function)
#(I/O) means input output

import threading
#let's say we have a bunch of chores to do. we have to walk the dog get the mail and take out the trash

#just to simulate these functions taking an indeterminate amount of time. I'm going to import the time module to help us
#import time

#def walk_dog():
#    time.sleep(8)
#    print("You finish walking the dog")

#def take_out_trash():
#    time.sleep(2)
#    print("You take out the trash")

#def get_mail():
#    time.sleep(4)
#    print("You get the mail")

#walk_dog()
#take_out_trash()
#get_mail()

#these functions are running on the same thread, the main thread our main pyhton program
#we have to complete these chores in order one by one because they all running on the same thread

# we could accomplish all three tasks at the same time

import time

def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking {name}")

def take_out_trash(biomull, plastikmull):
    time.sleep(2)
    print(f"You take out the {biomull} and {plastikmull}")

def get_mail():
    time.sleep(4)
    print("You get the mail")

#let's say we have a chore object
chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
#that function accepts arguments, we need one more keyword argument and it's 'args'
#we will send this function a tuple. within this tuple we will list our arguments
#since this is a tuple, if we only have one argument we have to end that tuple with a comma, to let python know that is a tuple
chore1.start()

chore2 = threading.Thread(target=take_out_trash, args=("ekmek", "plastikbardaklar"))
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

#so we're executing functions concurrently we're multitasking. all at the same time

#we get this message that all chores are complete, although we haven't finished any yet and we're still completing them
#with the join method we will wait for these threads to finish before continuing with the rest of the program

chore1.join()
chore2.join()
chore3.join()

print("ALL chores are complete!")

#NOTE: The call to join blocks until thread finishes execution. Each .join() waits for its respective thread to end.


