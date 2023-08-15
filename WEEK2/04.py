#Q4 Write a function extsort to sort a list of files based on extension.
import os
def extsort(x):
    i=0
    while(i<len(x)):
         x[i]=x[i].split('.')
         i=i+1
    x.sort(key=lambda x:x[1])
    i=0
    while(i<len(x)):
         x[i]=".".join(x[i])
         i=i+1 
    return x
lisFiles = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
print("Files before sorting: ", lisFiles)
print("\nFiles after sorting: ",extsort(lisFiles))