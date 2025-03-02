# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr.", "Spongebob", "Squarepants")
# we're currently using positional arguments
# the position of these arguments does matter

#an optinial feature when sending arguments to a function is that we could turn these into keyword arguments
hello("Hello", last="Schmidt", title="Mr.", first="Jonas")

#if you're mixing and matching positional arguments and keyword arguments;
#you want to be sure that the positional arguments are first



#a lot of built-in functions such as the print function; they have some keyword arguments, you can use
print("1", "2", "3", "4", "5", sep="-")

print()

for x in range(1, 11):
    print(x, end=" ")

#EXERCİSE, generate a phone number
def get_phone(country, area, first, last):
    return f"{country}--{area}--{first}--{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)
