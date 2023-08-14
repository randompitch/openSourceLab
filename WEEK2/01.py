#Q1 Write a function “duplicate” to find all duplicates in the list.
def duplicate(l1):
    dup = []
    l1.sort()
    for i in range(0, len(l1)):
        if (l1[i] not in dup) and (l1[i] == l1[i-1]):
            dup.append(l1[i])
    print("\nThe duplicate elements in the list are: ")
    for i in range(0,len(dup)):
        print(dup[i], end = " ")
    
#main
l1 = [1,2,3,2,4,5,5,6,7,8,9,5,9,6]
print("The elements in the list are: ")
for i in range(0, len(l1)):
    print(l1[i], end = " ")
duplicate(l1)
