# Task 4: Operator Story 
# Ask the user for two numbers and: 
# ● Show results using arithmetic operators 
# ● Compare the two numbers 
# ● Print a logical decision using if-else 
# Make the output fun or conversational. 
# Submission instructions remain same! 

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

# Arithmetic operations

addition = a + b
subtraction = a - b 
multiplication = a * b
division = a / b if b != 0 else "undefined (cannot divide by zero)"
modulus = a % b if b != 0 else "undefined (cannot divide by zero)"
print(f"\nLet's do some fun with numbers {a} and {b}!")
print(f"Addition: {a} + {b} = {addition}")  
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")
print(f"Modulus: {a} % {b} = {modulus}")

# Comparison operations

print("\nNow, let's compare these two numbers:")

if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is less than {b}.")
else:
    print(f"{a} is equal to {b}.")

# Logical decision

if a % 2 == 0 and b % 2 == 0:
    print(f"\nBoth {a} and {b} are even numbers. Even Steven!") 
elif a % 2 != 0 and b % 2 != 0:
    print(f"\nBoth {a} and {b} are odd numbers. Odd Squad!")
else:
    print(f"\nOne of the numbers is even and the other is odd. A perfect pair of opposites")

