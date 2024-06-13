import random
import string
from words import words

def get_valid_word(words):
    """
    Randomly selects a valid word from the list of words.
    A valid word does not contain dashes or spaces.
    
    Args:
        words (list): List of words to choose from.
    
    Returns:
        str: A valid word in uppercase.
    """
    word = random.choice(words)  # Randomly choose a word
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    """
    Main function to play the Hangman game.
    Prompts the user to guess letters and provides feedback on their guesses.
    """
    hangman_word = get_valid_word(words)
    hangman_word_letters = set(hangman_word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase)  # Set of uppercase English letters
    used_letters = set()  # Letters guessed by the user
    lives = 6

    # Game loop: continue until the word is guessed or the user runs out of lives
    while len(hangman_word_letters) > 0 and lives > 0:
        # Display current status to the user
        print(f"\nYou have {lives} lives left and have used these letters: {' '.join(used_letters)}")
        word_list = [letter if letter in used_letters else '_' for letter in hangman_word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        # Check if the guessed letter is valid and not already used
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in hangman_word_letters:
                hangman_word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Letter is not in the word.")
        elif user_letter in used_letters:
            print("You have already guessed that character. Try again.")
        else:
            print("Invalid character. Please try again.")

    # End of game messages
    if lives == 0:
        print(f'You died. Sorry, the word was {hangman_word}\n')
    else:
        print(f'Congratulations! You guessed the correct word: {hangman_word}\n')

if __name__ == "__main__":
    hangman()