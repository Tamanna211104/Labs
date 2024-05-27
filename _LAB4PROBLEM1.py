#LAB4PROBLEM1
import random

def load_word_list(a):
    """Loads a list of words from a file and returns it as a list."""
    WordList = []
    with open('WordList.txt') as file:
        for line in file:
            WordList.append(line.strip())
    #word_list = [word.strip() for word in word_list]
    return WordList

def select_word(word_list):
    """Selects a random word from a list of words."""
    word = random.choice(word_list)
    return word

def display_word(word, letters_guessed):
    """Displays a word with letters that have been guessed and underscores for letters that haven't."""
    displayed_word = ""
    for letter in word:
        if letter in letters_guessed:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def play_game():
    """Plays a game of guess the word."""
    # Load the word list
    word_list = load_word_list("WordList.txt")

    # Select a random word
    word = select_word(word_list)

    # Initialize variables
    letters_guessed = []
    incorrect_guesses = 0

    # Display the word with underscores for unguessed letters
    displayed_word = display_word(word, letters_guessed)
    print("The word contains", len(word), "letters.")
    print(displayed_word)

    # Loop until the player has either guessed the word or made 6 incorrect guesses
    while "_" in displayed_word and incorrect_guesses < 6:
        # Get a letter from the player
        letter = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if letter in letters_guessed:
            print("You already guessed that letter. Try again.")
        # Check if the letter is in the word
        elif letter in word:
            letters_guessed.append(letter)
            displayed_word = display_word(word, letters_guessed)
            print(displayed_word)
        else:
            incorrect_guesses += 1
            print("Incorrect. You have", 6 - incorrect_guesses, "incorrect guesses left.")

    # Check if the player won or lost
    if "_" not in displayed_word:
        print("Congratulations! You won.")
    else:
        print("Sorry, you lost. The word was", word + ".")

# Start the game
play_game()
