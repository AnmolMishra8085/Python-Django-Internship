#             🧾 Task 4: Flexible Calculator (*args)

# Create a function calculate_total(*numbers) that:
# Accepts any number of values
# Returns their sum
# If no values passed → return 0

from unittest import result


def calculate_total(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
a = input("Enter numbers separated by spaces: ")
numbers = map(float, a.split())  # Convert input strings to floats
output = calculate_total(*numbers)
print("The total sum is:", output) 
# the total sum is: 0 if no numbers are provided
# output value will be float type