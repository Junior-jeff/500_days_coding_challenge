#!/usr/bin/env python3

# 3. Shopping Discount Logic*  
# Ask the user to enter number of items and price per item.  
# - Compute total price.  
# - Apply discount:  
# - ≥5 items and total > 5000 → 15% off  
# - ≥5 items → 10%  
#  - <5 items → no discount  
# - Print final price.

# Get user input
num_items = int(input("Enter the number of items: "))
price_per_item = float(input("Enter the price per item: "))

# Calculate total price
total_price = num_items * price_per_item

# Apply discount
if num_items >= 5 and total_price > 5000:
    discount = 0.15 * total_price
elif num_items >= 5:
    discount = 0.10 * total_price
else:
    discount = 0.0

final_price = total_price - discount

# Display result
print(f"Total price: ₦{total_price}\nDiscount: ₦{discount}\nFinal Price: ₦{final_price:.2f}.")

