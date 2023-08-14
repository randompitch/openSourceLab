#Q3 Write a function “lensort” to sort a list of strings based on length.
def lensort(s, n):
    for i in range(1, n):
        temp = s[i]
        j = i - 1
        while j >= 0 and len(temp) < len(s[j]):
            s[j + 1] = s[j]
            j -= 1 
        s[j + 1] = temp

#main
stringLis = ["akshita","megha", "sambhav","megs"]
n = len(stringLis)
print("List of Strings originally: ")
for i in range(n):
    print(stringLis[i], end = " ")    
lensort(stringLis, n)
print("\n\nList of strings after sorting:")
for i in range(n):
    print(stringLis[i], end = " ")  
