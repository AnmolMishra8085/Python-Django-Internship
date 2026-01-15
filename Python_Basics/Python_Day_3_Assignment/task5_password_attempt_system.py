# Task 5: Password Attempt System 
# ● User gets 3 attempts to enter the correct password 
# ● If correct → "Access Granted" and stop loop 
# ● If 3 attempts fail → "Account Locked" 

# Use: 
# ● while loop 
# ● break 

password = "pass"
attempts = 0

while attempts < 3:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access Granted")
        break
    attempts += 1
if attempts == 3:
    print("Account Locked")