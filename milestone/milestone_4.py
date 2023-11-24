import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.list_of_guesses = []

        print(f"The mystery word has {self.num_letters} characters")
        print(self.word_guessed)

    @staticmethod
    def is_valid_letter_guess(guess):
        return len(guess) == 1 and guess.isalpha()

    def select_random_word(word_list):
        return random.choice(word_list)

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.update_word_guessed(guess)
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
        
    def ask_for_input(self):
        while self.num_lives > 0:
            print("Guess a letter: ")
            guess = input()
            if not self.is_valid_letter_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                continue
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

    def update_word_guessed(self, guess):
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.word_guessed[i] = guess
        print("Word guessed so far:", " ".join(self.word_guessed))
        if "_" not in self.word_guessed:
            print("Congratulations! You've guessed the word.")
            exit()
        print(f"Lives left: {self.num_lives}")


def main():
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry']
    game = Hangman(word_list, num_lives=5)
    game.ask_for_input()

if __name__ == "__main__":
    main()