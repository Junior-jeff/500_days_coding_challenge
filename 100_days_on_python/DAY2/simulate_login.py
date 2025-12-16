#!/usr/bin/env python3

# Login System Simulation
# - Ask for a username and password.
# - Use a while loop to allow 3 login attempts.
# - Use string methods to ignore case sensitivity for username.
# - Use logical operators to check multiple credentials.
# - Print formatted output showing success or failure.

correct_username = junior-jeff
correct_password = Junior_j377

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if username.lower() == correct_username.lower() and password == correct_password:
        print("Login successful!\nWelcome, {}.".format(username))
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print("Incorrect credentials.\nAttempts left: {:>2}".format(remaining))

        if remaining == 0:
            print("Account locked. Too many failed attempts.")