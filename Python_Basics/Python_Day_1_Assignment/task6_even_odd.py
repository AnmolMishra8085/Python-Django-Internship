## task6_even_odd.py
# Ask the user to enter a number.
# Print whether the number is even or odd

number = int(input("Enter a number: ")) 

if number % 2 == 0:
    print(f"{number} is an even number.")   
else:
    print(f"{number} is an odd number.")    