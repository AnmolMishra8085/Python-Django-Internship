# Task 4: Number Analyzer 
# Using a for loop from 1 to 20: 
# ● Print "Even" for even numbers 
# ● Print "Odd" for odd numbers 
# ● Skip number 13 using continue 

for num in range(1, 21):
    if num == 13:
        continue
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")