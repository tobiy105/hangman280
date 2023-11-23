# Guess the Word Game

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description
Welcome to the Hangman Game project! This Python-based game is designed to be fun. 

## Project Aim
The primary aim of this project is to develop a Hangman game from scratch, allowing players to guess letters to reveal a hidden word. Through this project, you'll learn key programming concepts, including managing word lists, using the `random` module for random word selection, handling user input for letter guesses, and implementing input validation to enhance the gaming experience.

By working on this project, I learnt:

- Managing lists in Python.
- Utilising the `random` module for random selections.
- Taking user input and providing feedback.
- Implementing input validation to enhance user experience.
- Creating a Hangman game loop.
- Validating user input for single alphabetical characters.
- Checking if a guessed letter is in the secret word.
- Organizing code into functions for better modularity.

## Installation
To run the game on your local machine, follow these installation instructions:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/tobiy105/hangman280.git
2. Navigate to the project directory:
   ```bash
   cd milestone
3. Run the game by executing the following command:
   ```bash
   python milestone_2.py
3. Run the game by executing the following command:
   ```bash
   python milestone_3.py

## Usage
Once the game is running, you can play it by following these steps:

1. The game will display a message asking you to guess a letter.
2. Enter a letter (make sure it's a single alphabetical character) and press Enter.
3. If your guess is valid and in the secret word, the game will display "Good guess! {guess} is in the word.".
4. If your guess is valid but not in the secret word, the game will display "Sorry, {guess} is not in the word. Try again."
5. If your guess is invalid (e.g., you entered more than one character or a non-alphabetical character), the game will display "Invalid letter. Please enter a single alphabetical character."
6. Keep guessing until you correctly guess the word or rerun the game for a new word.

## File Structure

The project file structure is as follows:

- milestone_2.py: Contains the Python code for the "Guess the Word" game.
- README.md: This documentation file.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


