# Task 1: Smart Login System 
# Write a program that: 
# ● Takes username and password 
# ● If username is "admin" and password is "python123" → print "Login 
# Successful" 
# ● If username is correct but password is wrong → print "Wrong Password" 
# ● Else → print "User Not Found"


name = input("Enter your username: ")
password = input("Enter your password: ")

if name == "admin" and password == "python123":
    print("Login Successful")
elif name == "admin" and password != "python123":
    print("Wrong Password")
else:
    print("User Not Found")