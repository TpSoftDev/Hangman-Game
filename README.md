# Hangman Game

## Description

This program implements a simple command-line Hangman game. The player attempts to guess a randomly chosen word by guessing letters one at a time. The player has a limited number of incorrect guesses (lives) before they lose the game. This project demonstrates several core programming concepts and techniques.

## How to Play

1. Run the program.
2. The program will randomly select a word from a predefined list.
3. You will be prompted to guess a letter.
4. If the guessed letter is in the word, it will be revealed in its correct positions.
5. If the guessed letter is not in the word, you lose one life.
6. The game continues until you either guess the word or run out of lives.

## Example

```
Welcome to Hangman!
You have 6 lives left and have used these letters: 
Current word: _ _ _ _ _
Guess a letter: a
You have 6 lives left and have used these letters: A
Current word: _ A _ _ _
Guess a letter: e
Letter is not in the word.
You have 5 lives left and have used these letters: A E
Current word: _ A _ _ _
...
```

## Techniques and Skills Used

### 1. **Random Choice Generation**
   - **Module:** `random`
   - **Function:** `random.choice()`
   - **Description:** Used to select a random word from a predefined list (`words`). Ensures each game starts with a different word, adding variety and replay value.

### 2. **String Manipulation**
   - **Module:** `string`
   - **Operations:** Uppercasing, joining, and checking substrings.
   - **Description:** Manages the display of the word to the user with guessed and unguessed letters. Handles user input to ensure case-insensitive comparisons.

### 3. **Control Flow**
   - **Structures:** Loops (`while`), conditionals (`if`, `elif`, `else`).
   - **Description:** Controls the game loop, processing each guess and updating the game state (lives, used letters, current word display) accordingly.

### 4. **Functions**
   - **Modularity:** `get_valid_word()`, `hangman()`
   - **Description:** Encapsulates game logic in functions for clarity and reusability. `get_valid_word()` handles word selection, while `hangman()` manages the game flow.

### 5. **Input Validation**
   - **Checks:** Validates user input to ensure it is a single alphabetical character that has not been guessed before.
   - **Feedback:** Provides real-time feedback to the user on invalid or repeated guesses.

### 6. **Set Operations**
   - **Sets:** `set()`
   - **Description:** Uses sets to manage the letters in the chosen word (`hangman_word_letters`) and the letters guessed by the user (`used_letters`). Efficiently checks membership and updates the game state.

### 7. **Docstrings and Comments**
   - **Documentation:** Docstrings provide clear explanations of function purposes, arguments, and return values.
   - **Inline Comments:** Added to clarify key parts of the code, improving readability and maintainability.

### 8. **PEP 8 Compliance**
   - **Style Guide:** Follows Python's PEP 8 style guide for consistent and readable code.

## Requirements

- Python 3.x
- A `words.py` file containing a list of words named `words`.

Enjoy the game!
