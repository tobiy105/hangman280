
def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def main():
    while True:
        print("Guess a letter: ")
        guess = input()

        if is_valid_guess(guess):
            print("Good guess!") 
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


if __name__ == "__main__":
    main()