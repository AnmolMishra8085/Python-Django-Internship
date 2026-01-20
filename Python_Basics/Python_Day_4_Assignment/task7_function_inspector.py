#                   🧾 Task 7: Function Inspector

# Write a function that:
# Accepts any arguments (*args, **kwargs)
# Prints:
# Number of positional arguments
# Number of keyword arguments
# Print all received data

#  Goal: Understand how Python sees input

def arguments(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    print(f"Total positional arguments: {len(args)}")
    print(f"Total keyword arguments: {len(kwargs)}")     
    print(f"All Received data: {args + tuple(kwargs.values())}") 
    # In kwargs, only values are printed as received data

arguments(1, 2, 'Abhinav','Shiva', name="Anmol", age=21)
