# nested loops = A loop within another loop (outer, inner)
#                outer loop:
#                    inner loop:


for x in range(1, 10):
    print(x, end="")
#all of these numbers on the same line at the end of my print statement
# print(x, end="") or you can add a diffrent character print(x, end="-")


#what i would like to repeat this three time
#for x in range(3)
#        you could also say range(1, 4)
#whatever code is within this loop will be executed three times
for jfjf in range(3):
    for y in range(1, 10):
        print(y, end="")

#on seperate lines
#let's add each iteration of the outer loop onto a new line
for gfgf in range(3):
    for u in range(1, 10):
        print(u, end="")
    print()

#PROJECT, a rectangle
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")
for gfgf in range(rows):
    for u in range(columns):
        print(symbol, end="")
    print()
