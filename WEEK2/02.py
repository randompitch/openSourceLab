#Q2 Write a function group (list, size) that takes a list and splits 
#   into smaller lists of given size

def group(l,size):
    return [l[i:i+size] for i in range(0, len(l), size)]

#main
n = int(input("Enter the number of elemnts: "))
array = []
print("Enter the numbers: ")
for i in range(0,n):
    ele = int(input())
    array.append(ele)

print("The array elements are: ", array)
p = int(input("Enter the size you want to split the list into: "))
print(group(array,p))
