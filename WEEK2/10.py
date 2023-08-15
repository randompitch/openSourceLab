#Q10 Python provides a built-in function map that applies a function to each element of a list.
#    Provide an implementation for map using list comprehensions.
def double(n):
    return n+n

numbers = [x for x in range(1,6)]       #list comprehension
print("List originally: ", numbers)
newList = map(double,numbers)       #map function
print("List after mapping it to function double: ",list(newList))   