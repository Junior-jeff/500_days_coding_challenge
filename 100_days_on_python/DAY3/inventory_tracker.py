#!/usr/bin/env python3

# Inventory Tracker
# - Inventory is stored as: {item_name: (quantity, price)}
# - Display all items in a table format.
# - Allow user to “buy” an item: input item name and quantity.
# - Update quantity if in stock; else, show error.
# - Loop until user types "exit".

# Initial inventory
inventory = {
    "book": (10, 1500),
    "pen": (25, 200),
    "notebook": (15, 800),
    "bag": (5, 5000),
    "ruler": (20, 150)
}

def display_inventory():
    print("\nINVENTORY")
    print("{:<12} {:>10} {:>10}".format("Item", "Quantity", "Price"))
    print("-" * 34)
    for item, (qty, price) in inventory.items():
        print("{:<12} {:>10} {:>10}".format(item, qty, price))
    print("-" * 34)

while True:
    display_inventory()
    choice = input("Enter item to buy (or type 'exit' to quit): ").strip().lower()

    if choice == 'exit':
        print("\nThank you for using the Inventory Tracker.")
        break

    if choice not in inventory:
        print("Item not found in inventory.\n")
        continue

    try:
        qty_request = int(input("Enter quantity to buy: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.\n")
        continue

    current_qty, price = inventory[choice]

    if qty_request <= 0:
        print("Quantity must be greater than 0.\n")
    elif qty_request > current_qty:
        print("Not enough stock. Only {} available.\n".format(current_qty))
    else:
        new_qty = current_qty - qty_request
        inventory[choice] = (new_qty, price)
        total = qty_request * price
        print("Purchase successful. Total cost: ₦{:,.2f}\n".format(total))

