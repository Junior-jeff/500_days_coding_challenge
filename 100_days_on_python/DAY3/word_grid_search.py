#!/usr/bin/env python3

# Word Grid Search (2D Collection Challenge)
# - Create a 4×4 grid of random letters (2D list).
# - Ask the user to input a word.
# - Check if the word can be found horizontally in any row (left-to-right only).
# - Use nested loops and string comparison.
# - Print success/failure using format specifiers.

import random
import string

# Generate 4x4 grid of random uppercase letters
grid = [[random.choice(string.ascii_uppercase) for _ in range(4)] for _ in range(4)]

# Display the grid
print("\nWORD GRID")
for row in grid:
    print(" ".join(row))

# Get word input from user
word = input("\nEnter a word to search (uppercase only): ").upper()

found = False

# Search each row
for i, row in enumerate(grid):
    row_str = ''.join(row)
    if word in row_str:
        found = True
        print("\nWord '{}' found in row {} → {}".format(word, i + 1, row_str))
        break

if not found:
    print("\nWord '{}' not found in any row.".format(word))
