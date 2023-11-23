
def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def main():
    secret_word = "apple"
    while True:
        print("Guess a letter: ")
        guess = input()

        if is_valid_guess(guess):
            if guess in secret_word:
                print(f"Good guess! {guess} is in the word.")
                break
            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


if __name__ == "__main__":
    main()