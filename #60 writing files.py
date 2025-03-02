# Python writing files (.txt, .json, .csv)

#suppose we have some data that we would to output

# .txt
txt_data = "I like pizza!"

file_path = "output.txt"

#'with' is a statement. it's used to wrap a block of code to execute
#if we open a file the 'with' statement will also close that file when we're done with it
# ;so we don't need to manually close files

#the 'open' function will return a file object

#the second parameter is mode 'w' is 'Write'
# 'x' will also write if this file doesn't exist (if it already does exist we'll receive an error)
# 'a' is for append to append a file
# 'r' is to read

#'as' keyword to give it a name as file
with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")

#we also have the capability of setting an absolute file path
# let's say I would like to output this file to my desktop

txt_data1 = "I like sushi!"

# C:\Users\user\Desktop  ( / or \\ )
file_path1 = "C:\\Users\\user\\Desktop\\output1.txt"

with open(file_path1, "w") as file1:
    file1.write(txt_data1)
    print(f"txt file1 '{file_path1}' was created")

#for our text data there are diffrent modes as well

txt_data2 = "I like sushi!"

file_path2 = "C:\\Users\\user\\Desktop\\output2 .txt"

try:
    with open(file_path2, "x") as file2:
        file2.write(txt_data1)
        print(f"txt file1 '{file_path2}' was created")
except FileExistsError:
    print("That file already exists!")


with open(file_path1, "a") as file1: #'a' any new data will be append to that file
     file1.write(txt_data1)
     print(f"txt file1 '{file_path1}' was created")



employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "C:\\Users\\user\\Desktop\\output3 .txt"

#write() argument must be str, not list
#in order for us to write each item within a list we'll need to iterate over it using some sort of loop
# ; we can write a list or any other collection directly

try:
    with open(file_path, "x") as file:
        for employee in employees:
              file.write(employee + " ")
        print(f"txt fileee '{file_path}' was created")
except FileExistsError:
    print("This file already exists!")

# .json

#in summary a .json file is made of key value pairs
import json

employee = { #let's say we have a dictionary
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}
file_path = "C:\\Users\\user\\Desktop\\output4.json"

# the dump method will convert our dictionary to a json string to output it

#The dump() needs the json file name in which the output has to be stored as an argument.
with open(file_path, "w") as file:
    json.dump(employee, file, indent= 4) #indent for how many spaces do we want to indent each
    print(f"json file '{file_path}' was created")

# .csv
#csv files are pretty common with a spreadsheet of data like an Excel spreadsheet

#we will create a 2d data structure of employees. this will be a list of lists.
#think of our 2d data structure as a table of rows and columns

import csv
employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "C:\\Users\\user\\Desktop\\output5.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file) #writer is an object it provides methods for writing data to a csv file
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("This file already exists!")
 