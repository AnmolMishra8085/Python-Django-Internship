## task4_calculator.py
# Take two numbers as input.
# Print their sum, difference, and multiplication.

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))    

sum_result = n1 + n2
difference_result = n1 - n2     
multiplication_result = n1 * n2
print(f"The sum of {n1} and {n2} is: {sum_result}")
print(f"The difference when {n2} is subtracted from {n1} is: {difference_result}")
print(f"The multiplication of {n1} and {n2} is: {multiplication_result}")