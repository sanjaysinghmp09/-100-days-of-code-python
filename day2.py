# Day 2: Python Fundamentals

# Variables and Data Types
name = "Sanjay"
age = 20
is_student = True
height = 5.8  # in feet

print(f"My name is {name}, and I am {age} years old.")
print(f"Am I a student? {is_student}")
print(f"My height is {height} feet.")

# Conditional Statements
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# Loops: Example of a for loop
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Functions
def greet_user(username):
    return f"Hello, {username}! Welcome to Day 2 of Python."

print(greet_user(name))

# Lists and Basic Operations
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("\nFruits List:", fruits)

# Dictionary Example
person = {"name": "Sanjay", "age": age, "city": "Bhopal"}
print("Person Dictionary:", person)

# Simple User Input (commented out for now)
# user_name = input("Enter your name: ")
# print(f"Nice to meet you, {user_name}!")

# End of Day 2
print("\nKeep learning and coding!")
