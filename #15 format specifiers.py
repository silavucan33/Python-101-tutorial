#format specifiers = {value:flags} format a value based on what
#                                   flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.3f}")
#even tough price2 and price3 only have two decimal places in the original numbers
#we will concatenate some additional zeros




price4 = 3.14159
price5 = -987.65
price6 = 12.34

print(f"Price 4 is ${price4:10}")
print(f"Price 5 is ${price5:10}")
print(f"Price 6 is ${price6:10}")
#each value now has a total of 10 spaces to display the output



price7 = 3.14159
price8 = -987.65
price9 = 12.34

print(f"Price 7 is ${price7:010}")
print(f"Price 8 is ${price8:010}")
print(f"Price 9 is ${price9:010}")
#each number is now zero padded



price10 = 3.14159
price11 = -987.65
price12 = 12.34

print(f"Price 10 is ${price10:<10}")
print(f"Price 11 is ${price11:<10}")
print(f"Price 12 is ${price12:<10}")
#all these numbers are now left justified then we have all of the after
#they're all uniform



price13 = 3.14159
price14 = -987.65
price15 = 12.34

print(f"Price 13 is ${price13:>10}")
print(f"Price 14 is ${price14:>10}")
print(f"Price 15 is ${price15:>10}")
#right justify would ve a right angle bracket



price16 = 3.14159
price17 = -987.65
price18 = 12.34

print(f"Price 16 is ${price16:^10}")
print(f"Price 17 is ${price17:^10}")
print(f"Price 18 is ${price18:^10}")
#our numbers are now centered



price19 = 3.14159
price20 = -987.65
price21 = 12.34

print(f"Price 19 is ${price19:+}")
print(f"Price 20 is ${price20:+}")
print(f"Price 21 is ${price21:+}")
#if you have any positive values and you would like to display a plus sign just use plus



price22 = 3.14159
price23 = -987.65
price24 = 12.34

print(f"Price 22 is {price22: }")
print(f"Price 23 is {price23: }")
print(f"Price 24 is {price24: }")
#or you could use a space for any positive numbers
#these numbers are lined up evenly even though we have a negative number in here



price25 = 3000.14159
price26 = -9870.65
price27 = 1200.34

print(f"Price 25 is {price25:,}")
print(f"Price 26 is {price26:,}")
print(f"Price 27 is {price27:,}")
#..there is a thousand seperator which is a comma
#we should probably increase the value of our prices



#we could also mix and match flags
price28 = 3.14159
price29 = -987.65
price30 = 12.34

print(f"Price 28 is {price28:+,.2f}")
print(f"Price 29 is {price29:+,.2f}")
print(f"Price 30 is {price30:+,.2f}")
