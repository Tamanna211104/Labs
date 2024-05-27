import random

# Generate a random 4-letter code
def generate_code():
    code = []
    for i in range(4):
        code.append(random.choice(['A', 'B', 'C', 'D', 'E', 'F']))
    return code

# Compare the guess with the code and return feedback
def get_feedback(code, guess):
    feedback = []
    for i in range(4):
        if guess[i] == code[i]:
            feedback.append('1')
        elif guess[i] in code:
            feedback.append('2')
        else:
            feedback.append('3')
    return feedback

# Main game loop
def play_game():
    print("Welcome to MasterMind!")
    code = generate_code()
    num_guesses = 0
    while True:
        guess = input("Guess the Code: ").upper()
        if len(guess) != 4 or not all(letter in ['A', 'B', 'C', 'D', 'E', 'F'] for letter in guess):
            print("Invalid input. Please enter 4 letters from A to F.")
            continue
        num_guesses += 1
        feedback = get_feedback(code, guess)
        print(''.join(feedback))
        if feedback == ['1', '1', '1', '1']:
            print("You guessed it right!")
            print("Number Of Guesses:", num_guesses)
            break

# Start the game
play_game()
