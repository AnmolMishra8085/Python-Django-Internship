# Task 2: Electricity Bill Checker 
# Input units consumed: 
# ● Units < 100 → "No Charge" 
# ● Units between 100–300 → "Normal Usage" 
# ● Units > 300 → "High Usage – Save Energy!"

units = int(input("Enter the number of units consumed in House : "))

if units < 100:
    print("No Charge")  
elif 100 <= units <= 300:
    print("Normal Usage")
else:
    print("High Usage – Save Energy!")
