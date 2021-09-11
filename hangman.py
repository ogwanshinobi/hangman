import sys
import random

import RandomWords from random_word

r = RandomWords()

# Function asks user for number of wrong attempts for the game
def get_num_attempts():
    # Get user-inputted number of incorrect attempts for game
    while True:
        num_attempts = input ("How many incorrect attempts do you think you'll need? [1-25] ")
        try:
            num_attempts = int (num_attempts)
            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print ("{0} is not an integer between 1 and 25".format(num_atttempts))
        except ValueError:
            print ("{0} is not an integer between 1 and 25".format(num_attempts))

# Fuction asks user to enter length of word to be predicted
def get_min_word_length():
    while True:
        min_word_length = input ("What minumum word length do you want? [4-16]")
        try:
            min_word_length = int (min_word_length)
            if 4 <= min_word_length <= 16:
                return min_word_length
            else:
                print ("{0} is not between 4 and 16".format(min_word_length))
        except ValueError:
            print ("0} is not between 4 and 16".format(min_word_length))

# Function displays word if word length and index length are not the same
def get_display_word(word, idxs):
    # Get word suitable for display
    if len (word) != len (idxs):
        raise ValueError ("Word length and indices are CLEARLY not the same. Try again.")
        displayed_word = " ".join([letter if indx[i] else "*" for i, letter in enumerate (word)])
        return displayed_word.strip()

# Function gets next guess from user as input
from string import ascii_lowercase
def get_next_letter(remaining_letters):
    if len (remaining_letters) == 0:
        raise ValueError ("There are no remaining letters.")
    while True:
        next_letter = input ("Guess a character").lower()
# Checks if next letter is not more than a single character
        if len (next_letter) != 1:
            print ("{0} is not a single character...try again.".format(next_letter))
# Checks if next letter is a letter (and no other character)
        elif next_letter not in ascii_lowercase:
            print ("{0} isn't even a letter...try again.".format(next_letter))
# Checks if next letter hasn't already been guessed 
        elif next_letter not in remaining_letters:
            print ("WRONG! {0} has been guessed before.".format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter

# Integrate above functions and allow user to retry if they would like
def play_hangman():
# Greet the user : )
    name = input ("What's your name?\n")

    choice = input (f"Hello, {name}, wanna play a game? [y/n] \n")
    if "y" in choice: 
        print ("Great! Let's play hangman")
    if "n" in choice:
        print ("Bye bye!")
        sys.exit()

# Let player set difficulty
    print ("Starting a game of Hangman...")
    attempts_remaining = get_num_attempts()
    min_word_length = get_min_word_length()

# Randomly selects word
    print ("Selecting a super hard word...")
    word = r.get_random_word(min_Length = (min_word_length-1))
    print ()

# Initialize game state variables
    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set (ascii_lowercase)
    wrong_letters = []
    word_solved = False

# Main game loop
    while attempts_remaining > 0 and not word_solved:
# Print game state
        print ("Word: {0}".format(get_display_word(word, idxs)))
        print ("Attempts remaining: {0}".format(attempts_remaining))
        print ("Previous guesses: {0}".format(" ".join(wrong_letters)))

# Get player's next letter guess
        next_lettter = get_next_letter(remaining_letters)

        # Check if letter guess is in word
        if next_letter in word:
            # Guessed correctly
            print ("Huzzah! {0} is in the word!".format(next_letter))
            # Reveal matching letters
            for i in range (len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            # Guessed incorrectly
            print ("Womp womp...{0} is NOT in the word!".format(next_letter))

            # Decrement number of attempts left and append guess to wrong guesses
            attempts_remaining -= 1
            wrong_letters.append(next_letter)

            # Check if word is solved
        if False not in indx:
            word_solved = True
        print ()

        # The game is over: reveal word
        print ("The word is {0}".format(word))

        # Notifies player if they won or lost
        if word_solved:
            print ("Congrats Smarty Pants {name}! You won!")
        else:
            print ("Womp...sorry, {name}. You lose.")

        # Ask player if they want to try again
        try_again = input ("Would you like to try again? [y/n]  ")
        return try_again.lower() == "y"
    if __name__ == "__main__":
        while play_hangman():
            print ()
