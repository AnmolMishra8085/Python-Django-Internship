# Task 3: Movie Eligibility 
# Ask user for: 
# ● Age 
# ● Has ID card? (yes/no) 
# Conditions: 
# ● Age ≥ 18 and ID card = yes → "Entry Allowed" 
# ● Else → "Entry Denied"

age = int(input("Enter your age: "))
id_card = input("Do you have an ID card? (yes/no): ")

if age >= 18 and id_card.lower() == "yes":
    print("Entry Allowed")  
else:
    print("Entry Denied")
    