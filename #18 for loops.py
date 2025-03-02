#for loop = execute a block of code a fixed number of times.
#           You can iterate over a range, string, sequence, etc.

#there is a lot of overlap where you could use either a while loop or a for loop

#i would like to start at 1 then count to 10. but the second number is exclusive so
#we're going to write 11
for x in range(1, 11):
    print(x)

#to count backwards
for count in reversed(range(1, 11)):
    print(count)
print("HAPPY NEW YEAR!")

#there is an additional parameter too you could add
#that is the step
for count2 in range(1, 11, 2):
    print(count2)

credit_card = "1234-5678-9012-3456"

for count3 in credit_card:
    print(count3)

#we'll have a few projects involving that. there are two useful keywords as well
#these aren't exclusive to for loops, you can use these within while loops as well

#suppose we going to count to 20
for z in range(1, 21):
    if x == 13:
        continue
    else:
        print(z)
#we have skipped the number 13
#to skip over an iteration you can use the continue keyword

for y in range (1, 21):
    if y == 13:
        break
    else:
        print(y)
#if x equal to 13 then break. so yeah we have only counted to 12.