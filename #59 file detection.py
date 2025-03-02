# Python file detection

#to work with files using python
import os


#for file detection we can either use;
# Relative = folder/test.txt
# Absolute = C:/Users/Brocode/Desktop/test.txt

#relative file path
#file_path = "text.txt"       (name with extension)

#we'll be passing in the string of the file path as an argument

#absolute file path
#file_path1 = C:\Users\user\Desktop ( / or \\ )
file_path1 = "C:\\Users\\user\\Desktop"


#there is a built-in method of is file to check to see if that file is in fact a file and not a directory


if os.path.exists(file_path1): #built-in method 'exists'
    print(f"The location {file_path1} exists")

    if os.path.isfile(file_path1):
        print("That is a file")
    elif os.path.isdir(file_path1):
        print("That is a directory")

else:
    print("That location doesn't exist")
