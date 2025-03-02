
name = input("Enter your full name: ")
phone_number = input("Enter your phone #: ")


result1 = len(name)
#len function will give us the lenght of a string, how many characters is it

#if we were to type our variable name follow by a DOT, we have access to a whole bunch of diffrent methods
result2 = name.find(" ")
#the find method will return the first occurence of a given character the position
#when working with indexes we always begin with zero

#if you need the last occurence there is a diffrent method. r meaning reverse
result3 = name.rfind("o")

#we can capitalize the first letter in a string by using the capitalize function
name1 = name.capitalize()
name2 = name.upper()
name3 = name.lower()

#the isdigit method will return either true or false if a string only contains digits. the result is a boolean
result4 = name.isdigit()
#otherwise we have have isalpha. depending if a string contains only alphabetic characters
result5 = name.isalpha()
result6 = phone_number.count("-")

#we could eliminate all the dashes compeletely by replacing the dashes or another charachter with an empty string
phone_number = phone_number.replace("-","")

#print(phone_number)

#IF YOU WOULD LIKE A COMPREHENSIVE LIST OF ALL THE STRING METHODS AVAİLABLE TO YOU, YOU CAN USE THE HELP FUNCTION TYPE IN THE DATA TYPE
#print(help(str))

#EXERCİSE
# validate user input exercise
# 1. username is no more than 12 charachters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a user name: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")