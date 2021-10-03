"""
This code should request a word from the user and return how many vowels that
word contains.

Find the bug.
"""

word = input("Type a word: ")
num_vowels = 0
vowels = ["a", "e", "i", "o", "u"]

for letter in word.lower():
    if letter in vowels:
        num_vowels += 1

print('There are {} vowels in "{}"'.format(num_vowels, word))
