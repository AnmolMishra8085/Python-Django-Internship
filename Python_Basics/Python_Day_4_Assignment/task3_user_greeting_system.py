#              🧾 Task 3: User Greeting System

# Create a function greet_user(name, role="student"):
# If role is "student" → "Welcome student <name>"
# If role is "admin" → "Welcome admin <name>"
# Call function:
#     Once, with only the name
#     Once with name + role (keyword argument)

def greet_user(name, role="student"):
    match role:
        case "student":
            print(f"Welcome student {name}")
        case "admin":
            print(f"Welcome admin {name}")
        case _:
            print(f"Welcome {name}")

greet_user("Shiva")
greet_user("Arayan", role="admin") 
greet_user("Riya", role="guest")
