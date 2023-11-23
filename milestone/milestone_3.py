def ask_for_input():
    print("Guess a letter: ")
    guess = input()
    return guess

def check_guess(word, guess):
    guess = guess.lower()
    if guess in word:
        return True
    else:
        return False

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def main():
    secret_word = "apple"
    while True:
        guess = ask_for_input()

        if is_valid_guess(guess):
            if check_guess(secret_word, guess):
                print(f"Good guess! {guess} is in the word.")
                break
            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

if __name__ == "__main__":
    main()