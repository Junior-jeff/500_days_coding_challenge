#!/usr/bin/env python3

# Password Locker & Strength Validator
# - User creates passwords and stores them in a list if valid.
# - Password must contain: 1 uppercase, 1 lowercase, 1 digit, 1 special character, and be ≥8 characters.
# - Prevent duplicate passwords using a set.
# - Print a formatted summary of all valid passwords at the end.

import string

valid_passwords = []
password_set = set()
special_chars = string.punctuation

while True:
    pwd = input("Enter a password (or type 'done' to finish): ").strip()
    if pwd.lower() == 'done':
        break

    # Duplicate check
    if pwd in password_set:
        print("Password already used. Try another.\n")
        continue

    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in special_chars for c in pwd)

    if all([has_upper, has_lower, has_digit, has_special]) and len(pwd) >= 8:
        valid_passwords.append(pwd)
        password_set.add(pwd)
        print("Password saved.\n")
    else:
        print("Invalid password. Must contain:")
        if not has_upper:
          print("  - At least one UPPERCASE letter")
        if not has_lower:
            print("  - At least one lowercase letter")
        if not has_digit:
            print("  - At least one digit")
        if not has_special:
            print("  - At least one special character ({})".format(special_chars))
        if len(pwd) < 8:
            print("  - Minimum 8 characters")
        print()

# Summary
print("\nSAVED PASSWORDS")
print("-" * 25)
for i, p in enumerate(valid_passwords, 1):
    print("{}. {:<20}".format(i, p))

