#Q17. Write a program to find anagrams in a given list of words. 
#   Two words are called anagrams if one word can be formed by 
#   rearranging letters of another. For ex: ‘eat’, ‘ate’ are anagrams.

def anagram(lis):
    print("\nThe anagrams in the given list are: ")
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if(len(lis[i]) == len(lis[j]) and sorted(lis[i]) == sorted (lis[j]) ):
                print(f"{lis[i]} & {lis[j]}")
            
        
    
n = int(input("Enter number of words in list: "))
lis = []
for i in range(0, n):
    str = input(f"Enter string {i+1}: ")
    lis.append(str)
    
anagram(lis)
