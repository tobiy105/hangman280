def get_user_guess():
    print("Guess a letter: ")
    guess = input()
    return guess

def is_guess_correct(word, guess):
    guess = guess.lower()
    return guess in word

def is_valid_letter_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def main():
    secret_word = "apple"
    while True:
        guess = get_user_guess()

        if is_valid_letter_guess(guess):
            if is_guess_correct(secret_word, guess):
                print(f"Good guess! {guess} is in the word.")
                break
            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

if __name__ == "__main__":
    main()
