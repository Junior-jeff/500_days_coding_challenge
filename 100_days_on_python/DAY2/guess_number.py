#!/usr/bin/env python3

# Number Guessing Game (Limited Attempts)*
# - Prompt user to guess a secret number (predefined).
# - Convert input to integer (type casting).
# - Use logical operators and conditional expressions to give hints (e.g., too high, too low).
# - Allow 5 attempts using a `while` loop.
# - Use string indexing and format specifiers to show current attempt and remaining tries.

secret_number = 42
max_attempts = 5
attempt = 1

while attempt <= max_attempts:
    guess = input("Attempt {} of {}\nGuess the number: ".format(attempt, max_attempts))

    if not guess.isdigit():
        print("Invalid input. Please enter a number.\n")
        continue

    guess = int(guess)

    if guess == secret_number:
        print("Correct! You guessed the number in attempt {}.".format(attempt))
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

    remaining = max_attempts - attempt
    if remaining > 0:
        print("You have {:>2} attempt(s) left.\n".format(remaining))
    else:
        print("\nGame over! The number was {}.".format(secret_number))

    attempt += 1
