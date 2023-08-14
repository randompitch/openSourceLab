#Q12. Write a function triplets that takes a number n as an argument and 
#     returns a list of triplets such that the sum of first two elements 
#     of the triplet equals the third element using numbers below n.
#     Please note that (a, b, c) and (b, a, c) represent the same triplet.

def triplets(n):
    for i in range(1,n+1):
        if((2*i+1) < n):
            triplet = [i, i+1, 2*i+1]
            print(triplet)
            
n = int(input("Enter the number upto which you want to find triplets: "))
triplets(n)
