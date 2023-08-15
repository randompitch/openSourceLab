#Q16 Write a program to count the frequency of characters in a given file. 
#    Can you use character frequency to tell whether the given file is a Python program file, 
#    C program file or a text file?
filename = input("Enter the file name: ")
file_extension = filename.split('.')[-1]
with open(filename, "r") as file:    
    nchar = 0
    for line in filename:
        nchar += len(line)    
    print("Character frequency:", nchar)    
    if file_extension == "py":
        print("It's a Python program file")
    elif file_extension == "c":
        print("It's a C program file")
    else:
        print("It's a text file")
