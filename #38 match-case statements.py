# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

def day_of_week(day):
        if day == 1:
            return "It is Sunday"
        elif day == 2:
            return "It is Monday"
        elif day == 3:
            return "It is Tuesday"
        elif day == 4:
            return "It is Wednesday"
        elif day == 5:
            return "It is Thursday"
        elif day == 6:
            return "It is Friday"
        elif day == 7:
            return "It is Saturday"
        else:
            return "Not a valid day"

print(day_of_week(1))


#FIRST EXAMPLE
def day_of_week1(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"
# 'case _' if there are no matching case this case would function as the else statement

print(day_of_week1(1))

#SECOND EXAMPLE
def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return True
        case "Tuesday":
            return True
        case "Wednesday":
            return True
        case "Thursday":
            return True
        case "Friday":
            return "It is Friday"
        case "Saturday":
            return True
        case _:
            return False

print(is_weekend("Monday"))

#there is a way we can modify this match case too

#we are going to use the or logical operator (which is represented with a vertical bar)
def is_weekend1(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend1("Monday"))
