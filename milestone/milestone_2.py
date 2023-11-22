import random

word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry']
word = random.choice(word_list)

print("Enter a letter: ")
guess = input()
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")