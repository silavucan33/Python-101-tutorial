# Python compound interest calculator

principle = 0
rate = 0
time = 0


#nothing happens we go straight to the results. so the reason that this is happening
#is that when we reach the while loops, this condition is false from the beginning
#we never end up entering these while loops. we skip over them. because these three conditions are all false
while principle < 0:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")

print(principle)


while rate < 0:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")

print(rate)

while time < 0:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")

total = principle * pow(1 + rate / 100, time)
print(f"Balance after {time} year/s: ${total:.2f}")


#you could write either a standard while loop with a condition. such as;
while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero")

print(principle)


while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than or equal to zero")

print(rate)

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than or equal to zero")

total = principle * pow(1 + rate / 100, time)
print(f"Balance after {time} year/s: ${total:.2f}")


#A diffrent variation of this while loop. We should be able to enter zero values in now
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break
#this loop would continue forever you would need to explicitly break out of the while loop
# using this break keyword

total = principle * pow(1 + rate / 100, time)
print(f"Balance after {time} year/s: ${total:.2f}")
