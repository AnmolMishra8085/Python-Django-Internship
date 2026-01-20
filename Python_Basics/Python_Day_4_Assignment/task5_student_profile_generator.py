#               🧾 Task 5: Student Profile Generator

# Create a function student_profile(name, **details) that:
# Prints the student's name
# Prints all provided details like:age, coursecity
# If no extra details → "No additional info"
#  Focus: Dynamic keyword arguments

def student_profile(name, **details):
    print(f"Student Name: {name}")
    if details:
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No additional info") 

student_profile("Anmol", age=21, course="Python", city="Jamuna Colliery")
student_profile("Riya")
student_profile("Arayan", age=22)