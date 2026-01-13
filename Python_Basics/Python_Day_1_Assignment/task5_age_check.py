## task5_age_check.py
# Ask the user for their age.
# Display an appropriate message based on the age value

age = int(input("Enter your age: "))    

if age < 18:
    print("You are a minor.")   
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")