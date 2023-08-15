#Q11 Python provides a built-in function filter(f, a) that returns items of the list a for which
#    f(item) returns true. Provide an implementation for filter using list comprehensions
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
print("Elements in list: ", letters)
vowelsFilter = filter(filter_vowels, letters)
vowels = list(vowelsFilter)
print("Elements after filtering", vowels)