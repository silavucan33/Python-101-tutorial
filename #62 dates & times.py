
import datetime
#this module allows us to work with dates and times using our system clock, our computer's clock

#to create a date object
date = datetime.date(2025, 1, 2)

#to get the time right now
today = datetime.date.today()

time = datetime.time(12, 30, 0) #pass in hours, minutes and then seconds
now = datetime.datetime.now()

#we can format the appearance of the
#now = now.strftime("%H:%M:%S %d-%m-%Y") '%H' for hours. This format specifiers you can find according to the datetime documentation online
now = now.strftime("%H:%M:%S %d-%m-%Y")

print(date)
print(today)
print(now)

#EXERCISE, a current date and time has passed a target date and time

#first 'datetime' access the time module. and we create a new 'datetime'
target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")

