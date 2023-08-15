#Q9 Write a program wrap.py that takes filename and width as arguments 
#   and wraps the lines longer than width.
import sys
def wrap(filename):
    k = int(input("Enter width: "))
    f = open(filename).readlines()
    for i in f:
        new = i
        while len(new)>k:
            print((new[:k]))
            new=new[k:]
    print(new)

filename = input("Enter file name: ")
wrap(filename)