#!/usr/bin/env python3

# Password Validator & Strength Checker
# Write a program that:
# - Asks for a password input from the user.
# - Uses string methods and indexing to check:
# - At least one uppercase, one lowercase, one digit, and one special character.
# - Uses logical and conditional expressions to evaluate strength.
# - While loop should repeat until a valid password is entered.
# - Use format specifiers to display feedback.

import string

special_chars = string.punctuation

while True:
    password = input("Enter a password: ")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_chars for c in password)

    if all([has_upper, has_lower, has_digit, has_special]):
        length_score = len(password)
        if length_score >= 12:
            strength = "Strong"
        elif length_score >= 8:
            strength = "Moderate"
        else:
            strength = "Weak"

        print("You entered a valid password!\nStrength: {:>8}".format(strength))
        break
    else:
        print("\nPassword must contain at least: ")
        if not has_upper:
            print("one UPPERCASE letter")
        if not has_lower:
          print("one lowercase letter")
        if not has_digit:
            print("one digit")
        if not has_special:
            print("one special character ({})".format(special_chars))
        print("Please try again.\n")
