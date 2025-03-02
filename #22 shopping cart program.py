# Shopping cart program

foods = []
prices = []
total = 0

# im not using tuples because tuples are unchangeable
# we going to ask a user what food they would like to buy

# set is unordered so. list better

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
#this will take our input, make it lowercase
# if somebody types in uppercase q, he can't actually quit.
#if food == "q":
     break
    else:
        price = float(input(f"Enter the price a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")




