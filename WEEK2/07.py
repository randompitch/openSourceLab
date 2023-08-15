#Q7 Write a program reverse.py to print lines of a file in reverse order.
with open("myfile.txt", "r") as myfile:
    data = myfile.read()
 
data = data[::-1]
print(data)