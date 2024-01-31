import random

# Generate a random number between 1 and 10
number_to_guess = random.randint(1, 10)

# Initialize a variable to keep track of the number of guesses
num_guesses = 0

# Prompt the user to guess the number
while True:
    # Get the user's guess as a string
    guess_str = input("Guess the number between 1 and 10: ")

    # Convert the user's guess to an integer
    guess = int(guess_str)

    # Increment the number of guesses
    num_guesses += 1

    # Check if the user's guess is correct
    if guess == number_to_guess:
        print(f"Congratulations! You guessed the number in {num_guesses} guesses!")
        break

    # Check if the user's guess is too high
    elif guess > number_to_guess:
        print("Too high! Try again.")

    # Check if the user's guess is too low
    elif guess < number_to_guess:
        print("Too low! Try again.")

    # Check if the user has exceeded the maximum number of guesses
    if num_guesses >= 5:
        print("Sorry, you've exceeded the maximum number of guesses. The number was {}.".format(number_to_guess))
        break
