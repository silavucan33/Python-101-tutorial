import random

#print(help(random))

# for a random whole integer
# maybe you're rolling a six-sided dice
number = random.randint(1, 6)
print(number)

# within the randint method you can place variables as well as long
# as they contain numbers

low = 1
high = 100
number1 = random.randint(low, high)
print(number1)

#if you need a random floating point number
number2 = random.random()
print(number2)

#you can pick a random choice from a sequence
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

#using the shuffle method i can shuffle this sequence
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
