#!/usr/bin/env python3

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))

# Determine contribution
if age < 18:
    contribution = 0.0
elif 18 <= age <= 60:
    if income >= 50000:
        contribution = 0.10 * income
    else:
        contribution = 0.05 * income
else:
    contribution = 0.02 * income

# Display result
print(f"{name}, your calculated contribution is ₦{contribution:.2f}")