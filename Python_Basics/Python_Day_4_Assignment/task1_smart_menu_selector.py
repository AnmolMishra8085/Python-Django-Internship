#                🧾 Task 1: Smart Menu Selector

# Create a function food_menu(choice) that:
# Uses match
# Accepts a string ("pizza", "burger", "coffee")
# Prints the price:
# pizza → ₹250
# burger → ₹150
# coffee → ₹100
# Default case → "Item not available"

# Use match, not if-else.


def food_menu(choice):
    match choice:
        case "Aapka pizza":
            print("₹250")
        case "Mera burger":
            print("₹150")
        case "Hamari coffee":
            print("₹100")
        case _:
            print("Item not available, kal aana")

a = input("Enter your choice (Aapka pizza, Mera burger, Hamari coffee): ")
food_menu(a)
