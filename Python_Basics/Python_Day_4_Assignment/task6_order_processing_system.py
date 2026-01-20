#                  🧾Task 6: Order Processing System

# Create a function:
# process_order(item, quantity=1, **options)
# Rules:
# Base prices:
# pizza → 200
# burger → 120
# Optional options:
# extra_cheese=True → +50
# home_delivery=True → +30
# Print final bill

def process_order(item, quantity=1, **options):
    base_prices = {
        "pizza": 200,
        "burger": 120
    }
    
    if item not in base_prices:
        print("Item not available")
        return                                        # Early exit if item not found
    
    total = base_prices[item] * quantity
    
    if options.get("extra_cheese", False):            # false is default if key not found
        total += 50 * quantity
    if options.get("home_delivery", False):
        total += 30
    
    print(f"Final bill for {quantity} {item}(s): ₹{total}")

process_order("pizza", 2, extra_cheese=True, home_delivery=True)
process_order("burger", home_delivery=True)
process_order("pasta") 
process_order("pizza", 3)