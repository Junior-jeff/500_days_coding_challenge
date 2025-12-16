#!/usr/bin/env python3

# 4. Simple ATM Withdrawal Validator*  
# Prompt user for account balance and withdrawal amount.  
# - Ensure values are numbers.  
# - If withdrawal > balance → deny with error 
# - - If withdrawal % 100 ≠ 0 → deny (ATM dispenses in 100s)  
# - Else subtract and show new balance.

# Get user input
balance = float(input("Enter your account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

# Validate operation
if withdraw > balance:
    print("Error: Insufficient funds.")
elif withdraw % 100 != 0:
    print("Error: ATM dispenses only in multiples of ₦100.")
else:
    balance -= withdraw
    print(f"Withdrawal successful.\nNew balance: ₦{balance:.2f}")

