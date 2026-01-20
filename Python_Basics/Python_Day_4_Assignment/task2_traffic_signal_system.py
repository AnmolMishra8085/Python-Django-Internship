#               🧾 Task 2: Traffic Signal System

# Write a function traffic_action(color):
# "red" → "Stop"
# "yellow" → "Ready"
# "green" → "Go"
# Any other value → "Invalid signal"

def trafic_action(color):
    if color == "red":
        return "stop"
    elif color == "yellow":
        return "Ready"
    elif color == "green":
        return "go"
    else:
        return "invalid signal"

a = input("Enter the color of the traffic light you can see now : ").lower()
print(trafic_action(a))