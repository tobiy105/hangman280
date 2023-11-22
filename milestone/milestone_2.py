import random

def select_random_word(word_list):
    return random.choice(word_list)

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def main():
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry']
    word = select_random_word(word_list)

    print("Enter a letter: ")
    guess = input().lower()  

    if is_valid_guess(guess):
        if guess in word:
            print("Good guess!")
        else:
            print("Oops! That letter is not in the word.")
    else:
        print("Oops! That is not a valid input.")

if __name__ == "__main__":
    main()
