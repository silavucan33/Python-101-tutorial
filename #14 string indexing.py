#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "1234-5678-9012-3456"

credit_number[0]
#the first postion has an index of zero. computers always start with zero so that's why the first index is zero
#print(credit_number[3])
#if you have just one field listed without any colons it's assumed you're filling in the starting position

#what if you would like the first four digits of the string?
#print(credit_number[0:4])
#you can omit the zero in the beginning. pyhton assumes the starting position will bethe beginnning of the string

#print(credit_number[5:9])

#maybe we need the last 12 digits
#print(credit_number[5:])
#if you need everything up to the end of the string, you don't need to list an ending index. just be sure to add that colon

#you could also use a negative index. if you need the last character in a string
#print(credit_number[-1])

#step: using the step field we can access the characters in a string by a given step
#we can count by twos or we can count by threes
#if we're not filling in the starting or ending Fields but we need a step we would need two colons
#print(credit_number[::3])


#EXERCİSE

last_digits = credit_number[-4:]
#we can omit the ending index. pyhton assumes we need the rest of the string then
print(f"XXXX-XXXX-XXXX-{last_digits}")

#EXERCİSE2, reverse the characters in the string

credit_number = credit_number[::-1]
#if we need the entire string we don't need a starting index or an ending index
#"-1" will reverse a string
print(credit_number)


#you can list a starting position, ending position and even a step if you need to skip over characters