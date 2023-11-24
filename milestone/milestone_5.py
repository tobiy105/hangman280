import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_lives = num_lives
        self.list_of_guesses = []

        print(f"The mystery word has {len(self.word)} characters")
        print(" ".join(self.word_guessed))

    @staticmethod
    def is_valid_letter_guess(guess):
        return len(guess) == 1 and guess.isalpha()

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            self.handle_correct_guess(guess)
        else:
            self.handle_incorrect_guess(guess)

    def handle_correct_guess(self, guess):
        print(f"Good guess! {guess} is in the word.")
        self.update_word_guessed(guess)

    def handle_incorrect_guess(self, guess):
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

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
        self.word_guessed = [char if char == guess or self.word_guessed[i] == guess else self.word_guessed[i] for i, char in enumerate(self.word)]
        print("Word guessed so far:", " ".join(self.word_guessed))
        if "_" not in self.word_guessed:
            print("Congratulations! You've guessed the word.")
            exit()
        print(f"Lives left: {self.num_lives}")

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif "_" not in game.word_guessed:
            print('Congratulations. You won the game!')
            break
        else:
            game.ask_for_input()

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry']
    play_game(word_list)
