# Python reading files (.txt, .json, .csv)

#in the previous topic we have created some sample files to work with

file_path = "C:\\Users\\user\\Desktop\\python project files\\output1.txt"

try:
    with open(file_path, "r") as file:
    #when we read our file object it's going to return one long string which we will assign to a variable named content
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")

#what if we don't have permission to this file? (edited the permissions of output1)
except PermissionError:
    print("You do not have permission to read that file")


#let's say we would like to read a json file
import json
file_path = "C:\\Users\\user\\Desktop\\python project files\\output4.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file) #load method. that should read the contents of my file
        #print(content)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")


#here's how to read a csv file
import csv
file_path = "C:\\Users\\user\\Desktop\\python project files\\output5.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file) #(we're given a memory address)
#with the csv file what we need to do is read the csv file line by line
        for line in content:
             #print(line)
             print(line[1]) #if you need a specific column of data from a csv file you can use an index as one possibility
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

