# Task 6: Find First Multiple of 7 
# Using a loop from 1–50: 
# ● Find and print the first number divisible by 7 
# ● Stop the loop immediately 

for n in range(1, 51):
    if n % 7 == 0:
        print(f"The first number divisible by 7 is: {n}")
        break